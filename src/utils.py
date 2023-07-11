import fileinput

def read_file(file_path:str):
    with open(file_path, 'r') as file:
        content = file.read()
    return content