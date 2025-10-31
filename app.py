import streamlit as st
import json
from modules.intent_parser import analyze_intent
from modules.memory_engine import store_memory, load_memories
from modules.insight_graph import generate_insights

st.set_page_config(page_title="Calyx | Augmented Intelligence Layer", page_icon="■", layout="wide")
st.title("■ CALYX")
st.subheader("Augmented Intelligence Harvest Layer")
st.markdown("Type your thoughts, notes, or reflections below — Calyx will learn and connect your ideas.")

user_input = st.text_area("■ What’s on your mind today?", height=150)

if st.button("Add to Memory"):
    if user_input.strip():
        intent = analyze_intent(user_input)
        store_memory(user_input, intent)
        st.success("■ Memory stored successfully!")
    else:
        st.warning("Please write something first.")

if st.button("Generate Insights"):
    data = load_memories()
    if data:
        insights = generate_insights(data)
        st.markdown("### ■ Reflections")
        for ins in insights:
            st.write(f"- {ins}")
    else:
        st.warning("No memories found yet.")

st.markdown("### ■ Existing Memory Log")
data = load_memories()
if data:
    for item in data:
        st.markdown(f"• {item['text']} — *({item['intent']})*")
else:
    st.info("No memories stored yet.")

