import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="waky",
    version="0.0.1",
    author="Nicolas Landier",
    author_email="nicolas.landier@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/landier/waky",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)