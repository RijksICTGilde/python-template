#!/usr/bin/env python
import pathlib


if __name__ == '__main__':

    if '{{ cookiecutter.use_django }}' != 'y':
        pathlib.Path('manage.py').unlink()
        pathlib.Path('{{ cookiecutter.project_python_slug }}', '__main__.py').unlink()
        pathlib.Path('{{ cookiecutter.project_python_slug }}', 'asgi.py').unlink()
        pathlib.Path('{{ cookiecutter.project_python_slug }}', 'settings.py').unlink()
        pathlib.Path('{{ cookiecutter.project_python_slug }}', 'urls.py').unlink()
        pathlib.Path('{{ cookiecutter.project_python_slug }}', 'wsgi.py').unlink()

    # if 'no' in '\{{ cookiecutter.command_line_interface|lower }}':
    #     pathlib.Path('src', '{{ cookiecutter.project_slug }}', 'cli.py').unlink()

    # if 'Not open source' == '{ { cookiecutter.open_source_license }}':
    #     pathlib.Path('LICENSE').unlink()
