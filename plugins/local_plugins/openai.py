import openai
import os

# Authenticate with the API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the prompt and parameters for the text generation
prompt = "Write a short story about a robot that gains consciousness"
model = "text-davinci-002"
temperature = 0.7
max_tokens = 100

# Generate the text
response = openai.Completion.create(
  engine=model,
  prompt=prompt,
  temperature=temperature,
  max_tokens=max_tokens
)

# Print the generated text
print(response.choices[0].text)
