from setuptools import setup

setup(
    name='solver',
    version='1.1',
    py_modules=['solver'],
    install_requires=[
        'Click',
    ],
    entry_points='''
    [console_scripts]
    solver=solver:cli
    ''',
)
