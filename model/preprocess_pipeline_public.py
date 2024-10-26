import pandas as pd
import numpy as np

df1 = pd.read_json("../datasets/scrapped/unlabelled/unlabelled1.json")
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

df1['latestPosts'] = df1['latestPosts'].apply(lambda x: [] if isinstance(x, float) and np.isnan(x) else x)
df1["latest_media_comments"] = df1["latestPosts"].apply(lambda x: x[0]["commentsCount"] if x != [] else 0)
df1["latest_media_likes"] = df1["latestPosts"].apply(lambda x: x[0]["likesCount"] if x != [] else 0)
df1["isLatestPost"] = np.ones(df1.shape[0])

for i, j in zip(df1["latestPosts"], range(df1.shape[0])):
    if i == []:
        df1.loc[j, "isLatestPost"] = 0

df1["isLatestPost"] = np.ones(df1.shape[0])

for i, j in zip(df1["latest_media_comments"], range(df1.shape[0])):
    if pd.isna(i):  # Use pd.isna() to check for NaN values
        df1.loc[j, "latest_media_comments"] = 0
        df1.loc[j, "latest_media_likes"] = 0
        df1.loc[j, "isLatestPost"] = 0

columns_use = ["followersCount","followingCount","isPrivate","isVerified","postsCount","username_len","username_num_count","username_ratio","isBio", "latest_media_comments", "latest_media_likes", "isLatestPost"]
df1 = df1[columns_use]
df1 = df1.replace(np.NaN, 0)