import os
from os.path import join
from utils import get_completion_from_messages, read_file, save_text_file, Languages, Text_format
import argparse

crt_file_path = os.path.dirname(os.path.abspath(__file__))


def get_cover_letter(curriculum: str, proposal: str, language: str, model: str, temperature: float, max_tokens: int):
    """
    Generate a cover letter based on the user's curriculum vitae and work proposal.

    Args:
        curriculum (str): User's curriculum vitae.
        proposal (str): Work proposal.
        language (str): Language for the cover letter.
        model (str): Language model to use.
        temperature (float): Temperature parameter for text generation.
        max_tokens (int): Maximum number of tokens to generate.

    Returns:
        str: Generated cover letter.
    """

    cv_delimiter = "####"
    pr_delimiter = "---"
    system_intro = f"""
    You are a cover letter assistant and you will be provided with a user Curriculum Vitae with a work proposal. \
    The user Curriculum Vitae query will be delimited with {cv_delimiter} characters. \
    The work proposal query will be delimited with {pr_delimiter} characters.\
    Understand the most important factors within the job proposal, then look for matches in the user's resume \
    that are relevant to the job proposal.
    """
    system_request = f"""
    Write a cover letter for the job proposal based on the user's resume.
    The cover letter should be written in {language}.
    End the letter specifying that this letter was written by an AI system based on ChatGPT.
    use up to {max_tokens} tokens.
    """

    messages = [
        {"role": "system", "content": system_intro},
        {"role": "user", "content": f"{cv_delimiter}{curriculum}{cv_delimiter}"},
        {"role": "user", "content": f"{pr_delimiter}{proposal}{pr_delimiter}"},
        {"role": "system", "content": system_request},
    ]
    return get_completion_from_messages(messages, model, temperature, max_tokens)


def create_cover_letter(cv_path:str, proposal_path:str, out_path:str,
                        out_format: str, language: str, model: str,
                        temperature: float, max_tokens: int):
    """
    Create a cover letter based on the provided parameters.

    Args:
        cv_path (str): Curriculum vitae file path
        proposal_path (str): Work proposal file path
        out_path (str): Path where the cover letter will be saved
        out_format (str): Output file format. TODO: pdf
        language (str): Output language.
        model (str): Language model to use.
        temperature (float): Temperature parameter for text generation.
        max_tokens (int): Maximum number of tokens to generate.
    """

    # Create cover letter
    print("Preparing cover letter...")
    curriculum = read_file(cv_path)  # Read CV
    proposal = read_file(proposal_path)  # Read Work Proposal
    response = get_cover_letter(curriculum, proposal, language, model, temperature, max_tokens)

    # Save cover letter
    if not os.path.exists(join(crt_file_path, "output")):
        os.makedirs(join(crt_file_path, "output"))
    file_name = join(out_path, f"coverletter.{out_format}")
    save_text_file(text=response, name=file_name, format=out_format)

if __name__ == "__main__":
    print("================================================================")
    print("                     MyCoverLetterAssistant                     ")
    print("               Authors: Deivid Botina & Diana Marin             ")
    print("================================================================")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path_cv_file",
        "-pcf",
        type=str,
        required=False,
        help="Path to the file containing the CV"
    )
    parser.add_argument(
        "--path_proposal_file",
        "-ppf",
        type=str,
        required=False,
        help="Path to the file containing the work proposal"
    )  
    parser.add_argument(
        "--out_path",
        "-op",
        type=str,
        required=False,
        help="Path where the coverletter will be saved"
    )        
    parser.add_argument(
        "--out_format",
        "-of",
        type=str,
        choices=[e.name for e in Text_format],
        default="txt",
        required=False,
        help="Output file format",
    )
    parser.add_argument(
        "--out_language",
        "-ol",
        type=str,
        choices=[e.name for e in Languages],
        default="ENGLISH",
        required=False,
        help="Output language",
    )
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        choices=["gpt-3.5-turbo", "gpt-4"],
        default="gpt-3.5-turbo",
        required=False,
        help="LLM name",
    )
    parser.add_argument(
        "--temperature",
        "-t",
        type=float,
        default=0.0,
        required=False,
        help="Temperature",
    )
    parser.add_argument(
        "--max_tokens",
        "-mt",
        type=int,
        default=500,
        required=False,
        help="Max tokens",
    )

    args = parser.parse_args()

    # Sanity checks
    args.temperature = 0 if args.temperature < 0 else args.temperature
    args.temperature = 1 if args.temperature > 1 else args.temperature
    args.max_tokens = 0 if args.max_tokens < 0 else args.max_tokens
    args.path_cv_file = join(crt_file_path, "CV.txt") if args.path_cv_file is None else args.path_cv_file
    args.path_proposal_file = join(crt_file_path, "Proposal.txt") if args.path_proposal_file is None else args.path_proposal_file
    args.out_path = crt_file_path if args.out_path is None else args.out_path

    for arg in vars(args):
        print(f"{arg}: {getattr(args, arg)}")
    print("================================================================")

    # Create cover letter
    create_cover_letter(
        cv_path = args.path_cv_file,
        proposal_path = args.path_proposal_file,
        out_path = args.out_path,
        out_format=args.out_format,
        language=args.out_language,
        model=args.model,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
    )
