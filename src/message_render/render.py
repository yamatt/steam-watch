from datetime import datetime
import json
from urllib.parse import quote_plus

from jinja2 import Environment, FileSystemLoader

def datetime_str_to_dt(dt_str):
    return datetime.fromisoformat(dt_str)

def datetime_to_google_calendar_format(dt_str):
    dt = datetime_str_to_dt(dt_str)
    return dt.strftime("%Y%m%dT%H%M%SZ")

def datetime_to_rtt_url_format(dt_str):
    dt = datetime_str_to_dt(dt_str)
    return dt.strftime("%Y-%m-%d")

def datetime_to_friendly_format(dt_str):
    dt = datetime_str_to_dt(dt_str)
    return dt.strftime("%A %-d %B %Y at %-H:%M")

def capitalise(s):
    def cap(part):
        if len(part) == 3:
            return part
        return part.capitalize()
    return " ".join([ cap(part) for part in s.split() ])


def get_template_environment(templates_dir_path):
    env = Environment(loader=FileSystemLoader(templates_dir_path))
    env.filters["urlquote"] = quote_plus
    env.filters["google_calendar_url_dt"] = datetime_to_google_calendar_format
    env.filters["rtt_url_dt"] = datetime_to_rtt_url_format
    env.filters["friendly_dt"] = datetime_to_friendly_format
    env.filters["capitalise"] = capitalise
    return env
    
def render(template_file_name, services_file_path, tiploc_data_file_path, templates_dir_path):
    env = get_template_environment(templates_dir_path)
    template = env.get_template(template_file_name)

    with open(services_file_path) as services_f, open(tiploc_data_file_path) as tiploc_f:
        services = json.load(services_f)
        tiploc_data = json.load(tiploc_f)

        output = template.render(services=services, tiploc=tiploc_data)

    return output

if __name__ == "__main__":
    argument_handler()
