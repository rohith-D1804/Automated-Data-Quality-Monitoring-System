## Missing Value Checker

import pandas as pd
from validator import run_all_checks
from quality_score import (
    calculate_quality_score,
    get_quality_status
)

df = pd.read_csv(r"D:\Data Analytics\Automated data monitoring system\data\sample_sale.csv")
results = run_all_checks(df)
print(results)

score = calculate_quality_score(results,df)
status = get_quality_status(score)
print(results)

print()
print("Quality Score :", score)
print("Quality Status :", status)


