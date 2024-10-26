import pandas as pd
import numpy as np

df1 = pd.read_json("private_unsupervised.json")
df1["username_len"] = df1["username"].apply(len)

def num_count(str):
    count = 0
    for i in str:
        try:
            x = int(i)
        except:
            pass
        else:
            count += 1
    return count

df1["username_num_count"] = df1["username"].apply(num_count)

df1["username_ratio"] = df1["username_num_count"] / df1["username_len"]

df1["biography"] = df1["biography"].replace(np.NaN, "")
df1["biography_len"] = df1["biography"].apply(len)

df1['isBio'] = df1['biography_len'].apply(lambda x: 1 if x > 0 else 0)

df1 = df1.rename(columns={'followsCount': 'followingCount', 'private': 'isPrivate', 'verified': 'isVerified'})
df1.columns

columns_use = ["followersCount","followingCount","isPrivate","isVerified","postsCount","username_len","username_num_count","username_ratio","isBio"]
df1 = df1[columns_use]

df1 = df1.replace(np.NaN, 0)

df1.to_json('private_clean_unsupervised.json', orient='records')

