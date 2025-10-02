# setup.py (GÜNCELLENMİŞ HALİ)

from setuptools import setup, find_packages

# requirements.txt dosyasını oku
with open('requirements.txt', 'r', encoding='utf-8') as f:
    required = f.read().splitlines()

# README.md dosyasını oku
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hermai',
    version='0.1.2',  # Versiyonu güncelledim
    author='bilgisayarkavramlari', # Adınızı veya kullanıcı adınızı yazın
    author_email='[E-posta Adresiniz]',
    description='A hermeneutic approach to explainable AI (XAI) with contextual and narrative explanations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bilgisayarkavramlari/hermai', 
    packages=find_packages(),
    install_requires=required,
    include_package_data=True,  # <-- EKLENDİ: MANIFEST.in dosyasını kullan
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