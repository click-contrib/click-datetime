
import click
import datetime

class Datetime(click.ParamType):
    '''
    A datetime object parsed via datetime.strptime.

    Format specifiers can be found here :
    https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    '''

    name = 'date'

    def __init__(self, format):
        self.format = format

    convert(self, value, param, ctx):
        if value is None:
            return value

        try:
            date = datetime.strptime(value, self.format)
            return date
        except ValueError:
            self.fail('Could not parse datetime string {datetime_str} formatted as {format}'.format(
                datetime_str=value, format=self.format,), param, ctx)
