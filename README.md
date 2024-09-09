# Click Datetime (in progress)

Click support for Python's `datetime` types to allow developers to easy parse 
date strings as parameters to Python click CLIs.

## Example

```bash
$ my-app import-task --start-date=2015-01-01 --end-date=2016-01-01
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
