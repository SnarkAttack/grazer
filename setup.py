import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grazer", # Replace with your own username
    version="0.0.1",
    author="Patrick McQuay",
    author_email="patrick.mcquay@gmail.com",
    description="Package to perform automated trading on Alpaca",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'alpaca-trade-api',
    ],
    tests_require=['pytest', 'coverage']
)