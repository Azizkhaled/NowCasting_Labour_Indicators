from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements(packages used in the project)
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        

setup(
name = 'Leveraging Transformers for Now-Casting Canadian Labor Indicators',
version='0.1',
author='Aziz Al-Najjar, Luke Budny, Tariq Elbahrawy',
author_email='azizknajjar@gmail.com, lukeswalks@hotmail.com, tariqbahrawy@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')





)