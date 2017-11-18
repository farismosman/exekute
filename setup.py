from setuptools import setup

setup(
    name='exekute',
    version='0.1',
    py_modules=['exekute'],
    install_requires=[
        'Click',
        'shutil'
    ],
    entry_points='''
        [console_scripts]
        exekute=exekute:cli
    ''',
)
