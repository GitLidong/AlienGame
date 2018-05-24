import json
numbers = range(1,10)
file_name = 'numbers.json'
with open(file_name,'w') as f_obj:
    json.dump(numbers,f_obj)

with open(file_name) as f_obj:
    numbers_result = json.load(f_obj)
print(numbers_result)

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")
