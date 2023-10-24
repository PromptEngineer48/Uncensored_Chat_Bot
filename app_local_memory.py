import openai

# openai.api_key="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"


openai.api_type = "open_ai"
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "Whatever"


messages = [{'role': 'system', 'content': 'you are a helpful assistant'}]


while True:
    user_input = input("Prompt: ")
    
    messages.append({'role': 'user', 'content': user_input})
    

    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=messages,
        temperature=0.7,
        max_tokens=-1
    )

    # print(response)
    print(response.choices[0].message.content)
    
    
    messages.append({'role': 'assistant', 'content': response.choices[0].message.content})





