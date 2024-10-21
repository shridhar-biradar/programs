
import json
f=open('demo3.txt','w')
original_data={1:10,2:20,3:30}
json_data=json.dumps(original_data)
# json_data=json.dumps({1:10,2:20,3:30})
f.write(json_data)
print('Data is stored')
f.close()
print('******************')

import json
f=open('demo3.txt','r')
json_data=f.read()
original_data=json.loads(json_data)
print(original_data)
f.close()
