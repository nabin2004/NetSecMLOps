from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    '''
    this function will return list of requirementss
    '''
    requirement_list: List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                ## ignore empty line and -e.
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

setup(
    name="NetSecMLOps",
    version="0.0.1",
    author="Nabin Oli",
    author_email="nabinoli2004@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)