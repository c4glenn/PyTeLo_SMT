from setuptools import setup, find_packages

setup(
    name="pytelo_smt",
    version="0.1.0",
    packages=find_packages(include=["stl", "mtl", "wmtl", "wstl"]),
)
