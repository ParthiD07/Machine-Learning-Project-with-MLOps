<<<<<<< HEAD
from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Parthi',
    author_email='parthiband2020@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
=======
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('/n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
name= 'Machine-Learning-Project-with-MLOps',
version='0.0.1',
author='Parthi',
author_email='parthiband2020@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')




)
>>>>>>> 886aad3f362f1f1fc1e1b0ca76260c9aae18447c
