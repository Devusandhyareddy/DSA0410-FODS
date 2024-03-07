import pandas as pd
data = pd.DataFrame({
    'customer_id': [1, 2, 3, None],
    'order_id': [101, 102, None, 104],
    'product_id': [201, 202, 203, 203],
    'product_name': ['Product A', 'Product B', 'Product C', 'Product C'],
    'price': [10.0, 20.0, 30.0, 30.0],
    'quantity': [1, 2, None, 4],
    'review_score': [5, 4, 5, None]
})
missing_values = data.isnull().sum().sum()
duplicates = data.duplicated().sum()
print("Data Quality Check:")
print("Number of missing values:", missing_values)
print("Number of duplicates:", duplicates)
