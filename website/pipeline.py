import pandas as pd
import numpy as np

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

def public_pipeline(df):
    df["username_len"] = df["username"].apply(len)
    df["username_num_count"] = df["username"].apply(num_count)
    df["username_ratio"] = df["username_num_count"] / df["username_len"]
    df["biography"] = df["biography"].replace(np.nan, "")
    df["biography_len"] = df["biography"].apply(len)
    df['isBio'] = df['biography_len'].apply(lambda x: 1 if x > 0 else 0)
    df = df.rename(columns={'followsCount': 'followingCount', 'private': 'isPrivate', 'verified': 'isVerified'})
    df['latestPosts'] = df['latestPosts'].apply(lambda x: [] if isinstance(x, float) and np.isnan(x) else x)
    df["latest_media_comments"] = df["latestPosts"].apply(lambda x: x[0]["commentsCount"] if x != [] else 0)
    df["latest_media_likes"] = df["latestPosts"].apply(lambda x: x[0]["likesCount"] if x != [] else 0)
    df["isLatestPost"] = np.ones(df.shape[0])

    for i, j in zip(df["latestPosts"], range(df.shape[0])):
        if i == []:
            df.loc[j, "isLatestPost"] = 0

    df["isLatestPost"] = np.ones(df.shape[0])

    for i, j in zip(df["latest_media_comments"], range(df.shape[0])):
        if pd.isna(i):  # Use pd.isna() to check for nan values
            df.loc[j, "latest_media_comments"] = 0
            df.loc[j, "latest_media_likes"] = 0
            df.loc[j, "isLatestPost"] = 0

    columns_use = ["followersCount","followingCount","isPrivate","isVerified","postsCount","username_len","username_num_count","username_ratio","isBio", "latest_media_comments", "latest_media_likes", "isLatestPost"]
    df = df[columns_use]
    df = df.replace(np.nan, 0)
    return df

def private_pipeline(df):
    df["username_len"] = df["username"].apply(len)
    df["username_num_count"] = df["username"].apply(num_count)

    df["username_ratio"] = df["username_num_count"] / df["username_len"]

    df["biography"] = df["biography"].replace(np.nan, "")
    df["biography_len"] = df["biography"].apply(len)

    df['isBio'] = df['biography_len'].apply(lambda x: 1 if x > 0 else 0)

    df = df.rename(columns={'followsCount': 'followingCount', 'private': 'isPrivate', 'verified': 'isVerified'})
    df.columns

    columns_use = ["followersCount","followingCount","isPrivate","isVerified","postsCount","username_len","username_num_count","username_ratio","isBio"]
    df = df[columns_use]

    df = df.replace(np.nan, 0)
    return df
