# !/usr/bin/env python
# encoding: utf-8

# Script to convert TCs docstring into Jira description.

import re
from copy import deepcopy


def modify_docstring(text):
    mod1 = text.replace('            GIVEN', '** *Given*')
    mod2 = mod1.replace('            WHEN', '** *When*')
    mod3 = mod2.replace('            THEN', '** *Then*')
    mod4 = mod3.replace('IntegrationTest/', '* IntegrationTest/')
    mod5 = mod4.replace('        ', '')
    return mod5

with open("test_case.txt", "r") as test_case:
    all_docstrings = re.findall(r'(?<=""")(?s).*?(?=""")', test_case.read())
    all_docstrings_copy = deepcopy(all_docstrings)
    for docstring in all_docstrings_copy:
        if 'IntegrationTest/' not in docstring:
            all_docstrings.remove(docstring)
    jira = ''
    for docstring in all_docstrings:
        jira = ''.join((jira, modify_docstring(docstring)))
    jira = ''.join(('*Test Cases:*\n\n', jira))

with open("jira.txt", "w") as f:
    f.write(jira)
