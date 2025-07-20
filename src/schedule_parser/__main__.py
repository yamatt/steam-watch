import click

from .collection import ScheduleCollection
from .memory_db import ScheduleMemoryDB

@click.command()
@click.argument('file_paths', nargs=-1, type=click.Path(exists=True), required=True)
def schedule(file_paths):
    schedule = ScheduleCollection.from_paths(file_paths)
    services = ScheduleMemoryDB(schedule).services


if __name__ == '__main__':
    schedule()
