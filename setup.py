from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.readlines()

setup(
    name="docs-research",
    version="0.1.0",
    author="Erik Novak",
    description="Setup the research documentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[req for req in requirements if req[:2] != "# "],
    setup_requires=["flake8"],
)