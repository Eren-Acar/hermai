# setup.py

from setuptools import setup, find_packages

# requirements.txt dosyasını oku
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='hermai',
    version='0.1.0',  # First version
    author='Sadi Evren SEKER',
    author_email='hermai@sadievrenseker.com',
    description='A hermeneutic approach to explainable AI (XAI) with contextual and narrative explanations.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bilgisayarkavramlari/hermai', 
    packages=find_packages(), 
    install_requires=required, #
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.8',
)