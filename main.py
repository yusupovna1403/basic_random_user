import json 

f= open('data.json').read()
data = json.loads(f)
print(data)