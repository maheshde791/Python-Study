#! /usr/bin/python

import re
pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print(pattern.search('415-867-5309'))
print(pattern.search('415-867-5309').groups())
print(pattern.search('415-867-539'))
