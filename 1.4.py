import pandas as pd
from sklearn.impute import SimpleImputer

# Sample integrated dataset
data = {
    'customer_id': [1, 2, 3, 4, 5],
    'product_id': [100, 101, 102, 103, 104],
    'order_date': ['2023-05-15', '2023-06-20', '2023-07-10', None, '2023-09-18'],
    'product_name': ['Product A', 'Product B', None, 'Product D', 'Product E'],
    'unit_price': [10.99, None, 15.99, 25.99, 30.49]
}
df = pd.DataFrame(data)

def handle_missing_values(df, strategy='mean'):
    try:
        imputer = SimpleImputer(strategy=strategy)
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
        return df_imputed
    except Exception as e:
        print("Error occurred during missing value handling:", e)
        return None

# Example usage:
cleaned_df = handle_missing_values(df, strategy='mean')
print("Cleaned DataFrame:")
print(cleaned_df)
