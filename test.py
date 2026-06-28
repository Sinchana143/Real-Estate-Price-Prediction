import pandas as pd

data = pd.read_csv(
    r'C:\Users\HP\Desktop\real_estate_project\dataset.csv',
    sep=';',
    encoding='latin1'
)

print(data.columns)
print(data.head())
