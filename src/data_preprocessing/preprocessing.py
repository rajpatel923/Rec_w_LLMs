import pandas as pd
import json
from pathlib import Path

data_path = Path('../../Dataset/raw')


def load_data():
    """Load raw data from JSON files and return DataFrames."""
    # Load data from files
    metadata_df = pd.read_json("/Users/rajpatel/Desktop/Langchain/Movie_Rec_System/Dateset/raw/metadata.json", lines=True)
    ratings_df = pd.read_json("/Users/rajpatel/Desktop/Langchain/Movie_Rec_System/Dateset/raw/ratings.json", lines=True)
    reviews_df = pd.read_json("/Users/rajpatel/Desktop/Langchain/Movie_Rec_System/Dateset/raw/reviews.json", lines=True)
    tags_df = pd.read_json("/Users/rajpatel/Desktop/Langchain/Movie_Rec_System/Dateset/raw/tags.json", lines=True)
    tag_count_df = pd.read_json("/Users/rajpatel/Desktop/Langchain/Movie_Rec_System/Dateset/raw/tag_count.json", lines=True)
    survery_answer = pd.read_json("/Users/rajpatel/Desktop/Langchain/Movie_Rec_System/Dateset/raw/survey_answers.json", lines=True)

    return metadata_df, ratings_df, reviews_df, tags_df, tag_count_df, survery_answer
