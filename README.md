# Sentiment Analysis using TextBlob
Overview :
This project is a simple Sentiment Analysis tool using Python's TextBlob library. 
It analyzes the sentiment of any given text and classifies it as Positive, Negative, or Neutral. 
Additionally, it provides a confidence score that reflects the intensity of the sentiment.

Features :
Classifies the sentiment as Positive, Negative, or Neutral.
Provides a confidence score (polarity) for the sentiment ranging from -1 to 1.
Simple command-line interface for text input.

How It Works :
The user inputs a sentence or block of text.
The program uses the TextBlob library to calculate the polarity of the text.
Based on the polarity score:
If polarity > 0, the text is classified as Positive.
If polarity == 0, the text is classified as Neutral.
If polarity < 0, the text is classified as Negative.
