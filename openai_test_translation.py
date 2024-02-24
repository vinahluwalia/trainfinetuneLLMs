from dotenv import load_dotenv
load_dotenv()

import os
# print(os.getcwd())
import openai

# Translation
english_text = "Hello, How are you?"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assitant."},
        {"role": "user", "content": f'Translate the following English text to French: "{english_text}"'},
    ],
)

print(response['choices'][0]['message']['content'])