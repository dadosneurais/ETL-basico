import pandas as pd
import json

with open('users.json') as file:
    data = json.load(file)

df_users = pd.DataFrame(data)

df_ids = pd.read_csv('id.csv')

user_ids = df_ids['userId'].tolist()

df_filtered_users = df_users[df_users['id'].isin(user_ids)]

user_with_highest_limit = df_filtered_users.loc[df_filtered_users['account'].apply(lambda x: x['limit']).idxmax()]

print(df_users,"\n")

user_name = user_with_highest_limit['name']
print("Usuário com maior saldo de limite:", user_name)

print("Informações do usuário com maior saldo de limite:")
print(user_with_highest_limit)
