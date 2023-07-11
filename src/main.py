import os
from os.path import join
from utils import get_completion, read_file, save_text_file
import argparse

delimiter = "####"
crt_file_path = os.path.dirname(os.path.abspath(__file__))


def create_cover_letter(model:str, out_format:str):
    
    print("Preparing coverletter...")
    CV = read_file(join(crt_file_path,"CV.txt")) # Read CV
    Proposal = read_file(join(crt_file_path,"Proposal.txt")) # Read Work Proposal
    response = get_completion(f"Is the text between {delimiter} a Curriculum Vitae?. \n {delimiter}{Proposal}{delimiter} \
                            answer with Y for an affirmative answer and N for a negative one. Explain why in one sentence", model)

    if not os.path.exists(join(crt_file_path,'output')): os.makedirs(join(crt_file_path,'output'))
    file_name = join(crt_file_path,'output','coverletter.'+out_format)
    save_text_file(text=response,
                   name=file_name,
                   format = out_format)

    print(f"[SUCESS!] Coverletter succesfully saved in {file_name}")


if __name__ == "__main__":
    print('================================================================')
    print('                     MyCoverLetterAssistant                     ')
    print('               Authors: Deivid Botina & Diana Marin             ') 
    print('================================================================')   

    parser = argparse.ArgumentParser()
    parser.add_argument('--model','-m',type=str,choices=['gpt-3.5-turbo','gpt-4'],default='gpt-3.5-turbo',required=False,help='LLM name')
    parser.add_argument('--out_format','-of',type=str,choices=['txt'],default='txt',required=False,help='Output file format')    
    args = parser.parse_args()    
    for arg in vars(args):
        print(f'{arg} : {getattr(args, arg)}')
    print('================================================================') 
    create_cover_letter(model=args.model,
                        out_format=args.out_format)