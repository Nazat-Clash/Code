from setuptools import setup, find_packages

setup(
    name='digital_clock',  # Package name
    version='1.0.0',
    description='A simple digital clock that can display the current local time in either 12-hour or 24-hour format.',
    author='Raiyan Khan',
    author_email='nazat.clash@gmail.com',
    packages=find_packages(),
    py_modules=['clock'],  # List all Python files in the package
)
