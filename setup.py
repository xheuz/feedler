import os
from setuptools import setup, find_packages

info = {}
current_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_dir, "feedler", "__meta__.py"), "r") as file:
    exec(file.read(), info)

setup(
    author_email=info["__author_email__"],
    author=info["__author__"],
    description=info["__description__"],
    install_requires=["defusedxml==0.6.0", "requests==2.24.0"],
    license=info["__license__"],
    name=info["__title__"],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6.*",
    version=info["__version__"],
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ),
)
