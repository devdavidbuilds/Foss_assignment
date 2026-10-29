from setuptools import setup, find_packages

setup(
    name="calculator",
    version="1.0.0",
    author="Student Author",
    author_email="author@example.com",
    description="A simple Python arithmetic package providing basic mathematical operations.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
