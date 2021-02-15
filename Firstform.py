import json
file = open('filename.txt','a+',encoding='utf-8')
#----------------------optonal window for user

add_name = input('Enter a name>>')
add_numb1 = input('Enter a number>>')
add_numb2 = input('Do you have any number? Y/N?')
form = {}
form[add_name] = [add_numb1]

if add_numb2 == 'YES':
    add_numb2 = input('Enter a number>>')
    form[add_name].append(add_numb2)
elif add_numb2 == 'NO':
    form = form

json.dump(form,file,indent=4)
file.close()