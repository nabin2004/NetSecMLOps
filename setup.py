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

print(get_requirements())