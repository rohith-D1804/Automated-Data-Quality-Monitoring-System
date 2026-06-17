## Missing Value Checker

import pandas as pd
from validator import run_all_checks

df = pd.read_csv(r"D:\Data Analytics\Automated data monitoring system\data\sample_sale.csv")
results = run_all_checks(df)

print(results)


