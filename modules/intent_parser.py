from textblob import TextBlob

def analyze_intent(text: str) -> str:
    """
    Analyzes the sentiment of the given text and categorizes it.

    Parameters:
    text (str): The text to analyze.

    Returns:
    str: A string describing the tone and category of the text.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    tone = "neutral"  # Default tone
    if polarity > 0.2:
        tone = "positive"
    elif polarity < -0.2:
        tone = "negative"

    category = "factual observation" if subjectivity <= 0.5 else "personal reflection"

    return f"{tone}, {category}"

