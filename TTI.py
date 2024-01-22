import base64
import requests
import os

url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

text_Prompt = input("Your prompt: ")
prompt_type = input("How you want it to look like? Separate your options by a comma: ")

body = {
  "steps": 40,
  "width": 1024,
  "height": 1024,
  "seed": 0,
  "cfg_scale": 5,
  "samples": 1,
  "text_prompts": [
    {
      "text": text_Prompt,
      "weight": 1
    },
    {
      "text": prompt_type,
      "weight": -1
    }
  ],
}

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": "sk-kxkyva9ncO1dvHONsC04zs4Grh2IRhVD11SrlN8m1CjbvBOV",
}

response = requests.post(
  url,
  headers=headers,
  json=body,
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

# make sure the out directory exists
if not os.path.exists("./output"):
    os.makedirs("./output")

for i, image in enumerate(data["artifacts"]):
    with open(f'./output/tti_{image["seed"]}.png', "wb") as f:
        f.write(base64.b64decode(image["base64"]))