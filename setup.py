import os
from setuptools import setup, find_packages

with open(
    os.path.join(os.path.dirname(__file__), "requirements/common.txt"), "r"
) as fh:
    requirements = fh.readlines()

NAME = "binance-connector-zxw"
DESCRIPTION = (
    "修复了原版的binance-connector-python的websocket连接丢失无法捕获错误的BUG，使其可以正常运行"
)
AUTHOR = "shuiheyangguang@me.com"
URL = "https://github.com/sunshineinwater/binance-connector-python-zxw"
VERSION = None

about = {}

with open("README.md", "r") as fh:
    about["long_description"] = fh.read()

root = os.path.abspath(os.path.dirname(__file__))

if not VERSION:
    with open(os.path.join(root, "binance", "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name=NAME,
    version=about["__version__"],
    license="MIT",
    description=DESCRIPTION,
    long_description=about["long_description"],
    long_description_content_type="text/markdown",
    AUTHOR=AUTHOR,
    url=URL,
    keywords=["Binance", "Public API"],
    install_requires=[req for req in requirements],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)
