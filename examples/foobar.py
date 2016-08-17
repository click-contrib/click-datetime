
import click

from click_datetime import Datetime

@click.option('--date', type=Datetime(format='%d/%m/%y'), default='', help='''
An example parsing and printing a datetime.
''')
@click.command()
def foobar(date):
    click.echo('The date : {0}'.format(date))


if __name__ == '__main__':
    foobar()
