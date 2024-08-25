from openai import OpeanAI

#pip install openai
#if you saved the key under a different environment variable name, you can do someting like:
client = OpeanAI(
    api_key = "USE YOUR OWN API KEY"
)

completion = client.chat.comletion.create(
 model = "gpt-3.5-turbo"
 messages=[
     {"role":"system","content":"you are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
     {"role":"user":"content":"what iis coding"}
 ]
)
print(completion.choices[0].message.content)






