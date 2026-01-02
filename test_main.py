# test_main.py
import pytest
# CHANGE: Import from 'main' instead of 'app'
from main import calculate_sum

def test_calculate_sum_basic(monkeypatch, capsys):
    # Simulate user inputs: "10", then "20", then "exit"
    inputs = iter(["10", "20", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    calculate_sum()

    captured = capsys.readouterr()

    # Assertions
    assert "Current sum: 10.0" in captured.out
    assert "Current sum: 30.0" in captured.out
    assert "Final Total Sum: 30.0" in captured.out

def test_calculate_sum_invalid_input(monkeypatch, capsys):
    # Simulate: "10", then "garbage text", then "5", then "exit"
    inputs = iter(["10", "hello", "5", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    calculate_sum()
    captured = capsys.readouterr()

    assert "Invalid input" in captured.out
    assert "Final Total Sum: 15.0" in captured.out