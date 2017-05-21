from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sentiment',
    version='0.1.0',
    description='Sentiment analysis tool',
    long_description=readme,
    author='Matiushenkov Nikolay',
    author_email='mnvx@yandex.ru',
    url='https://github.com/mnvx/sentiment',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)