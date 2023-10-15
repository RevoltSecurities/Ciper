from setuptools import setup, find_packages

setup(
    name='Ciper',
    version='1.0.0',
    author='D.Sanjai Kumar',
    author_email='bughunterz0047@gmail.com',
    description="Ciper digs deep dive and found ip of user given subnet/cidrs networks and resolve to domains with valid ip's",
    packages=find_packages(),
    install_requires=[
        'colorama==0.4.4',
        'setuptools==68.1.2',
        "Requests==2.31.0"
    ],
    entry_points={
        'console_scripts': [
            'ciper = ciper.ciper:main'
        ]
    },
)
