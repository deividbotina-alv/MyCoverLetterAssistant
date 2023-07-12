import os
import sys
import openai
from dotenv import load_dotenv, find_dotenv
import enum

_ = load_dotenv(find_dotenv())  # read local .env file

try:
    openai.api_key = os.environ["OPENAI_API_KEY"]
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    print("Do you have the .env file with your OPENAI_API_KEY?")
    sys.exit()


class Languages(enum.Enum):
    ENGLISH = enum.auto()
    SPANISH = enum.auto()
    FRENCH = enum.auto()
    GERMAN = enum.auto()
    PORTUGUESE = enum.auto()
    ITALIAN = enum.auto()


def read_file(file_path: str):
    """
    Read the content of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Content of the file.
    """
    with open(file_path, "r") as file:
        content = file.read()
    return content


def get_completion(prompt, model="gpt-3.5-turbo"):  # "gpt-3.5-turbo"
    """
    Get completion from the language model.

    Args:
        prompt (str): The input prompt.
        model (str): The language model to use.

    Returns:
        str: The generated completion.
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    """
    Get completion from messages using the language model.

    Args:
        messages (list): List of messages.
        model (str): The language model to use.
        temperature (float): Temperature parameter for text generation.
        max_tokens (int): Maximum number of tokens to generate.

    Returns:
        str: The generated completion.
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]

def save_text_file(text: str, name: str, format: str = "txt"):
    """
    Save text to a file. If the file already exists, append a number to the filename.

    Args:
        text (str): The text to save.
        name (str): The file name.
        format (str): The file format.
    """
    if format != "txt":
        print("[save_text_file] ERROR: Format not valid")
        return

    base_name, ext = os.path.splitext(name)
    counter = 1
    new_name = name

    while os.path.exists(new_name):
        new_name = f"{base_name}({counter}){ext}"
        counter += 1

    with open(new_name, "w") as file:
        file.write(text)

    print(f"[SUCCESS!] File saved as {new_name}")