import click

from .parser import ScheduleParser
from .memory_db import ScheduleMemoryDB

@click.command()
@click.argument('base_file_path', type=click.Path(exists=True), required=True)
@click.argument('updates_file_paths', nargs=-1, type=click.Path(exists=True))
def schedule(base_file_path, updates_file_paths):
    schedule = ScheduleParser.from_paths(base_file_path, updates_file_paths)
    db = ScheduleMemoryDB(schedule)

if __name__ == '__main__':
    schedule()
