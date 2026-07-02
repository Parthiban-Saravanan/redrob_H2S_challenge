import pandas as pd
import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer, util
from rank_bm25 import BM25Okapi
import os
import time
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

@st.cache_resource
def load_ai_model():
    """Optimized model caching to eliminate startup stalls."""
    return SentenceTransformer('all-MiniLM-L6-v2')

def run_elite_ranking_engine_stream(data_path, job_description):
    """
    Generator-based pipeline execution engine.
    Yields tuple: (current_stage_index, status_message, description, intermediate_data_or_None)
    """
    stages = [
        "Initializing AI search...",
        "Connecting to candidate database...",
        "Searching candidate profiles...",
        "Identifying relevant skills...",
        "Matching experience with job requirements...",
        "Ranking potential candidates...",
        "Calculating match scores...",
        "Preparing final candidate list..."
    ]

    # Stage 1: Init
    yield (1, stages[0], "Spinning up core contextual analytics kernels...", None)
    time.sleep(0.6)

    # Stage 2: Database Check
    yield (2, stages[1], "Opening read stream to localized JSONL file parameters...", None)
    time.sleep(0.6)
    if not os.path.exists(data_path):
        yield (8, "Error", f"Target file '{data_path}' could not be located.", None)
        return

    try:
        df = pd.read_json(data_path, lines=True)
    except Exception as e:
        yield (8, "Error", f"Failed parsing document stream: {str(e)}", None)
        return

    # Stage 3: Search
    yield (3, stages[2], f"Ingested {len(df)} candidate nodes into working memory space.", None)
    time.sleep(0.7)

    text_column = None
    for col in ['resume_text', 'resume', 'text', 'profile_text', 'experience', 'description']:
        if col in df.columns:
            text_column = col
            break
    if text_column is None:
        string_cols = df.select_dtypes(include=['object', 'string']).columns
        text_column = string_cols[0] if len(string_cols) > 0 else df.columns[0]

    df[text_column] = df[text_column].fillna('')
    corpus = df[text_column].astype(str).tolist()

    # Stage 4: Keywords
    yield (4, stages[3], "Running sparse lexical overlap distribution filters...", None)
    tokenized_corpus = [doc.lower().split(" ") for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)
    tokenized_query = job_description.lower().split(" ")
    keyword_scores = bm25.get_scores(tokenized_query)
    if np.max(keyword_scores) > 0:
        keyword_scores = keyword_scores / np.max(keyword_scores)
    time.sleep(0.8)

    # Stage 5: Dense Transformers
    yield (5, stages[4], "Computing multi-dimensional dense sentence embeddings...", None)
    model = load_ai_model()
    candidate_embeddings = model.encode(corpus, convert_to_tensor=True, show_progress_bar=False)
    job_embedding = model.encode(job_description, convert_to_tensor=True)
    semantic_scores = util.cos_sim(job_embedding, candidate_embeddings)[0].cpu().numpy()
    time.sleep(0.8)

    # Stage 6: Ranking Matrix
    yield (6, stages[5], "Calculating hybrid vector reciprocal combinations...", None)
    velocity_scores = []
    important_keywords = [word.strip(",.()\"'") for word in tokenized_query if len(word) > 4]

    for text in corpus:
        text_lower = text.lower()
        mention_count = sum(text_lower.count(kw) for kw in important_keywords)
        density_bonus = min(mention_count * 0.05, 0.2)
        
        first_segment = text_lower[:int(len(text_lower)*0.3)]
        recency_count = sum(first_segment.count(kw) for kw in important_keywords)
        recency_bonus = min(recency_count * 0.1, 0.15)
        
        velocity_scores.append(density_bonus + recency_bonus)
    time.sleep(0.6)

    # Stage 7: Composite Index Math
    yield (7, stages[6], "Blending scores (50% Semantic, 30% Stack, 20% Velocity)...", None)
    df['semantic_score'] = semantic_scores
    df['keyword_score'] = keyword_scores
    df['velocity_score'] = np.array(velocity_scores)
    df['final_match_score'] = (semantic_scores * 0.5) + (keyword_scores * 0.3) + (df['velocity_score'] * 0.2)
    df = df.sort_values(by='final_match_score', ascending=False).reset_index(drop=True)
    time.sleep(0.6)

    # Stage 8: Done
    yield (8, stages[7], "Finalizing beautiful presentation layers and analytics plots.", (df, text_column))