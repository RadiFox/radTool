import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="radTool",
    version="0.0.1",
    author="Sebastian Biernat",
    author_email="sebastian.biernat@icloud.com",
    description="little extension for FunnyCase",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RadiFox/radTool",
    project_urls={
        "Bug Tracker": "https://github.com/RadiFox/radTool/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: Windows",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)