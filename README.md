# Customer Churn & Retention Analytics

A Python/Pandas portfolio project analyzing customer churn patterns in the **IBM Telco Customer Churn** dataset.

## Project Overview
The dataset contains **7,043 customers**. This project cleans the data, engineers tenure cohorts, measures churn across customer segments, and translates the strongest observed patterns into retention hypotheses.

## Tools
- Python
- Pandas
- NumPy
- Matplotlib

## Key Results
| Metric / Segment | Churn Rate |
|---|---:|
| Overall | 26.5% |
| 0–12 months tenure | 47.4% |
| Electronic check | 45.3% |
| Month-to-month contract | 42.7% |
| Fiber optic service | 41.9% |
| 25–48 months tenure | 20.4% |
| One-year contract | 11.3% |
| Two-year contract | 2.8% |

## Data Cleaning & Feature Engineering
- Converted `TotalCharges` to numeric.
- Identified **11 blank TotalCharges values** and handled them as missing values rather than inventing values.
- Created tenure cohorts for retention analysis.
- Converted churn labels into a numeric indicator for grouped churn-rate calculations.

## Business Insights
- Churn was substantially higher among customers on month-to-month contracts than among customers on longer contracts.
- Customers in their first 12 months showed the highest observed tenure-cohort churn.
- Fiber-optic and electronic-check cohorts also showed elevated churn in this dataset.
- These are **associations, not causal effects**; the analysis does not claim that any single attribute causes churn.

## Retention Hypotheses
- Prioritize early-tenure onboarding and engagement.
- Test incentives for customers to move from month-to-month to longer contracts.
- Investigate service experience within the fiber-optic cohort.
- Review payment-friction and customer characteristics associated with electronic-check usage.

## Repository Structure
- `src/customer_churn_analysis.py` — reproducible Python/Pandas analysis
- `README.md` — methodology, results and business interpretation

## Portfolio Note
This is a self-initiated analytics portfolio project using the public IBM Telco Customer Churn dataset.
