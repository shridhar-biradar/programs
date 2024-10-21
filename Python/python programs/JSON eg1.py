# json.dumps() for converting json data to original data

import json

f=open('demo1.txt','w')

original_data=[10,20,30]

json_data=json.dumps(original_data)

f.write(json_data)
f.close()


import json
f=open('demo1.txt','r')

json_data=f.read()

original_data=json.loads(json_data)
print(original_data)
f.close()
