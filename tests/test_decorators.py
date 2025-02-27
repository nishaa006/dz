import os
import pytest
from src.decorators import log, my_function, error_function

def setup_module(module):
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

def test_successful_function():
    logged_func = log("test_log.txt")(my_function)
    result = logged_func(3, 4)
    assert result == 7
    with open("test_log.txt", "r", encoding="utf-8") as f:
        log_content = f.read()
    assert "my_function ok" in log_content


def test_function_with_error():
    logged_func = log("test_log.txt")(error_function)
    result = logged_func(0)
    assert result is None
    with open("test_log.txt", "r", encoding="utf-8") as f:
        log_content = f.read()
    assert "my_function ok\nerror_function ok\n" in log_content
