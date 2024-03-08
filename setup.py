from setuptools import find_packages,setup
from typing import List

hypen_E="-e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if hypen_E in requirements:
            requirements.remove(hypen_E)
    return requirements

setup(
    name="DiamondPricePrediction",
    version="0.0.1",
    author="BheesettiAnand",
    author_email="anandbheesetti@gmail.com",
    install_requires=get_requirements("requirements_dev.txt"),
    packages=find_packages()
)