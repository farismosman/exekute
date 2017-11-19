import click
import shutil
from os.path import isfile
from complex.cli import pass_context


@click.command('copy', short_help='')
@click.argument('src', nargs=1, required=True)
@click.argument('dest', nargs=1, required=True)
@pass_context
def cli(ctx, src, dest):
    shutil.copy(src, dest) if isfile(src) else shutil.copytree(src, dest)