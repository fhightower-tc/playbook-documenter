#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `playbook_documenter` module."""

import os

import pytest

from playbook_documenter import playbook_documenter


def _read_file():
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "./data/pb1.pbx")), 'r') as f:
        return f.read()


def test_documenter():
    pb_string = _read_file()
    docs = playbook_documenter.generate_documentation(pb_string)
    assert len(docs) == 2
    assert docs == {'internal_variables': [{'key': 'groupID', 'value': '#Trigger:1044:trg.action.item!String'}, {'key': 'metadataAddingPlaybookTrigger', 'value': ''}], 'trigger': ['UserAction']}


def test_bad_output_format():
    pb_string = _read_file()
    with pytest.raises(ValueError):
        docs = playbook_documenter.generate_documentation(pb_string, output_format='foo')


def test_markdown_output():
    pb_string = _read_file()
    docs = playbook_documenter.generate_documentation(pb_string, output_format='markdown')
    print("docs {}".format(docs))
    assert docs.strip() == """## Documentation

### Triggers

- UserAction

### Variables Declared in the Playbook

*The following variables are declared in this playbook:*

- groupID: #Trigger:1044:trg.action.item!String
- metadataAddingPlaybookTrigger: <NO VALUE GIVEN>"""
