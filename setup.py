import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {}
with open("waky/__init__.py", "r") as fp:
    exec(fp.read(), version)

setuptools.setup(
    name="waky",
    version=version["__version__"],
    author="Nicolas Landier",
    author_email="nicolas.landier@gmail.com",
    description="Waky is a web application to manage Wake-On-Lan supporting devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/landier/waky",
    packages=["waky"],
    include_package_data=True,
    install_requires=["getmac", "humanize", "jinja2", "ping3", "sanic"],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["waky=waky.main:main"]},
)
