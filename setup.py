from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req:
        return req.read().splitlines()

setup(
    name='Phonepe_data_analysis',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=read_requirements(),
    author='Immanuel',  # Replace with your name
    author_email='immanuel2504@gmail.com',
    description='A project for analyzing PhonePe transaction data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/immanuel2504/phonepe_data_analysis',  # Replace with your GitHub repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
