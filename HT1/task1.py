import task2

print("File one __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")

   with open('users.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['user_name','password'])
    users_data = [
        {'user_name':'hare', 'password': 'carrot54'},
        {'user_name': 'fox', 'password': 'hare4567'},
        {'user_name': 'wolf', 'password': 'fox44fox'},
        {'user_name':'bear', 'password': 'honey1256l'}
    ]
    writer.writeheader()
    writer.writerows(users_data)

