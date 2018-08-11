#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import flash, Flask, render_template, redirect, request, url_for

import playbook_documenter

app = Flask(__name__)
app.secret_key = 'abc'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/docs", methods=['POST'])
def document_playbook():
    if request.form.get('playbook'):
        html_docs = playbook_documenter.generate_documentation(request.form['playbook'], output_format='html')
        markdown_docs = playbook_documenter.generate_documentation(request.form['playbook'], output_format='markdown')
        return render_template("index.html", html_docs=html_docs, markdown_docs=markdown_docs)
    else:
        flash('Please paste the text for a playbook to create documentation for it.', 'error')
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
