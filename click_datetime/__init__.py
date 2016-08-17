
import click
from datetime import datetime

class Datetime(click.ParamType):
    '''
    A datetime object parsed via datetime.strptime.

    Format specifiers can be found here :
    https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    '''

    name = 'date'

    def __init__(self, format):
        self.format = format

    def convert(self, value, param, ctx):
        if value is None:
            return value

        if isinstance(value, datetime):
            return value

        try:
            datetime_value = datetime.strptime(value, self.format)
            return datetime_value
        except ValueError:
            self.fail('Could not parse datetime string "{datetime_str}" formatted as {format}'.format(
                datetime_str=value, format=self.format,), param, ctx)
