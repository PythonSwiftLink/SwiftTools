import os
from setuptools import setup, find_packages

BUILD_ID = os.environ.get("BUILD_BUILDID", "0")

setup(
    name="swift_tools",
    version="0.1" + "." + BUILD_ID,
    # Author details
    author="PythonSwiftLink",
    author_email="pythonswiftlink@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    setup_requires=[],
    tests_require=[],
    extras_require={},
)