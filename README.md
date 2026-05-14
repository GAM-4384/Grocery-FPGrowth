# Grocery-FPGrowth

**Frequent Itemset Mining on Grocery Transactions Using the FP-Growth Algorithm**

---

## Overview

This project applies the FP-growth algorithm to a real-world supermarket transaction dataset (9,836 shopping baskets) to discover frequently co-purchased item combinations. The pipeline covers data loading and preprocessing, frequent itemset mining across multiple support thresholds, result filtering, visualisation, and a performance benchmarking report.

---

## Algorithm

FP-growth (Frequent Pattern Growth) constructs a compact FP-tree from the transaction database and mines frequent itemsets directly from the tree structure, avoiding the repeated dataset scans required by Apriori. This makes it significantly faster at low support thresholds.

---

## Pipeline

```
groceries.csv
      │
      ▼
DataProcessor
  ├─ Parse comma-separated transaction records
  └─ One-hot encode items → transaction matrix
      │
      ▼
FPAnalyzer
  ├─ Run FP-growth (mlxtend) at configured min_support
  ├─ Collect frequent itemsets with support values
  └─ Filter by itemset length (e.g. length = 2)
      │
      ▼
Visualizer
  ├─ Support distribution plot
  └─ Itemset size distribution plot
      │
      ▼
PerformanceAnalyzer
  ├─ Sweep support thresholds: 0.005 → 0.05
  ├─ Record execution time and itemset count per threshold
  ├─ Plot performance comparison chart
  └─ Write performance_report.txt
```

---

## Project Structure

```
Grocery-FPGrowth/
├── main.py                     # Entry point: orchestrates the full pipeline
├── groceries.csv               # Raw transaction dataset (9,836 baskets)
├── requirements.txt            # Python dependencies
├── fp_analysis.log             # Runtime log (auto-generated)
├── performance_report.txt      # Benchmark results (auto-generated)
│
├── src/
│   ├── data_processor.py       # CSV parsing and one-hot encoding
│   ├── fp_analyzer.py          # FP-growth mining and result filtering
│   └── visualizer.py           # Support/size distribution and performance plots
│
└── utils/
    └── performance.py          # Multi-threshold benchmarking and report generation
```

---

## Performance Benchmark

Results on the Groceries dataset (9,836 transactions, 169 unique items):

| Min Support | Execution Time | Frequent Itemsets Found |
|---|---|---|
| 0.5% | 14.44 s | 1,001 |
| 1.0% | 5.24 s | 333 |
| 2.0% | 1.43 s | 122 |
| 3.0% | 0.44 s | 63 |
| 5.0% | 0.18 s | 31 |

At 1% support, 333 frequent itemsets are found, of which 3 are length-2 pairs (items that appear together in at least 1% of all baskets).

---

## Dataset

The Groceries dataset contains 9,836 real-world point-of-sale transactions from a grocery store. Each row lists the items purchased in a single basket, separated by commas. It is a standard benchmark dataset for association rule mining research.

---

## Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run the full pipeline
python main.py
```

Output files written to the project root after a successful run: `fp_analysis.log`, `performance_report.txt`, and several `.png` chart files.

The default minimum support threshold is set in `src/fp_analyzer.py`. Lowering it increases result count and runtime substantially (see benchmark table above).

---

## License

This repository is released for academic and non-commercial use only.

Copyright © 2024 Merlin. All rights reserved.

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND.
