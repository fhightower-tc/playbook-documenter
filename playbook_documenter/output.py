#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Output the documentation in a certain format."""


def create_html_output(json_docs):
    """Create html output for the playbook by converting the docs to markdown and then converting to html."""
    markdown_docs = create_markdown_output(json_docs)
    html_markdown = 1 # TODO: convert markdown to html


def create_markdown_output(json_docs):
    """Convert the docs to markdown."""
    markdown_template = """
## Documentation

{%- if json_docs.trigger %}
    ### Triggers

    {% for trigger in triggers %}
        - {{ trigger }}
    {% endfor %}
{%- endif %}

{%- if json_docs.http_link %}
    ### HTTP Link Trigger

    *This playbook uses an HTTP trigger. The following parts of the request sent to trigger this playbook are used in the playbook:*

    {% for request_part in json_docs.http_link %}
        - {{ request_part.app }}: {{ request_part.part }}
    {% endfor %}
{%- endif %}

{%- if json_docs.custom_metrics %}
    ### Custom Metrics

    *This playbook uses the following custom metrics \[[learn more](https://docs.threatconnect.com/en/latest/rest_api/custom_metrics/custom_metrics.html#custom-metrics)\]:*

    {% for custom_metric in json_docs.custom_metrics %}
        - Custom Metric Name: (( custom_metric.name ))
            - Weight: (( custom_metric.weight ))
            - Date: (( custom_metric.date ))
            - Value: (( custom_metric.value ))
            - Key: (( custom_metric.key ))
    {% endfor %}
{%- endif %}

{%- if json_docs.datastores %}
    ### Datastores

    *This playbook uses the following datastores:*


    {% for datastore in json_docs.datastores %}
        <!-- TODO: only display a value is it is not empty -->
        - `(( datastore.db_method )) (( datastore.domain_type.lower() ))/(( datastore.type_name ))/(( datastore.path ))`:
            - Datastore Entity: `(( datastore.request_entity ))`
            - Datastore Organization: (( datastore.organization_name ))
    {% endfor %}

{%- endif %}

{% if json_docs.variables|length > 0 %}
    {% if json_docs.variables.user_variables|length > 0 %}
        ### User Variables

        *This playbook expects the following user variables:*

        <!-- TODO: only display a value is it is not empty -->
        {% for variable in json_docs.variables.user_variables %}
            - (( variable.type )): (( variable.name ))
        {% endfor %}
    {% endif %}

    {% if json_docs.variables.org_variables|length > 0 %}
        ### Organization Variables

        *This playbook expects the following organization variables:*

        <!-- TODO: only display a value is it is not empty -->
        {% for variable in json_docs.variables.org_variables %}
            - (( variable.type )): (( variable.name ))
        {% endfor %}
    {% endif %}
{% endif %}

{% if json_docs.internal_variables %}
    ### Variables Declared in the Playbook

    *The following variables are declared in this playbook:*

    <!-- TODO: only display a value is it is not empty -->
    {% for variable in json_docs.internal_variables %}
        - (( variable.key )): (( variable.value ))
    {% endfor %}
{% endif %}
"""

