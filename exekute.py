import click
from shutil import copy, copytree
from os.path import isfile

def copy_files(_from, _to):
    copy(_from, _to) if isfile(_from) else copytree(_from, _to)

@click.command()
@click.option('--copy', '-cp', multiple=True, nargs=2,
                help="The equivelent of the linux command cp.")
def cli(copy):
    if copy:
        _from = copy[0][0]
        _to = copy[0][1]
        copy_files(_from, _to)
