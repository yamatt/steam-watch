from datetime import datetime
import json

import click

from .collection import ScheduleCollection
from .memory_db import ScheduleMemoryDB
from .query import SteamWatchQuery

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

@click.command()
@click.argument('file_paths', nargs=-1, type=click.Path(exists=True), required=True)
def schedule(file_paths):
    schedule = ScheduleCollection.from_paths(file_paths)
    services = ScheduleMemoryDB(schedule)
    query = SteamWatchQuery(services)

    print(json.dumps(list(query.all_stops()), default=json_serial))

if __name__ == '__main__':
    schedule()
