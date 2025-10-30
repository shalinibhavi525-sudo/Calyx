# Calyx
The Augmented Intelligence Harvest Layer
> *"The human mind is a garden. CALYX is the soil that learns what you plant."*
Calyx is a local prototype for a personal **Augmented Intelligence** system that learns from your reflections, notes, and thoughts. 
It maps your ideas into an **Insight Graph** — revealing connections you didn’t know existed.
Built with simplicity and modular clarity in mind, Calyx demonstrates how locally hosted AI tools can help individuals *think with their own memory* instead of replacing it.
---
## ■ Features
- ■ Learns from your text inputs or uploads (notes, reflections)
- ■ Builds semantic connections and saves them as an evolving memory
- ■ Smart retrieval: search your knowledge by concept, mood, or intent
- ■ Reflection Engine: generates insights about recurring ideas
- ■ Clean Streamlit dashboard for intuitive exploration
---
## ■ Architecture
```
User → Intent Parser → Memory Engine → Insight Graph → Reflections → UI
```
**Modules**
- `intent_parser.py`: detects meaning and emotional tone of text 
- `memory_engine.py`: stores, cleans, and expands user memories 
- `insight_graph.py`: creates concept links and similarity maps 
**Data**
- `user_knowledge.json`: stores all learned text 
- `insights_store.json`: stores generated reflections 
---
## ■■ Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
---
## ■ Future Expansion
Integrate embeddings (OpenAI or SentenceTransformer)
- Add visualization using D3.js or PyVis
- Connect to a local vector DB (FAISS / Chroma)
- Build context-aware recall and narrative synthesis
