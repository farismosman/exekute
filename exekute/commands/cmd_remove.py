import click
import os, shutil
from os.path import isfile
from complex.cli import pass_context


def abort(ctx, opts, value):
    if not value:
        ctx.abort()

@click.command('remove', short_help='')
@click.argument('filename', nargs=1, required=True)
@click.option('--yes', is_flag=True, callback=abort,
              expose_value=False,
              prompt='Are you sure you want to remove files?')
@pass_context
def cli(ctx, filename):
    os.remove(filename) if isfile(filename) else shutil.rmtree(filename)