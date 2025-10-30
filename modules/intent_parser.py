from textblob import TextBlob
def analyze_intent(text):
 blob = TextBlob(text)
 polarity = blob.sentiment.polarity
 subjectivity = blob.sentiment.subjectivity
 if polarity > 0.2:
 tone = "positive"
 elif polarity < -0.2:
 tone = "negative"
 else:
 tone = "neutral"
 if subjectivity > 0.5:
 category = "personal reflection"
else:
category = "factual observation"
 return f"{tone}, {category}"
