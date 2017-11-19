import click
import os, shutil
from os.path import isfile
from complex.cli import pass_context


@click.command('remove', short_help='')
@click.argument('filename', nargs=1, required=True)
@pass_context
def cli(ctx, filename):
    os.remove(filename) if isfile(filename) else shutil.rmtree(filename)