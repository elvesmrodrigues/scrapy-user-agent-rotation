import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scrapy-user-agent-rotator",
    version="1.0.1",
    author="Elves M. Rodrigues",
    author_email="elvesmateusrodrigues@gmail.com",
    description="Rotacionador de user-agent para Scrapy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elvesrodrigues/scrapy-user-agent-rotator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
