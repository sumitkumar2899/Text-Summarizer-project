import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-project"
AUTHOR_USER_NAME = "Sumeet"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "sumitkumar2899@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/sumitkumar2899/Text-Summarizer-project.git",
    project_urls={
        "Bug Tracker": f"https://github.com/sumitkumar2899/Text-Summarizer-project.git/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)