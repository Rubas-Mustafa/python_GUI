import openai

openai.api_key = "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"
openai.api_key = "OPENAI_API_KEY"

def Sentiment_analysis(text):
    messages = [
        {"role" : "system", "content" : """You are trained to analyze and detect the sentiment of given text
        if you are unsure of an answer, you can say "not sure" and recommend users to review manually."""},

        {"role" : "user", "content" : f"""Analyze the following text and determine if the sentiment is : positive or negative.
         Return answer in single word as either positive or negative: {text}"""}
    ]

    response = openai.ChatCompletion.create(
    model ="gpt-3.5-turbo",
    messages = messages, 
    max_tokens = 1,
    n = 1,
    temperature = 0.5)

    response_text = response.choices[0].message.content.strip().lower()

    return response_text

input = "I love Pakistan"
response = Sentiment_analysis(input)
print(input, ': The Sentiment is', response)