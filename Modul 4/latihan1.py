#Sistem login
count = 0
while count <= 3:
    username = input('Enter username: ') 
    password = input('Enter password: ')
    if password == 'udin345' and username == 'udin':
        print('Access granted.')
        break

    else:
        print('Access denied. Try again.')
        count += 1
        if count == 3:
            print('You have been blocked.')
