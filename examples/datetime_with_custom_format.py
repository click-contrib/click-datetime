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
