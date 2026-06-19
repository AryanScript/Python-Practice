# This is coding for json module


import json 

d='{"me":18,"maa":44,"papa":43,"anni":11}'

parshed=json.loads(d)
print(parshed)

d2='{"ghar":["aryan", "anni", "mummmy", "papa"]'\
'"gao":["pachaws", "ayodhya", "up"]}'

jscomp=json.dumps(d2)
print(jscomp)