from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mvclab',
    version='0.1.0',
    author='Martin Akerman',
    author_email='makerman@gmail.com',
    description='A framework for initializing web projects with MVC structure',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Polario/mvclab',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=8.0.0',
        'gitpython>=3.1.0',
        'pathlib>=1.0.1',
    ],
    entry_points={
        'console_scripts': [
            'mvclab=mvclab.cli:cli',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Code Generators',
    ],
    python_requires='>=3.9',
) 