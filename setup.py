from distutils.core import setup
import py2exe

setup(
    # Application name:
    name="raspiducky",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Juan Ezquerro LLanes",
    author_email="arrase@gmail.com",

    # Packages
    packages=["RaspiDucky"],

    # Details
    url="https://github.com/arrase/Raspiducky",

    description="A Keyboard emulator like Rubber Ducky build over Raspberry Pi Zero W",
    console=['raspiducky.py'],
    data_files=[
        ('C:\\Users\\ferri\\Desktop\\Raspiducky-master\\ducky', ['raspiducky.py']),
        ('C:\\Users\\ferri\\Desktop\\Raspiducky-master\\ducky', ['duckyd.py'])
    ],
    requires=['pybluez']
)
