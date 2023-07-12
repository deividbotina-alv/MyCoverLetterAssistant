import os
import sys
import openai
from dotenv import load_dotenv, find_dotenv
import enum

_ = load_dotenv(find_dotenv()) # read local .env file

try:
    openai.api_key  = os.environ['OPENAI_API_KEY']
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    print("Do you have the .env file with your OPENAI_API_KEY?")
    sys.exit()

class languages(enum.Enum):
    english = enum.auto()
    spanish = enum.auto()
    french = enum.auto()
    german = enum.auto()
    portuguese = enum.auto()
    italian = enum.auto()

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

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"]

def save_text_file(text:str, name:str, format:str='txt'):
    if format in ["txt"]:
        with open(name, 'w') as f:
            f.write(text)
    else:
        print("[save_text_file] ERROR: Format not valid")