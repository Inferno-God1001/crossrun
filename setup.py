from setuptools import setup, find_packages

setup(
    name='crossrun',
    version='1.0.0',
    author='Inferno-God1001',
    description='Run code in multiple languages (bash, ruby, python, javascript) from Python.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Inferno-God1001/crossrun',
    packages=find_packages(),
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
