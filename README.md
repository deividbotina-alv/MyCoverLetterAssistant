# MyCoverLetterAssistant

<p align="center">
    <a href="VERSION" alt="version">
        <img src="https://img.shields.io/badge/version-0.0.0-lightgray" /></a>    
    <a href="LICENSE" alt="License">
        <img src="https://img.shields.io/badge/license-GPL3-blue" /></a>
    <a href="PLATFORM" alt="Platform">
        <img src="https://img.shields.io/badge/platform-linux--64-lightgrey" /></a>  
    <a href="CONTRIBUTORS" alt="Contributors">
        <img src="https://img.shields.io/badge/contributors-2-brightgreen" /></a>                
</p>

MyCoverLetterAssistant is a project that allows users to generate personalized cover letters based on the content of two plain text files. By providing a work proposal file and a curriculum vitae file, users can leverage the power of ChatGPT to automatically generate professional and tailored cover letters that align with their profiles and desired job positions.

<img src="media/icon.jpeg" alt="easy-rppg Logo" width="384" height="384">

# Authors

- Deivid Johan Botina Monsalve
- Diana Marcela Marín Castrillón

# Installation

<details>
<summary> Specifications (click to expand)</summary>

The MyCoverLetterAssistant project has been tested on a Lenovo ThinkPad P16s Gen 1 with the following specifications:
- Operating System: Ubuntu 22.04.2 LTS
- Python version: 3.10.6

</details>


<details>
<summary> Setting up a Virtual Environment (click to expand)</summary>

***Make sure you have downloaded the repository and you are in it.***

To utilize the MyCoverLetterAssistant, it is highly recommended to create a virtual environment. You have two options to set up the virtual environment: either from scratch or by using the provided requirements.txt file. Follow the instructions below to proceed with your preferred method:


<details>
<summary>Installation from scratch (click to expand)</summary>

- Install pip

```bash
$ sudo apt-get install python3-pip
```
  
- Install the virtualenv package

```bash
$ sudo apt-get install virtualenv
```

- Create a virtual environment with a desired name, for example "venv".

```bash
$ virtualenv venv
```

- Activate the virtual environment you just created.

```bash
$ source venv/bin/activate
```

- Check your Python version

```bash
$venv$ python --version
```

- Install the openai library

```bash
$venv$ pip install openai==0.27.8
```

- Install the dotenv library

```bash
$venv$ pip install python-dotenv
```

- Install the docx library

```bash
$venv$ pip install --upgrade python-docx
```
</details>

<details>
<summary>Installation from requirements.txt file (click to expand)</summary>
  
- Install pip

```bash
$ sudo apt-get install python3-pip
```
  
- Install the virtualenv package

```bash
$ sudo apt-get install virtualenv
```

- Create a virtual environment with a desired name, for example "venv".

```bash
$ virtualenv venv
```

- Activate the virtual environment you just created.

```bash
$ source venv/bin/activate
```

- Check your Python version

```bash
$venv$ python --version
```

- Use pip and specify your requirements.txt file path

```bash
$venv$ pip install -r requirements.txt
```

</details>

</details>


</details>

<details>
<summary> Docker</summary>

In process...

</details>

# How to Use

Before using the MyCoverLetterAssistant, you need to set up the necessary API key from OpenAI. Follow the steps below to obtain your `OPENAI_API_KEY`:

1. Visit the [OpenAI website](https://openai.com) and create an account if you don't have one.
2. Navigate to the API section and generate an API key.
3. Copy the generated API key.

Next, create a file called `.env` in the root folder of this repository. Open the `.env` file and paste your `OPENAI_API_KEY` into it. Save the file.

Make sure to keep your API key confidential and do not share it publicly.

**Warning: Using the OpenAI models for generating cover letters may incur costs based on your usage. Please consider the pricing and terms of use of the OpenAI API to understand the potential charges you may incur.**

To generate a cover letter using the MyCoverLetterAssistant, you can run the `main.py` script with the following arguments:

|    Argument           | Short Flag | Type   | Description                                           | Default           | Required |
| :------------------- | :---------- | :------ | :----------------------------------------------------- | :---------------- | :-------- |
| `--path_cv_file`     | `-pcf`     | str    | Path to the file containing the CV                          | `CV.txt`          | False     |
| `--path_proposal_file` | `-ppf`  | str    | Path to the file containing the work proposal               | `Proposal.txt`    | False     |
| `--out_path`         | `-op`      | str    | Path where the cover letter will be saved             | Current directory | False     |
| `--out_format`       | `-of`      | str    | Output file format. Options: `txt`, `docx`            | `txt`             | False     |
| `--out_language`     | `-ol`      | str    | Output language. Options: `ENGLISH`, `SPANISH`, etc.  | `ENGLISH`         | False     |
| `--model`            | `-m`       | str    | LLM name. Options: `gpt-3.5-turbo`, `gpt-4`           | `gpt-3.5-turbo`   | False     |
| `--temperature`      | `-t`       | float  | Temperature for text generation                       | `0.0`             | False     |
| `--max_tokens`       | `-mt`      | int    | Maximum number of tokens to generate                  | `500`             | False     |

To generate a cover letter, run the following command:

```bash
$ python main.py --path_cv_file <path_to_cv_file> --path_proposal_file <path_to_proposal_file> --out_path <output_directory>
```

The generated cover letter will be saved in the specified --out_path directory with the default format (txt) and language (ENGLISH).

You can customize the behavior by providing values for the desired arguments. For example, to generate a cover letter in french with the docx format and with a maximum of 1000 tokens, use the following command:

```
$ python main.py --path_cv_file <path_to_cv_file> --path_proposal_file <path_to_proposal_file> --out_path <output_directory> --out_format docx --max_tokens 1000 --out_language FRENCH
```

Supported languages include: SPANISH, ENGLISH, FRENCH, GERMAN, PORTUGUESE, and ITALIAN.

***MyCoverLetterAssistant is for didactic purposes only, and commercial use is not allowed.***
