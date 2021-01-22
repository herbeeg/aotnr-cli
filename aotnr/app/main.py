import click

@click.command()
def default():
    click.echo('Welcome to the aotnr-cli interface. Please state your purpose or use --help to guide you.')

if '__main__' == __name__:
    """Run default command if no context has been given."""
    default()
