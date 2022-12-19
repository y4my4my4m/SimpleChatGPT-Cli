import openai
import os
import getpass
import colorama

openai.api_key = os.environ['OPENAI_API_KEY']
username = getpass.getuser()
colorama.init()

def send_message(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

while True:
    prompt = input(colorama.Style.DIM +colorama.Fore.GREEN + username + ": " + colorama.Style.NORMAL)
    response = send_message(prompt)
    print(colorama.Fore.BLUE + "chatbot: " + colorama.Style.BRIGHT + colorama.Fore.BLUE + response + "\n")
