import pandas as pd
def clean_rating_column(df, column_name='rating', strategy='median'):
    try:
        df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
        df[column_name].fillna(df[column_name].median(), inplace=True)
        df = df[(df[column_name] >= 1) & (df[column_name] <= 5)]
        return df
    except Exception as e:
        print("Error occurred during data cleaning:", e)
        return None
data = {
    'customer_id': [11, 12, 13, 14, 15],
    'product_id': [100, 101, 102, 103, 104],
    'rating': [4, 5, 2, 'na', 3], 
    'review_text': ['Great product!', 'Excellent service!', 'Not satisfied.', 'Will not buy again.', 'Good quality.']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print()
cleaned_df = clean_rating_column(df, column_name='rating', strategy='median')
print("Cleaned DataFrame:")
print(cleaned_df)

