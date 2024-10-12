from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    ans = blob.sentiment.polarity
    if ans>0:
        return "positive",ans
    elif ans==0:
        return "Neutral",ans
    return "Negative",abs(ans)

if __name__ == "__main__":
    user_ip = input("Enter text to analyze the seniment of the text : ")
    result,accuracy = analyze_sentiment(user_ip)
    print(f"The Sentiment of the given text is : {result}")
    print(f"The confidence of the text is : {accuracy*100}%")