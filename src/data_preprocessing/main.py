import pandas as pd
from pathlib import Path

from preprocessing import load_data
from feature_engg import making_metadata_ready, making_tags_ready



OUTPUT_PATH = Path("data/processed")

def main():
    # Load data
    metadata_df, ratings_df, reviews_df, tags_df, tag_count_df, survery_answer = load_data()

   # getting data ready
    preprocess_metadata_Df = making_metadata_ready(metadata_df=metadata_df, ratings=ratings_df, reviews=reviews_df)
    preprocess_tags_Df = making_tags_ready(tags_df=tags_df, tag_count_df=tag_count_df, survery_answer=survery_answer )

    print(preprocess_metadata_Df.head(), preprocess_tags_Df.head())


if __name__ == "__main__":
    main()
