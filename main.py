# Create your Own ChatGPT using Python
# pip install openai 
# then import openai
import openai
#Setup openAI API client
openai.api_key="Weblaunch"
#this loop will let us ask questions continuosly
#and behave like ChatGPT
while True:
    # set up the model and prompt
    model_engine="weblaunch-api"
    prompt= input("Hello how may I help You:")
    if 'exit' in prompt or 'quit' in prompt:
        break
    # Generate a Response
    completion= openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1000,
        n=1, stop=None,
        temperature=0.5)
    # exctracting useful part of response
    response= completion.choices[0].text
    # printing response
    print(response)   