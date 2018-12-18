#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `semsch` package."""

import unittest
from unittest.mock import patch
from click.testing import CliRunner

from semsch import Author, Paper
from semsch import cli


class TestModels(unittest.TestCase):

    def test_author(self):
        authorId = 'abc123'
        author = Author(authorId=authorId)
        self.assertTrue(author.authorId, authorId)

    def test_paper(self):
        paperId = 'abc123'
        paper = Paper(paperId=paperId)
        self.assertTrue(paper.paperId, paperId)

    @patch('requests.get')
    def test_get_author(self, mock_get):
        fake_author_json = {
            'aliases': ['Far Boo', 'Foobar'],
            'citationVelocity': 1,
            'influentialCitationCount': 1,
            'name': 'Foo Bar',
            'papers': [],
            'url': 'http://foo.bar',
        }
        mock_get.return_value.json.return_value = fake_author_json

        authorId = 'abc123'
        author = Author(authorId=authorId)

        self.assertTrue(author.can_get())

        author.get()

        for attr in fake_author_json:
            actual = getattr(author, attr)
            expected = fake_author_json[attr]
            self.assertEqual(actual, expected)

    @patch('requests.get')
    def test_get_paper(self, mock_get):
        fake_paper_json = {
            'arxivId': None,
            'authors': [],
            'citationVelocity': 2,
            'citations': [],
            'doi': 'foo.10/bar.7',
            'influentialCitationCount': 1,
            'references': 0,
            'title': 'Title',
            'topics': [],
            'url': 'http://foo.bar',
            'venue': 'Venue',
            'year': 2007,
        }
        mock_get.return_value.json.return_value = fake_paper_json

        paperId = 'abc123'
        paper = Paper(paperId=paperId)

        self.assertTrue(paper.can_get())

        paper.get()

        for attr in fake_paper_json:
            actual = getattr(actual, attr)
            expected = fake_paper_json[attr]
            self.assertEqual(actual, expected)

    def test_author_endpoint(self):
        pass

    def test_paper_endpoint(self):
        pass


class TestCli(unittest.TestCase):

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'semsch.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
