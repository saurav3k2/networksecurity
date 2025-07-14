from setuptools import setup, find_packages
from typing import List



def get_requirements() -> List[str]:
    """
    Reads a requirements file and returns a list of requirements.
    """
    
    requirements_lst = []
    try:
        with open('requirements.txt', 'r') as file:
            ## Read lines from the fil 
            lines = file.readlines()
            ##Process each lines
            for line in lines:
                requirements = line.strip()
                
                ## Ignore comments and empty lines -e.
                if requirements and requirements != '-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the current directory.")                 
            
    return requirements_lst
    
setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Saurav',
    author_email='saurav3k2@gmail.com',
    packages = find_packages(),
    install_requires=get_requirements()
    
)
