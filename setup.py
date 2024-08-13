from setuptools import setup, find_packages

setup(
    name='pull_request_reporter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'generate_reports=scripts.generate_reports:main',
        ],
    },
)
