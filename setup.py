from struct import pack_into

import setuptools

with open("README.md", "r", encoding= "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "Potatodisecese"
AUTHOR_USER_NAME = 'Dhanashree61'
SCR_REPO ="CNNClassifier"
AUTHOR_EMAIL = "dhanashree.kalbande9145@gmail.com"

setuptools.setup(
    name = SCR_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A Small python package for CNN Classifier",
    Lomg_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)