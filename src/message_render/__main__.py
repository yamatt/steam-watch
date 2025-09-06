from .render import render

import click

@click.command()
@click.argument("template_file_name", required=True)
@click.argument("services_file_path", type=click.Path(exists=True), required=True)
@click.argument("tiploc_data_file_path", type=click.Path(exists=True), required=True)
@click.argument('templates_dir_path', type=click.Path(exists=True), default="src/templates")
def argument_handler(template_file_name, services_file_path, tiploc_data_file_path, templates_dir_path):
    output = render(template_file_name, services_file_path, tiploc_data_file_path, templates_dir_path)
    print(output)


if __name__ == "__main__":
    argument_handler()
