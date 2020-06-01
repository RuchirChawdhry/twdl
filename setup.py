from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_desc = f.read()

entry_points = {
    "console_scripts": ["twdl=app:TWDL"],
}

setup(
    name="twdl",
    version="0.1",
    packages=find_packages(),
    entry_points=entry_points,
    # metadata:
    author="Ruchir Chawdhry",
    author_email="ruchir.github@outlook.com",
    description="",
    keywords="twitter download twdl dl twitter-dl tweet tweets video videos downloading downloads",
    url="https://github.com/RuchirChawdhry/twdl",
    license="MIT",
    long_description=long_desc,
)
