from setuptools import setup, find_packages

setup(
    name="quick-summarize-content-20260529_162300",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'quick=quick:main',
        ],
    },
)
