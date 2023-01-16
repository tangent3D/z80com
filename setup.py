from setuptools import setup, find_packages

setup(
    name="z80com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pyserial",
        #"ucdev @ git+https://github.com/tangent3D/python-ucdev#egg=ucdev"
    ],
    entry_points={
        "console_scripts": ["z80com=z80com.cmd:main"]
    },
)
