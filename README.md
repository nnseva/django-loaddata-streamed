[![Tests with Django v2-v3](https://github.com/nnseva/django-loaddata-streamed/actions/workflows/test-django2-3.yml/badge.svg)](https://github.com/nnseva/django-loaddata-streamed/actions/workflows/test-django2-3.yml)

[![Tests with Django v4-v5](https://github.com/nnseva/django-loaddata-streamed/actions/workflows/test-django4-5.yml/badge.svg)](https://github.com/nnseva/django-loaddata-streamed/actions/workflows/test-django4-5.yml)

# Django-Loaddata-Streamed

Streamed deserializer for the `loaddata` management command with optimal memory consuming

## Installation

*Stable version* from the PyPi package repository
```bash
pip install django-loaddata-streamed
```

*Last development version* from the GitHub source version control system
```bash
pip install git+git://github.com/nnseva/django-loaddata-streamed.git
```

## Inspiration

The original `loaddata` management command provided with the `Django` consumes
the memory to load the JSON-formatted fixture file as a whole before parsing. It makes
harder using huge datasets with gigabytes of fixtures.

The package uses the package `json_stream` to stream the uploaded JSON instead reading the whole file to the memory.

## Using

### With a special file extension

- Setup streamed serializer in `settings.py`
```python
    SERIALIZATION_MODULES = {
        'jsons': 'loaddata_streamed.jsons_serializer',
    }
```

- Use the serializer with the fixture file using a special `.jsons` extension
```bash
    python manage.py dumpdata -o fixture-file.jsons
    python manage.py loaddata fixture-file.jsons
```

### For the existent `.json` fixture files dumped before

- Setup streamed serializer in `settings.py`
```python
    SERIALIZATION_MODULES = {
        'jsons': 'loaddata_streamed.jsons_serializer',
    }
```

- Explisitly set up the format for the `loaddata` management command
```bash
    python manage.py dumpdata -o fixture-file.json
    cat fixture-file.json | python manage.py loaddata - --format jsons
```

### Replacing the built-in `.json` serializer

- Setup streamed serializer in `settings.py`
```python
    SERIALIZATION_MODULES = {
        'json': 'loaddata_streamed.jsons_serializer',
    }
```

- Transparent use of the streamed serializer
```bash
    python manage.py dumpdata -o fixture-file.json
    python manage.py loaddata fixture-file.json
```

## TODO:

- use alternative JSON stream serializers
- measure speed
