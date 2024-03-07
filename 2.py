import pandas as pd
customer_demographics=pd.DataFrame({
           'customer_id':[1,2,3,4,5],
           'age':[35,28,42,30,45],
           'gender':['m','f','m','f','f'],
           'location':['chennai','hyd','new york','nellore','tirupathi'],
           })
user_activity_logs=pd.DataFrame({
                'customer_id':[1,2,3,4,5],
                'timestamp':['2024-02-01 08:00:00','2024-02-01 09:00:00','2024-02-01 10:00:00','2024-02-01 11:00:00','2024-02-01 12:00:00'],
                'page_viwes':[10,15,20,25,30],
                'interaction_duration':[120,150,180,200,230]
                })
customer_support=pd.DataFrame({
                   'customer_id':[1,2,3,4,5],
                   'support_tickets':[3,2,1,4,2],
                   'satisfaction_score':[4,3,5,2,4]
                   })
merged_data = pd.merge(customer_demographics, user_activity_logs, on='customer_id', how='left')
merged_data = pd.merge(merged_data, customer_support, on='customer_id', how='left')
print("Unified Dataset:")
print(merged_data)
