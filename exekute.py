import os
import click
import shutil
from os.path import isfile


@click.command()
@click.option('--copy', nargs=2,help="The equivelent of the linux command cp.")
@click.option('--remove', nargs=1,help="The equivelent of the linux command rm.")
@click.option('--mkdir', nargs=1,help="The equivelent of the linux command mkdir.")
def cli(copy, remove, mkdir):
    if copy:
        src = copy[0]
        dest = copy[1]
        shutil.copy(src, dest) if isfile(src) else shutil.copytree(src, dest)
    if remove:
        os.remove(remove) if isfile(remove) else shutil.rmtree(remove)
    if mkdir:
        os.mkdir(mkdir)
