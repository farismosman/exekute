import click
from os import remove,mkdir
from os.path import isfile
from shutil import copy, copytree, rmtree

def copy_files(_from, _to):
    copy(_from, _to) if isfile(_from) else copytree(_from, _to)

def remove_files(arg):
    remove(arg) if isfile(arg) else rmtree(arg)

def create_directory(arg):
    mkdir(arg)

@click.command()
@click.option('--copy', '-cp', multiple=True, nargs=2,help="The equivelent of the linux command cp.")
@click.option('--remove', '-rm', multiple=True, nargs=1,help="The equivelent of the linux command rm.")
@click.option('--mkdir', nargs=1,help="The equivelent of the linux command mkdir.")
def cli(copy, remove, mkdir):
    if copy:
        _from = copy[0][0]
        _to = copy[0][1]
        copy_files(_from, _to)
    if remove:
        remove_files(remove[0])
    if mkdir:
        create_directory(mkdir)
