def factorial(num):
    if (num == 1):
        return num
    elif (num <= 0):
        return 0

    return num * factorial(num - 1)


print('HELLo World!')
username = input('Please, enter your name: ')
len_username = len(username)

if (len_username == 0):
    print('You did not enter a name')
    exit()

print(f'Hello, {username}!')
print(f'Your name has {len_username} letters. {len_username}! = {factorial(len_username)}')
