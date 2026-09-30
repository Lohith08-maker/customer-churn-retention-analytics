# Customer Churn & Retention Analytics

## Key Insights
- Overall churn was **26.5%** across **7,043 customers**.
- Customers in their first **0–12 months** had the highest observed tenure-cohort churn at **47.4%**.
- **Electronic check (45.3%)**, **month-to-month contracts (42.7%)**, and **fiber optic service (41.9%)** were associated with elevated churn.
- Longer contracts showed substantially lower churn: **11.3%** for one-year and **2.8%** for two-year contracts.

## Project Overview
A Python/Pandas portfolio project analyzing customer churn patterns in the **IBM Telco Customer Churn** dataset. The project cleans the data, engineers tenure cohorts, measures churn across customer segments, and translates observed patterns into retention hypotheses.

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
- Review payment friction and customer characteristics associated with electronic-check usage.

## How to Run
1. Download the IBM Telco Customer Churn CSV and place it in your working directory.
2. Install the required Python packages: `pandas`, `numpy`, and `matplotlib`.
3. Open `src/customer_churn_analysis.py`.
4. Update the dataset file path in the script if necessary.
5. Run the script with Python to reproduce the cleaning, segmentation and churn-rate analysis.

## Repository Structure
- `src/customer_churn_analysis.py` — reproducible Python/Pandas analysis
- `README.md` — methodology, results and business interpretation

## Dashboard / Visual Preview
> A visual summary will be added here to make the key churn patterns easier to review at a glance.

## Portfolio Note
This is a self-initiated analytics portfolio project using the public IBM Telco Customer Churn dataset. Reported segment differences are descriptive associations, not causal claims.
