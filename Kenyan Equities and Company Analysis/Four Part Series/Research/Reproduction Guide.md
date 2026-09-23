# Reproducing the numerical experiments

The numerical engine is `reproduce_models.py`, supplied beside `sources.json` and `issuer_directory.json`. It requires Python 3 and NumPy. From this Research directory, run:

```powershell
python reproduce_models.py
```

The engine writes `portfolio_results.json`, `simulation_results.json`, the four exact formula-audit CSV files, and a spreadsheet specification named `spec.json` in this directory. It uses fixed seeds and common random numbers for comparisons. Rerunning without changing inputs should reproduce the published numerical results to floating-point precision. It does not overwrite the delivered XLSX files or regenerate article prose and illustrations.

To change a large experiment, edit the named input arrays and case definitions in a copy of the engine: `mu`, `vol`, `loading`, `weights`, `crisis_losses`, and the contribution, inflation and withdrawal cases passed to `run`. The `run` function returns both summary measures and the full annual wealth history. The current layout uses eight assets, twenty years and 10,000 paths. Extending those dimensions also requires changing the associated array shapes, loops, labels and goal horizon. The sampled search uses explicit long-only, bank-sector, single-equity and bill-weight constraints; update the filter when changing the policy.

The XLSX files already contain live formulas for their documented inputs. The larger experiment and selected-search snapshots can be refreshed by transferring newly generated results into their clearly labelled snapshot tables, or by rebuilding XLSX from the generated specification using a spreadsheet authoring tool. Formula-audit CSV files contain exact Excel expressions as text for inspection. Keep their original versions with the published articles if you change the model, so numerical results remain traceable to the assumptions that produced them.

The article citation map connects each article's local IEEE reference numbers to the common source IDs used in the workbooks. Source URLs and scope notes are in `sources.json` and `References.md`. The directory is a dated research starting point; the engine does not fetch fresh prices or filings automatically.
