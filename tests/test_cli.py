"""Tests for CLI."""
import os

import pytest
from gendiff.cli import cli


def test_help_command():
    """Test for correct exit with -h command."""
    exit_status = os.system('gendiff -h')
    assert exit_status == 0


def test_cli_without_arg():
    """Test without arguments."""
    with pytest.raises(SystemExit):
        cli.parse_arguments()
        pytest.fail()
