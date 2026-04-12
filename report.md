# {{ title }}
**Date:** {{ date }}

## Summary Table
| {% for header in headers %}{{ header }} | {% endfor %}
| {% for header in headers %}--- | {% endfor %}
{% for row in rows -%}
| {% for cell in row %}{{ cell }} | {% endfor %}
{% endfor %}

## Detailed Insights
{% for row in rows %}
### Entry: {{ row[0] }}
- **Status:** {{ row[1] }}
- **Description:** This record was imported from the source file.
{% endfor %}