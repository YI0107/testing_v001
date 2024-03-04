import openai
openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Give me a color."}
  ]
)

print(completion.choices[0].message['content'])

