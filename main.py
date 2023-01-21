import json 

f= open('data.json').read()
data = json.loads(f)
lst = data['results']
first_name = lst[0]['name']['first']
last_name = lst[0]['name']['last'] 
print(first_name,last_name)