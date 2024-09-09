# Click Datetime

Click support for Python's `datetime` types to allow developers to easy parse 
date strings as parameters to Python click CLIs.

## Example

You can accept a datetime as a parameter to your click CLI

```python
from datetime import datetime
import click
from click_datetime import Datetime


@click.option(
    "--date",
    type=Datetime(format="%Y-%m-%d"),
    default=datetime.now(),
    help="An example parsing and printing a datetime.",
)
@click.command()
def cli(date: datetime):
    click.echo("The date : {0}".format(date))


if __name__ == "__main__":
    cli()  # type: ignore
```

```bash
$ python main.py --date=2016-01-01
```

## Installation

```bash
pip install click-datetime
```

## Development

### Building and packaging

```bash
poetry build
```

### Testing the compiled wheel

```bash
# Create a virtual environment for testing
python -m .venv/test
source .venv/test/bin/activate

# Confirm importing and exporting is correct
python -c 'import click_datetime as cd; print(dir(cd))'
```

## Authors

- Dawson Reid (@ddaws)
