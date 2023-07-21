from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='MyCoverLetterAssistant',
Summary='MyCoverLetterAssistant is a GitHub repository that provides a comprehensive solution for creating personalized cover letters and work proposals. Powered by ChatGPT, this project enables users to generate professional and tailored career documents based on their profiles and desired job positions.',
version='0.0.1',
author='Deivid & Diana',
author_email='deivid.johan.botina.monsalve@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
