from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()


REPO_NAME="Book-Recommender-System"
AUTHOR="Shubham Joshi"
EMAIL="indsjos@gmail.com"
LIST_OF_REQ=[]
SRC_REPO="Books_Recommender"

setup(
    name=REPO_NAME,
    version="0.0.1",
    author=AUTHOR,
    author_email=EMAIL,
    description="A simple book recommender system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shubham23i/Book-Recommender-System",
    packages=find_packages(),
    install_requires=LIST_OF_REQ,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)