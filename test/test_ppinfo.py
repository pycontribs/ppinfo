"""Tests for ppinfo package."""
import pytest

from ppinfo import Project


@pytest.mark.parametrize(
    ("path", "expected_python"),
    [("test/fixtures/proj1", "3.7"), ("test/fixtures/py310", "3.10")],
)
def test_min_version(path: str, expected_python: str) -> None:
    """Test ability to find minimal version of python required."""
    project = Project(path)
    assert project.min_python == expected_python
