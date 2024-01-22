import openai # pip install openai

def chat():
  openai.api_key = "YOUR_API_KEY"

  userinput = input("You: ")

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=userinput,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  print("ChatGPT: ", response)

def loop():
    if chat():
        chat()
        loop()
    else:
        chat()
        loop()


loop()
