from .render import render

import click

@click.command()
@click.argument("tiploc", required=True)
@click.argument("message_file_path", required=True)
def argument_handler(tiploc, message_file_path):
    output = render(tiploc, message_file_path)
    print(output)

if __name__ == "__main__":
    argument_handler()
