from setuptools import setup

setup(
    name='exekute',
    version='0.1',
    py_modules=['exekute', 'exekute.commads'],
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        exekute=exekute.cli:cli
    ''',
)
