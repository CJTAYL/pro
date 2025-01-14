# Delinquency Report 

The delinquency report is used by the Chief Lending Officer and Cheif Risk Officer to review the financial health of the institution. The report summarizes the data with the modified delinquency ratio (MDR), which is calculated with the following formula: 

$$ \frac{\Sigma \text{ current principal balance of delinquent loans}}{\Sigma \text{ current principal balance of all loans}} $$

## Examples of MDR

Consider the following portfolio:
- Loan A (credit card) - current principal balance = $100
- Loan B (auto loan) - current principal balance = $200
- Loan C (credit card) - current principal balance = $300

If Loan A was delinquent, the total MDR would be 0.17.

$$ \frac{100}{100 + 200 + 300} = \frac{100}{600} = 0.17 $$

When calculating product specific MDRs, the totals for a specific product are used. For instance, if Loan A is delinquent, the MDR for credit cards would be 0.25. 

$$ \frac{100}{100 + 300} = \frac{100}{400} = 0.25 $$

## Inclusion Criteria and Data Collection

To be included in the MDR calculation, a loan should not be charged off. 

When collecting data for the calculations, month end information should be used. To ensure the data is from the month's end, set the process date equal to the last calendar day of the month (this can be accomplished with a WHERE clause in the SQL query). 

## Visual Representations of the Data

Visual representations of the data should be provided to the Chief Lending Officer and the Chief Risk Officer in an Excel workbook via email on the 10th of every month. The data should contain line graphs showing the 2+ and 3+ Months MDR for the past 25 months. 

The data path for 2+ Months delinquent loans should be orange and the data path for 3+ Months delinquent should be blue. 

Each of the following categories should have a tab with its own line graph:
- Total Loans
- Credit Cards
- Auto Loans
- Mortgage / Consumer Loans

The y-axis of all graphs should have a minimum value of 0 to avoid producing data that appear to have increased variability. To avoid producing data that appear to have decreased variability, the maximum value of the y-axis should be approximately 5% larger than the largest data point. 

## Important Notes 

Although Valera is considered the "Source of Record" for credit card information, its calculations of the MDR are inaccurate because it includes charged off loans.
