import os
import sys
import click


CONTEXT_SETTINGS = dict(auto_envvar_prefix='EXEKUTE')


class Context(object):

    def __init__(self):
        pass

pass_context = click.make_pass_decorator(Context, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))

class ExecuteCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
               filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('exekute.commands.cmd_' + name, None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ExecuteCLI, context_settings=CONTEXT_SETTINGS)
@pass_context
def cli(ctx):
    pass