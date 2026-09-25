/* Local application acceptance: MathJax, actual form submissions and containment. */
const path = require('path');
const fs = require('fs');
const assert = require('assert/strict');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'C:/Users/Nevo/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

async function main() {
  const output = path.resolve(process.argv[2]);
  const base = process.argv[3] || 'http://127.0.0.1:8892';
  fs.mkdirSync(output, { recursive: true });
  const browser = await chromium.launch({ headless: true, channel: 'msedge' });
  const report = { origin: base, scope: 'Local preview; not proof of live deployment', checked_at: new Date().toISOString(), pages: [] };
  const keys = ['earnings-bridge','reinvestment','sbc-dilution','equity-value','bank-capital','insurer-remittances','sector-stress'];
  try {
    for (const viewport of [{width:1365,height:900},{width:390,height:844}]) {
      const page = await browser.newPage({viewport});
      for (const key of [...keys, 'dcf-value','business-credit']) {
        const route = keys.includes(key) ? '/calculators/valuation/'+key+'/' : '/calculators/'+key+'/';
        const response = await page.goto(base+route, {waitUntil:'networkidle'});
        assert.equal(response.status(),200,route);
        await page.waitForFunction(() => !!window.MathJax?.startup?.promise, {timeout:30000});
        await page.evaluate(() => window.MathJax.startup.promise);
        const maths = await page.locator('.symbol-table .math-inline').evaluateAll(nodes => nodes.map(n => ({rendered:!!n.querySelector('mjx-container'), error:!!n.querySelector('mjx-merror,[data-mjx-error]')})));
        assert(maths.length > 0, 'Missing symbol table '+route);
        assert(maths.every(m => m.rendered && !m.error), 'Unrendered/error symbol '+route);
        assert.equal(await page.locator('mjx-merror,[data-mjx-error]').count(),0,route);
        const layout = await page.evaluate(() => ({client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth}));
        assert(layout.scroll <= layout.client+1, 'Page overflow '+route+' '+JSON.stringify(layout));
        if (keys.includes(key)) {
          await page.getByRole('button',{name:'Calculate scenario',exact:true}).click();
          await page.waitForLoadState('networkidle');
          assert.equal(await page.locator('[role="alert"]').count(),0,'Default form failure '+route);
          assert((await page.locator('#valuation-results tbody tr').count()) > 0,'No result rows '+route);
          if (viewport.width > 1000) {
            const downloadPromise = page.waitForEvent('download');
            await page.getByRole('button',{name:'Download inputs and results (CSV)'}).click();
            const download = await downloadPromise;
            assert.equal(await download.failure(),null,'CSV failure '+route);
          }
        }
        await page.locator('.symbol-table').scrollIntoViewIfNeeded();
        await page.locator('.symbol-table').evaluate(node => node.scrollIntoView({block:'start',behavior:'instant'}));
        if (keys.includes(key)) assert(await page.locator('.symbol-table').evaluate(node => node.scrollWidth <= node.clientWidth+1), 'Symbol definitions overflow '+route);
        await page.screenshot({path:path.join(output, `${key}-${viewport.width}-symbols.png`)});
        if (key === 'earnings-bridge' || key === 'insurer-remittances') {
          await page.locator('#valuation-results > h2').first().evaluate(node => node.scrollIntoView({block:'start',behavior:'instant'}));
          await page.screenshot({path:path.join(output,`${key}-${viewport.width}-results.png`)});
        }
        report.pages.push({route,viewport:viewport.width,symbols:maths.length,mathjax:true,overflow:false,default_form:keys.includes(key)?'passed':'not repeated',csv:keys.includes(key)&&viewport.width>1000?'passed':'not repeated'});
      }
      await page.close();
    }
    const page = await browser.newPage();
    await page.goto(base+'/calculators/valuation/equity-value/');
    await page.locator('#id_discount').fill('2');
    await page.getByRole('button',{name:'Calculate scenario',exact:true}).click();
    await page.waitForLoadState('networkidle');
    assert((await page.locator('[role="alert"]').textContent()).includes('must exceed perpetual growth'));
    assert.equal(await page.locator('#valuation-results .result-box').count(),0);
    // A real JavaScript-disabled visit keeps symbol definitions readable.
    const fallback = await browser.newPage({javaScriptEnabled:false});
    await fallback.goto(base+'/calculators/dcf-value/');
    assert(await fallback.locator('.symbol-table .formula-fallback').first().isVisible());
    assert(!(await fallback.locator('.symbol-table .formula-tex').first().isVisible()));
    report.invalid_rate='rejected without stale results';
    report.no_javascript='readable symbol fallback';
    report.status='passed';
  } finally {
    fs.writeFileSync(path.join(output,'browser-qa.json'),JSON.stringify(report,null,2));
    await browser.close();
  }
  console.log(JSON.stringify({status:report.status,pages:report.pages.length,report:path.join(output,'browser-qa.json')}));
}
main().catch(error => { console.error(error); process.exitCode=1; });
