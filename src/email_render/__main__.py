from .render import render

import click

@click.command()
@click.argument("tiploc", required=True)
@click.argument("message_file_path", required=True)
def argument_handler(tiploc, message_file_path):
    return render(tiploc, message_file_path)

if __name__ == "__main__":
    email_json = argument_handler()
    print(email_json)
