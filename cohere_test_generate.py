from dotenv import load_dotenv
load_dotenv()
import cohere
import os

co = cohere.Client(os.environ["COHERE_API_KEY"])

response = co.generate(
    prompt='Please briefly explain to me how foundation models work using at most 100 words.',
    max_tokens=200,
)
print(response.generations[0].text)
print(response.generations)
