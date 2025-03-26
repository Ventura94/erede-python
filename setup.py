from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="erede",
    version="0.1.0",
    author="DevelopersRede",
    author_email="arian.ventura@zeb.mx",
    description="SDK de integração eRede",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DevelopersRede/erede-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        'requests>=2.25.1',
    ],
    include_package_data=True,
)
