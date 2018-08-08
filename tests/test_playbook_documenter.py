#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `playbook_documenter` module."""

import os

import pytest

from playbook_documenter import playbook_documenter


def _read_file(file_name='add_tag_attribute.pbx'):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), './data/' + file_name)), 'r') as f:
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


def test_markdown_output_1():
    pb_string = _read_file()
    docs = playbook_documenter.generate_documentation(pb_string, output_format='markdown')
    assert docs.strip() == """## Documentation

### Triggers

- UserAction

### Variables Declared in the Playbook

*The following variables are declared in this playbook:*

- groupID: #Trigger:1044:trg.action.item!String
- metadataAddingPlaybookTrigger: <NO VALUE GIVEN>"""


def test_markdown_output_2():
    pb_string = _read_file('page_monitor.pbx')
    docs = playbook_documenter.generate_documentation(pb_string, output_format='markdown')
    assert docs.strip() == """## Documentation

### Triggers

- Timer

### Datastores

*This playbook uses the following datastores:*

- `GET local/pageMonitor/`:
  - 
  - Datastore Organization: 

- `POST local/pageMonitor/#App:10146:databaseID!String`:
  -  Datastore Entity: `{"hash": "#App:10129:hash.encode.md5!String"}`
  - Datastore Organization: 

### Variables Declared in the Playbook

*The following variables are declared in this playbook:*

- userAgent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36
- slackChannel: #slack-channel
- website: http://example.com
- slackMessagePrefix: [Page Monitor PB]
- nonExistHash: 0"""


def test_markdown_output_3():
    pb_string = _read_file('URL_reader.pbx')
    docs = playbook_documenter.generate_documentation(pb_string, output_format='markdown')
    assert docs.strip() == """## Documentation

### Triggers

- HttpLink

### HTTP Link Trigger

*This playbook uses an HTTP trigger. The following apps use some part of the incoming request:*

- HTTP Client 2: body"""


def test_markdown_output_4():
    pb_string = _read_file('RF Alerts Incident Create.pbx')
    docs = playbook_documenter.generate_documentation(pb_string, output_format='markdown')
    assert docs.strip() == """## Documentation

### Triggers

- CVE
- Task

### Variables Declared in the Playbook

*The following variables are declared in this playbook:*

- RF: Recorded Future Alert
- XRFToken: your_api_key_here"""


def test_markdown_output_5():
    pb_string = _read_file('Array Serializer.pbx')
    docs = playbook_documenter.generate_documentation(pb_string, output_format='markdown')
    print("{}".format(docs))
    assert docs.strip() == """## Documentation

### Triggers

- HttpLink

### HTTP Link Trigger

*This playbook uses an HTTP trigger. The following apps use some part of the incoming request:*

- Json Path 1: body
- Find and Replace 1: body
- Value Lookup 1: queryparam
- Logger 1: body

### Variables Declared in the Playbook

*The following variables are declared in this playbook:*

- triggerForThisPlaybook: https://sandbox.threatconnect.com/api/playbook/402b2179-b9a1-4085-9e6b-2604fb015b3d
- errorMessage: Request to #App:14487:link!String failed: #App:14488:http.status_code!String . Make sure this link is correct and that the playbook related to this link is turned on.
- errorMessage: Request to #App:14482:triggerForThisPlaybook!String failed: #App:14486:http.status_code!String . Make sure this link is correct (it should be the trigger link for this playbook)."""


def test_markdown_output_6():
    pb_string = _read_file('Recurring Task.pbx')
    docs = playbook_documenter.generate_documentation(pb_string, output_format='markdown')
    print("{}".format(docs))
    assert docs.strip() == """## Documentation

### Triggers

- Timer

### Variables Declared in the Playbook

*The following variables are declared in this playbook:*

- taskName: [RECURRING] Send Metrics to Administrator
- dueDateOffset: 2D"""


def test_markdown_output_7():
    pb_string = _read_file('indicator comment link creator.pbx')
    docs = playbook_documenter.generate_documentation(pb_string, output_format='markdown')
    print("{}".format(docs))
    assert docs.strip() == """## Documentation

### Triggers

- UserAction

### Variables Declared in the Playbook

*The following variables are declared in this playbook:*

- errorMessagePrefix: [Indictor Comment Link Creator PB]:
- shareCommentLink: [[#Trigger:1066:trg.action.type!String:#Trigger:1066:trg.action.item!String]]"""
