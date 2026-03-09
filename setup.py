from setuptools import setup

setup(
    name="twit",
    version="0.1.0",
    packages=["twit"],
    entry_points={"console_scripts": ["twit = twit.cli:main"]},
)
