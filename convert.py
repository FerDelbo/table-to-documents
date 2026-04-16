import pandas as pd

df_spider = pd.read_csv('./data/spider/ground_truth.csv')
df_claimdb = pd.read_csv('./data/claimdb/ground_truth_claims.csv')
df_wiki = pd.read_csv('./data/wiki/ground_truth_wiki.csv')

df_final = pd.concat([df_spider, df_claimdb, df_wiki], ignore_index=True)

df_final.to_csv('./data/ground_truth_total.csv', index=False)

# print(df_final.head())
# print(df_final.shape)

# filter_driver = df_final["Table"] == 'customers'
# final_table = df_final[filter_driver]
# print(final_table.head())
# print(final_table.shape) 
# df = pd.read_json('../ClaimDB/train.jsonl', lines=True)

# print(df.head())

# table_grounth = df[["claim_id", "db_name", "label", "claim"]]

# filter = table_grounth["label"] == 'CONTRADICTED'
# final_table = table_grounth[filter]

# final_table.to_csv('./data/claimdb/fact_contradited.csv', index=False)

