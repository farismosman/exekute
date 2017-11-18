import click
import os
from os.path import isfile
from shutil import copy, copytree, rmtree


@click.command()
@click.option('--copy', '-cp', multiple=True, nargs=2,help="The equivelent of the linux command cp.")
@click.option('--remove', '-rm', multiple=True, nargs=1,help="The equivelent of the linux command rm.")
@click.option('--mkdir', nargs=1,help="The equivelent of the linux command mkdir.")
def cli(copy, remove, mkdir):
    if copy:
        _from = copy[0][0]
        _to = copy[0][1]
        copy(_from, _to) if isfile(_from) else copytree(_from, _to)
    if remove:
        os.remove(remove[0]) if isfile(remove[0]) else rmtree(remove[0])
    if mkdir:
        os.mkdir(mkdir)
