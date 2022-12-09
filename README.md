# open AI로 만든 Image 생성기
[DALL-E 링크](https://labs.openai.com/)
## 설명
---
이 레포지토리는 openAI사에서 제공하는 DALL-E라는 이미지 생성기를 모듈로 받아 파이썬으로 구현해놓은 코드를 올린 것이다.

대략적인 사용 방법은 다음과 같다.
1. 키워드를 넣는다.
2. 이미지 생성 개수를 설정한다.
3. url 주소에서 이미지를 사용한다.
4. Done!
## 사용법
---
#### 먼저 openai 모듈을 pip으로 설치한다.
```
pip install openai
```

```python
openai.api_key = "본인 api key"
```
- openAI 사이트에서 view api key를 통해 본인의 고유 api key를 코드 내에서 설정한다.

```python
variation_num = 2
```
- variation_num에 생성 개수를 설정한다.

```python
response = openai.Image.create(

prompt="sans and papyrus from undertale", #생성하고 싶은 키워드 or 문장

n=variation_num, #바리에이션 생성 개수

size="512x512" #256x256, 512x512, or 1024x1024

)
```
- prompt에 생성할 이미지의 텍스트를 입력한다. ex) "sans and papyrus from undertale"
- size에서 생성할 이미지의 크기를 설정한다. (256x256, 512x512, 1024x1024 셋 중 하나)

이후 image.py를 실행한다.
