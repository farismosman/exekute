import click
from subprocess import check_output
from complex.cli import pass_context


@click.command('commad', short_help='')
@click.argument('syntax', nargs=-1, required=True)
@pass_context
def cli(ctx, syntax):
    output = check_output(' '.join(syntax), shell=True)
    click.echo(output)