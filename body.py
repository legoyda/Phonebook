import json

print("Gritte in utility Phonebook.......\n"
      " For creating a new contakt press >ADD<.....\n"
      "  For edit a contact press a >EDIT< that editting wants....... \n"
      "   For delete a contakt press >DEL<......\n"
      "    For Exit press >QUIT<...........")
enter_raw = input('Enter>>')


if enter_raw == 'ADD':
    import Firstform
elif enter_raw == 'EDIT':
    import edit
elif enter_raw == 'DEL':
    import deletef
elif enter_raw == 'QUIT':
    exit()
