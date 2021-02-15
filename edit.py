import json
edit_raw = input('For select a contact to editing enter a NAME of contact>>\n'
                 '>>')
file = open('filename.txt','r',encoding='utf-8')
#edit_raw == 'LIST'
#print (file.read())
json_data = json.load(file)
for edit_raw in json_data:
    print (json_data)