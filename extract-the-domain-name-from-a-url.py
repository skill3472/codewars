import re

def domain_name(url):
    return re.match('(?:https?:\/\/)?(?:www\.)?([A-Za-z0-9\-]+)\.', url)[1]

print(domain_name('http://www.zombie-bites.com'))