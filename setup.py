import os
from setuptools import setup, find_packages

info = {}
current_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_dir, "README.md"), "r") as fh:
    long_description = fh.read()

with open(os.path.join(current_dir, "feedler", "__meta__.py"), "r") as file:
    exec(file.read(), info)

setup(
    name=info["__title__"],
    description=info["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=info["__version__"],
    author=info["__author__"],
    author_email=info["__author_email__"],
    license=info["__license__"],
    url="https://github.com/xheuz/feedler",
    keywords="rss json feed feeds parser",
    install_requires=["defusedxml==0.6.0", "requests==2.24.0"],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6.*",
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Text Processing :: Markup :: XML",
    ),
)
