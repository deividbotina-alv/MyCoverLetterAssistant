import os
import sys
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

try:
    openai.api_key  = os.environ['OPENAI_API_KEY']
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    print("Do you have the .env file with your OPENAI_API_KEY?")
    sys.exit()

def read_file(file_path:str):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def get_completion(prompt, model="gpt-3.5-turbo"): #"gpt-3.5-turbo"
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]