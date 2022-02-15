from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name = "FakeWordle",
    version = "0.1.1",
    description = "(Definitely not the first) Wordle made in Python to practise for the big show",
    long_description = readme,
    author = "Varunan Varathan",
    author_email = "varunanvara@gmail.com",
    url = "https://github.com/varunan-vara/FakeWordle",
    license = license,
    packages = find_packages(exclude=('tests', 'docs'))
)