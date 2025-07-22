import json
import click

@click.command()
@click.argument("corpus_file_path", type=click.Path(exists=True), required=True)
def tiploc(corpus_file_path):
    corpus = json.load(open(corpus_file_path))
    print(json.dumps(dict([
        [entry["TIPLOC"], entry["NLCDESC"].capitalize()] for entry in corpus["TIPLOCDATA"] if entry.get("TIPLOC") and entry.get("NLCDESC")
    ])))

if __name__ == "__main__":
    tiploc()
