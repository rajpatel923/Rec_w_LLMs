# Movie Recommendation System with LLM and Traditional Algorithms Integration

This project is a movie recommendation system that integrates large language models (LLMs) with traditional algorithms, such as collaborative and content-based filtering, to provide contextually relevant, personalized recommendations. By combining the strengths of LLMs with conventional recommendation techniques, the system aims to deliver highly customizable suggestions based on user preferences and mood.

## Project Structure

```plaintext
movie-recommendation-system/
├── data/
│   ├── raw/                           # Raw dataset files
│   ├── processed/                     # Preprocessed and feature-engineered data
│   ├── embeddings/                    # Movie and user embeddings
│   ├── recommendations/               # Output recommendations for users
│   └── external/                      # Additional resources like IMDb API or tag data
│
├── src/
│   ├── data_preprocessing/            # Data cleaning and feature engineering scripts
│   ├── model/                         # Models for collaborative, content-based, and LLM integration
│   ├── recommendation_engine/         # Recommendation pipeline and similarity search
│   ├── app/                           # Backend API and frontend components
│   └── utils/                         # Helper functions and configurations
│
├── notebooks/                          # Jupyter notebooks for EDA and model experiments
├── tests/                              # Unit tests for different modules
├── requirements.txt                    # Dependencies
├── README.md                           # Project overview and setup instructions
└── run.py                              # Main script to start the recommendation system
# Project Workflow

## Step 1: Data Preprocessing and Feature Engineering
- **Load Raw Data**: Scripts in `src/data_preprocessing/` load and clean data files, including `ratings.json`, `metadata.json`, `reviews.json`, `tags.json`, and `tag_count.json`.
- **Process Ratings**: Create a user-item interaction matrix and normalize ratings.
- **Generate Tag Features**: Calculate tag frequencies and aggregate Tag Genome relevance scores to build tag-based movie profiles.
- **Sentiment Analysis on Reviews**: Run sentiment analysis on `reviews.json` to capture emotional tones for each movie.
- **Generate Embeddings**: Use models like BERT or Sentence Transformers to create embeddings for movies based on metadata, tags, and sentiment scores.

## Step 2: Traditional Model Setup
- **Collaborative Filtering** (`src/model/collaborative_filtering.py`): Use matrix factorization techniques like SVD or ALS to train on the user-item matrix.
- **Content-Based Filtering** (`src/model/content_based_filtering.py`): Build content-based profiles using movie metadata and Tag Genome relevance scores.
- **Hybrid Model** (`src/model/hybrid_model.py`): Combine collaborative and content-based filtering for initial recommendations.

## Step 3: Integrate LLM for Contextual Understanding
- **LLM Setup** (`src/model/llm_integration.py`): Use an LLM (e.g., GPT-4, T5) to interpret user queries and filter recommendations based on identified themes and moods.
- **Contextual Filtering**: Apply LLM-based filtering to prioritize movies in the hybrid recommendation list based on user context.
- **Ranking and Explanation Generation**: Use the LLM to rank final recommendations and generate human-like explanations.

## Step 4: Embedding-Based Similarity Search
- **Embedding Similarity Search** (`src/recommendation_engine/similarity_search.py`): Use FAISS for fast similarity search with embeddings.
- **Personalized Embedding Search**: Generate personalized recommendations based on user-specific embeddings.

## Step 5: Sentiment-Based Recommendation Refinement
- **Filter by Sentiment** (`src/model/sentiment_analysis.py`): Filter or rank movies to match the user's requested tone (e.g., "uplifting").
- **Combine with Tag-Based Filtering**: Use tag relevance and sentiment scores to enhance personalization.

## Step 6: Build the Recommendation Pipeline
- **End-to-End Pipeline** (`src/recommendation_engine/recommendation_pipeline.py`): Combine traditional filtering, LLM-based ranking, and embedding search into a unified recommendation engine.
- **Testing and Evaluation**: Evaluate model performance with cross-validation and metrics like precision, recall, and NDCG.

## Step 7: API and Frontend Setup
- **Backend API** (`src/app/api.py`): Implement an API to process recommendation requests and handle user feedback.
- **User Interface** (`src/app/user_interface/`): Create a frontend where users can input preferences and receive recommendations with LLM-generated explanations.
- **Dashboard** (`src/app/dashboard.py`): Monitor model performance and user interactions for further improvements.

## Step 8: Continuous Evaluation and Feedback Integration
- **User Feedback Loop**: Collect user feedback to refine future recommendations.
- **A/B Testing**: Use A/B testing to evaluate different recommendation strategies and optimize the pipeline.

## Getting Started

### Prerequisites
- Python 3.8+
- Install dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Running the System
1. **Data Preprocessing**: Run `src/data_preprocessing/preprocess.py` to prepare and process raw data files.
2. **Model Training**: Train models by running `src/model` scripts (e.g., collaborative filtering, content-based filtering).
3. **Start the Recommendation Engine**:
    ```bash
    python run.py
    ```
4. **API and Frontend**: Launch the API (`src/app/api.py`) and the user interface.

### Testing
Run tests to ensure each module works as expected:
```bash
pytest tests/
