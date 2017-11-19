import click, os
from complex.cli import pass_context


@click.command('mkdir', short_help='')
@click.argument('dirname', nargs=1, required=True)
@pass_context
def cli(ctx):
    os.mkdir(mkdir)