"""Tests for the application"""
import pytest
from app import hello


def test_hello():
    """Test hello function"""
    assert hello() == "Hello, World!"


def test_hello_returns_string():
    """Test that hello returns a string"""
    result = hello()
    assert isinstance(result, str)
