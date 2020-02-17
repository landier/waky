import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="waky",
    version="0.0.2",
    author="Nicolas Landier",
    author_email="nicolas.landier@gmail.com",
    description="Waky is a web application to manage Wake-On-Lan supporting devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/landier/waky",
    packages=setuptools.find_packages(),
    install_requires=["ping3", "sanic", "sanic_brogz"],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["waky=waky.main:main"]},
)
