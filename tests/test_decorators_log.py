import pytest

from src.decorators import log


def test_log(capsys):
    @log()
    def my_function(x, y, z):
        return x * y * z

    my_function({2}, 3, "5")
    captured = capsys.readouterr()
    assert "my_function error: TypeError. Inputs: ({2}, 3, '5'), {}\n" in captured.out


def test_log_capsys(capsys):
    @log()
    def my_function(x, y, z):
        return x * y * z

    my_function(2, 3, 5)
    captured = capsys.readouterr()
    assert "my_function ok\n" in captured.out
