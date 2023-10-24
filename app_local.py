import openai

# openai.api_key="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"


openai.api_type = "open_ai"
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "Whatever"


response = openai.ChatCompletion.create(
    model='gpt-4',
    messages=[
        {'role': 'system', 'content': 'you are a helpful assistant'},
        {'role': 'user', 'content': 'What is the capital of France?'}
    ],
    temperature=0.5,
    max_tokens=1024
)

print(response)
print(response.choices[0].message.content)


