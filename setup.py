from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="PythonRequire",
    packages=['require.py'],
    version='0.0.0'
    description="A require() function in python."
    long_description=long_description,
    long_description_content_type='text/markdown'
)