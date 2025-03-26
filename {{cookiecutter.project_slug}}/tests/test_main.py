import subprocess

from {{cookiecutter.project_python_slug}} import __main__


def test_main_process():
    completed_process = subprocess.run(["python", "-m", "{{cookiecutter.project_python_slug}}"], capture_output=True, text=True)
    assert completed_process.returncode == 0


def test_main_function():
    assert __main__.main() == 0
