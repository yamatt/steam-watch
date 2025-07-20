import click

from .collection import ScheduleCollection
from .memory_db import ScheduleMemoryDB
from .query import SteamWatchQuery

@click.command()
@click.argument('file_paths', nargs=-1, type=click.Path(exists=True), required=True)
def schedule(file_paths):
    schedule = ScheduleCollection.from_paths(file_paths)
    services = ScheduleMemoryDB(schedule)
    query = SteamWatchQuery(services)

    for station in query.get_stations():
        print(station)

if __name__ == '__main__':
    schedule()
