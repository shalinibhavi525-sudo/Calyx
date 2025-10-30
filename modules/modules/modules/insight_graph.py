from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
from pathlib import Path
INSIGHT_FILE = Path("data/insights_store.json")
def generate_insights(data):
 texts = [d["text"] for d in data]
 if len(texts) < 2:
 return ["Not enough data yet for cross-insights. Add more thoughts!"]
 vectorizer = TfidfVectorizer(stop_words='english')
 tfidf = vectorizer.fit_transform(texts)
 sim_matrix = cosine_similarity(tfidf, tfidf)
 avg_sim = np.mean(sim_matrix[np.triu_indices_from(sim_matrix, 1)])
 top_terms = sorted(vectorizer.vocabulary_.keys())[:5]
 insights = [
 f"Your ideas often revolve around: {', '.join(top_terms)}.",
 f"Average conceptual similarity across your entries: {avg_sim:.2f}",
 "You seem to revisit themes — your mind connects ideas naturally."
 ]
 INSIGHT_FILE.parent.mkdir(exist_ok=True)
 with open(INSIGHT_FILE, "w") as f:
 json.dump(insights, f, indent=2)
 return insights
