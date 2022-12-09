import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "본인 api key"  #openAI 홈페이지에서 본인의 api key 복붙하면 됨

variation_num = 6
response = openai.Image.create(
  prompt="neoskyclad", #생성하고 싶은 키워드 or 문장
  n=variation_num,  #바리에이션 생성 개수
  size="512x512"  #256x256, 512x512, or 1024x1024
)

# response = openai.Image.create_variation(
#   image=open("corgi_and_cat_paw.png", "rb"),
#   n=1,
#   size="1024x1024"
# )

for i in range(0, variation_num):
  image_url = response['data'][i]['url']
  print("=========================", i+1, "=========================")
  print(image_url)