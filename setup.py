from setuptools import find_packages,setup
from typing import List
setup(
    name='HousePricePrediction',
    version='0.0.1',
    author='teja tanush',
    author_email='tejatanush47@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)