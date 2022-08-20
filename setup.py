from setuptools import find_packages, setup

setup(
    name="parrots-backend",
    version="1.0.0",
    description="Parrots media backend",
    install_requires=[
        "fastapi",
    ],
    url="https://github.com/seoul-parrots/parrots-backend",
    author="seoul-parrots",
    author_email="sunghwan@scatterlab.co.kr",
    packages=find_packages(exclude=["tests"]),
)
