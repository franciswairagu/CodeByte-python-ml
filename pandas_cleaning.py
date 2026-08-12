# =============================
# Question
# =============================

"""
You are provided with a csv sales_data_missing.csv containing detailed sales information
Replace missing Promotion_id column with "No Promotion".
Calculate the total sales for the specific product_id in a given month.
Add a column each month's total sales to the dataset.
There are only two months present in the data; order these columns in ascending order by month number.
If there were no sales, fill the column with 0.0.
Ensure that the dataset contains only order_id, product_id, promotion_id and the monthly_total_sale columns.
Return the cleaned dataset as Numpy array.
"""


import io
import pandas as pd

data = """order_id,product_id,promotion_id,currency,order_value,order_date,origin,order_value_column
1001,P101,PROMO_A,USD,150.50,2024-01-05,Web,150.50
1002,P102,,USD,80.00,2024-01-08,App,80.00
1003,P101,PROMO_B,USD,200.00,2024-01-12,Web,200.00
1004,P103,,USD,45.25,2024-01-15,Store,45.25
1005,P102,PROMO_A,USD,120.00,2024-01-18,App,120.00
1006,P101,,USD,100.00,2024-01-22,Web,100.00
1007,P104,PROMO_C,USD,310.00,2024-01-25,Store,310.00
1008,P103,,USD,60.00,2024-01-28,App,60.00
1009,P102,PROMO_B,USD,95.00,2024-01-30,Web,95.00
1010,P101,,USD,180.00,2024-01-31,Store,180.00
1011,P101,PROMO_A,USD,220.00,2024-02-02,Web,220.00
1012,P102,,USD,110.00,2024-02-05,App,110.00
1013,P103,PROMO_B,USD,50.00,2024-02-09,Store,50.00
1014,P101,,USD,130.00,2024-02-12,Web,130.00
1015,P104,PROMO_A,USD,290.00,2024-02-14,App,290.00
1016,P102,,USD,75.00,2024-02-17,Store,75.00
1017,P103,PROMO_C,USD,85.00,2024-02-20,Web,85.00
1018,P101,,USD,190.00,2024-02-22,App,190.00
1019,P102,PROMO_B,USD,140.00,2024-02-24,Store,140.00
1020,P104,,USD,330.00,2024-02-26,Web,330.00
1021,P101,PROMO_A,USD,160.00,2024-02-27,App,160.00
1022,P103,,USD,40.00,2024-02-28,Store,40.00
1023,P105,,USD,500.00,2024-01-10,Web,500.00
1024,P105,PROMO_A,USD,450.00,2024-02-15,App,450.00
1025,P102,,USD,105.00,2024-02-28,Web,105.00"""

df = pd.read_csv(io.StringIO(data))
df.to_csv("sales_data_missing.csv", index=False)

import pandas as pd

# Load the data 
df = pd.read_csv("sales_data_missing.csv")
print(df.info())

# Replace missing values in promotion_id with `No Promotion`
df["promotion_id"] = df["promotion_id"].fillna("No Promotion")

# convert order_date to datetime type and get month
df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.month

# Calculate the total sales for the specific product_id in a given month.
monthly_sales = (
    df.groupby(["product_id", "month"])["order_value_column"]
    .sum().unstack(fill_value=0.0)
)

# order month in ascending order and reset index of monthly sales for merging 
month_cols = sorted(monthly_sales.columns)
monthly_sales = monthly_sales.reset_index()

# merge monthly_sales with df 
merged_df = df.merge(monthly_sales, on="product_id", how="left")

# fill any nulls in the months after merging 
for month in month_cols:
    merged_df[month] = merged_df[month].fillna(0.0)

final_cols = ["order_id", "product_id", "promotion_id"] + month_cols

final_df = merged_df[final_cols]

final_df = final_df.to_numpy()

print(final_df[:5])