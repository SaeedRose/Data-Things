import pandas as pd

clms = pd.read_csv("file_name.csv")

# CODE_1
# به ارور زرد رنگ در زیر نام متغیر توجه نشود! کد درست کار میکند
# میتوان نام متغیر را به هر چیز دیگری غیر از ایکس هم تغییر داد

for i, col in enumerate(clms.columns, start=1):
    globals()[f"x{i}"] = col
# print(x2)
# -----------------------------------------------------------------

# CODE_2
# در صورتی که میخواهید با دادن نام ستون، نام متغیر اختصاص داده شده را پیدا کنید از این کد استفاده کنید
column_to_var = {}
for i, col in enumerate(clms.columns, start=1):
    var_name = f"x{i}"
    globals()[var_name] = col
    column_to_var[col] = var_name
    
# print(column_to_var["your column name"])    
    
