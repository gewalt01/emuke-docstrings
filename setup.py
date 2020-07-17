from setuptools import setup
from pathlib import Path

setup(
    name="fox",
    version='0.0.1',
    packages=["fox"],
    package_dir={"": str(Path("src"))},
)
