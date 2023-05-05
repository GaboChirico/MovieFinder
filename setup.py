from setuptools import setup

setup(
    name="StreamerFinder",
    version="0.1.0",
    packages=["src"],
    install_requires=["justwatch"],
    entry_points={
        "console_scripts": [
            "sf = src.main:main",
        ],
    },
)
