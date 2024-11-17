import pandas as pd


def making_metadata_ready(metadata_df: pd.DataFrame, ratings:pd.DataFrame, reviews:pd.DataFrame) -> pd.DataFrame:
    metadata_df = metadata_df.drop(columns="dateAdded")
    metadata_df["starring"] = metadata_df["starring"].str.lower().str.split(",")
    metadata_df = metadata_df.merge(reviews, on="item_id", how="left")
    metadata_df = metadata_df.merge(ratings, on="item_id", how="left")
    return metadata_df

def making_tags_ready(tags_df: pd.DataFrame, tag_count_df: pd.DataFrame, survery_answer: pd.DataFrame) -> pd.DataFrame:
    tags = tags_df.rename(columns={"id": "tag_id"})
    tag_count_df = tag_count_df.merge(tags, on='tag_id', how='left')
    tag_count_df = tag_count_df.merge(survery_answer, on=['tag_id', 'item_id'], how='inner')
    return tag_count_df
