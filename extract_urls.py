import re

from html_source import html

# only extract .com URLs from html

# https? = match http and https
# (?:www.)? = match with or w/o www
# [^ ]+ = match everything but white space
# \.com/ = only match .com urls
# [^ ][^"]+ = break when you hit a white space or "
url_pattern = re.compile('https?://(?:www.)?[^ ]+\.com/[^ ][^"]+')
url_matches = url_pattern.findall(html)
print(url_matches)
