---
title: "{{ title }}"
author: Automated Python Pipeline
date: \today
---

## Data Summary
Below is the processed data from the source file.

| {% for h in headers %}{{ h }} | {% endfor %}
| {% for h in headers %} --- | {% endfor %}
{% for row in rows -%}
| {% for h in headers %}{{ row[h] }} | {% endfor %}
{% endfor %}

\newpage

## Detailed Analysis
{% for row in rows %}
### Entry: {{ row.Name }}
- **Category:** {{ row.Category }}
- **Value:** ${{ row.Value }}
- **Note:** This entry was processed via Pandoc.
{% endfor %}