from datetime import datetime
import json
from urllib.parse import quote_plus

import click
from jinja2 import Environment, FileSystemLoader

def datetime_to_google_calendar_format(dt_str):
    dt = datetime.fromisoformat(dt_str)
    return dt.strftime("%Y%m%dT%H%M%SZ")

def capitalise(s):
    def cap(part):
        if len(part) == 3:
            return part
        return part.capitalize()
    return " ".join([ cap(part) for part in s.split() ])

@click.command()
@click.argument("template_file_name", required=True)
@click.argument("data_file_path", type=click.Path(exists=True), required=True)
@click.argument("tiploc_data_file_path", type=click.Path(exists=True), required=True)
@click.argument('templates_dir_path', type=click.Path(exists=True), default="src/templates")
def render(template_file_name, data_file_path, tiploc_data_file_path, templates_dir_path):
    env = Environment(loader=FileSystemLoader(templates_dir_path))
    env.filters["urlquote"] = quote_plus
    env.filters["dt"] = datetime_to_google_calendar_format
    env.filters["capitalise"] = capitalise
    template = env.get_template(template_file_name)
    output = template.render(data=json.load(open(data_file_path)), tiploc=json.load(open(tiploc_data_file_path)))
    print(output)

if __name__ == "__main__":
    render()
