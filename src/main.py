import os
from utils import get_completion, read_file
import argparse

delimiter = "####"
crt_file_path = os.path.dirname(os.path.abspath(__file__))


def main(model:str):
    # Read CV
    print("Reading CV file...")
    CV = read_file(os.path.join(crt_file_path,"CV.txt"))
    response = get_completion(f"Is the text between {delimiter} a Curriculum Vitae?. \n {delimiter}{CV}{delimiter} \
                            answer with Y for an affirmative answer and N for a negative one. Explain why in one sentence", model)
    print(response)

    # Read Work Proposal
    print("Reading Proposal file...")
    Proposal = read_file(os.path.join(crt_file_path,"Proposal.txt"))
    response = get_completion(f"Is the text between {delimiter} a Curriculum Vitae?. \n {delimiter}{Proposal}{delimiter} \
                            answer with Y for an affirmative answer and N for a negative one. Explain why in one sentence", model)
    print(response)


if __name__ == "__main__":
    print('================================================================')
    print('                     MyCoverLetterAssistant                     ')
    print('               Authors: Deivid Botina & Diana Marin             ') 
    print('================================================================')   

    parser = argparse.ArgumentParser()
    parser.add_argument('--model','-m',type=str,choices=['gpt-3.5-turbo','gpt-4'],default='gpt-3.5-turbo',required=False,help='LLM name')
    
    args = parser.parse_args()    
    for arg in vars(args):
        print(f'{arg} : {getattr(args, arg)}')
    print('================================================================') 
    main(model=args.model)