from setuptools import setup, find_packages

setup(
    name='PokerBot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Dependencies will be listed in requirements.txt
    ],
    entry_points={
        'console_scripts': [
            'pokerbot = main:main'
        ]
    },
    description='An AI-powered poker bot for online poker platforms.',
    author='Your Name',
    author_email='youremail@example.com',
    url='https://github.com/yourusername/PokerBot',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
