# Forecast Model Benchmarking
Accuracy vs Stability vs Tail Risk

This project benchmarks multiple forecasting approaches and highlights a key
production reality:

The best average accuracy model is not always the best operational model.

Rather than reporting one headline metric, this repo evaluates models across:
- overall accuracy (WAPE / MAE)
- stability (rolling error drift)
- tail risk (p90 / max absolute errors)
- robustness under stress regimes

The focus is on model selection trade-offs and decision-ready evaluation.

---

## Why This Project

Many portfolios present one model and one metric.
In production, you usually choose a model based on multiple competing goals:
- reduce average error
- avoid catastrophic misses
- maintain stability over time
- behave reasonably under regime shifts

This project makes those trade-offs explicit.

---

## Repository Structure

```text
forecast-model-benchmarking/
├── notebooks/   # narrative benchmarking workflow
├── src/         # reusable benchmarking utilities
├── data/        # generated datasets (gitignored)
└── outputs/     # benchmark tables and key plots

## How to Read

1. 00_project_brief.ipynb

2. 01_data.ipynb

3. 02_models.ipynb

4. 03_tradeoff_analysis.ipynb 

---

## Author

Yeji Choe  
Data Scientist – Forecasting & Decision Systems  
Auckland, New Zealand


---


---

# `notebooks/00_project_brief.ipynb`

### Markdown cell

```markdown
# Project Brief: Forecast Model Benchmarking

Goal:
Benchmark multiple forecasting models and compare them across dimensions that
matter in production.

We evaluate:
- average accuracy
- stability over time
- tail risk (p90/max error)
- performance during stress regimes

Outcome:
A summary table and a single clear chart showing accuracy vs stability.

PROJECT_NAME = "forecast-model-benchmarking"
