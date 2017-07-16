import re

commaRegex = re.compile(r'^(\d{1,3})(,\d{3})*$')

mo = commaRegex.findall('1 fakjfa 3434 7,632,276 fhaj 345,564 66 ahffaj 4,567 78,58')

print(mo)
