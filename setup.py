from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:

    requirement_list:List[str]=[]
    with open('requirements.txt', 'r') as filehandle:
        for line in filehandle:
        # Remove linebreak which is the last character of the string
            curr_place = line[:-1]
        # Add item to the list
            requirement_list.append(curr_place)
    
    return requirement_list


setup(
      
    name="sensor",
    version="0.0.1",
    author="Ishan",
    author_email="ishan.142@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),

)

