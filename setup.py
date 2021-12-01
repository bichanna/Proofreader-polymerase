from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'DNA proofreading'
LONG_DESCRIPTION = """
[Usage](https://github.com/bichanna/Proofreader)
"""

# Setting up
setup(
    name="DNAProofreader",
    version=VERSION,
    author="bichanna",
    author_email="nobu.bichanna@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/bichanna/Proofreader",
    packages=find_packages(),
	license="MIT",
    keywords=["DNA", "proofread", "proofreading", "proofreader", "python"],
    classifiers= [
        "Intended Audience :: Education"
    ],
    entry_points = """
        [console_scripts]
        proofread=Proofreader.main:main
    """
)