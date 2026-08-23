"""Tests for app.py — used by CI pipeline."""
from app import greet


def test_greet():
    assert greet("world") == "Hello, world!"


def test_greet_custom():
    assert greet("Harness") == "Hello, Harness!"