"""
pip install -e .
"""

import setuptools



setuptools.setup(
    name="finnish_business_portal",
    version="2023.2",
    author="markus.kaukonen@student.hanken.fi",
    author_email="markus.kaukonen@student.hanken.fi",
    description="collecting financial data in Finland",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.7",
    install_requires=[
    ],
)
