import pandas as pd
from validator import check_missing_values as mv

df = pd.read_csv(r"D:\Data Analytics\Automated data monitoring system\data\sample_sale.csv")
result = mv(df)

print(result)
