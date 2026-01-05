from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
from pathlib import Path

INSIGHT_FILE = Path("data/insights_store.json")

def generate_insights(data):

    texts = [d["text"] for d in data]
    
    # Check if there are enough texts to generate insights
    if len(texts) < 2:
        return ["Not enough data yet for cross-insights. Add more thoughts!"]
    

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    

    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    

    avg_similarity = np.mean(similarity_matrix[np.triu_indices_from(similarity_matrix, 1)])
    
    top_terms = sorted(vectorizer.vocabulary_.keys())[:5]
    
    insights = [
        f"Your ideas often revolve around: {', '.join(top_terms)}.",
        f"Average conceptual similarity across your entries: {avg_similarity:.2f}",
        "You seem to revisit themes — your mind connects ideas naturally."
    ]
    
    INSIGHT_FILE.parent.mkdir(exist_ok=True)
    with open(INSIGHT_FILE, "w") as file:
        json.dump(insights, file, indent=2)
    
    return insights
