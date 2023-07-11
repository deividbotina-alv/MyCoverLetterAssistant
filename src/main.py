import os
import openai
from dotenv import load_dotenv, find_dotenv
from utils import read_file

crt_file_path = os.path.dirname(os.path.abspath(__file__))
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

def get_completion(prompt, model="gpt-3.5-turbo"): #"gpt-3.5-turbo"
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

delimiter = "####"

# Read CV
CV = read_file(os.path.join(crt_file_path,"CV.txt"))
print("###### CV #######")
print(" ")
print(CV)

response = get_completion(f"Is the text between {delimiter} a Curriculum Vitae?. \n {delimiter}{CV}{delimiter} \
                          answer with Y for an affirmative answer and N for a negative one. Explain why in one sentence")

print(response)

# Read Work Proposal
Proposal = read_file(os.path.join(crt_file_path,"Proposal.txt"))
print("###### Proposal #######")
print(" ")
print(Proposal)

response = get_completion(f"Is the text between {delimiter} a Curriculum Vitae?. \n {delimiter}{CV}{delimiter} \
                          answer with Y for an affirmative answer and N for a negative one. Explain why in one sentence")

print(response)

