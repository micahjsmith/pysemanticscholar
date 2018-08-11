#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `semsch` package."""

import unittest
from click.testing import CliRunner

from semsch import semsch
from semsch import cli


class TestSemsch(unittest.TestCase):
    """Tests for `semsch` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        pass

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_000_something(self):
        """Test something."""
        self.assertTrue(True)

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'semsch.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
