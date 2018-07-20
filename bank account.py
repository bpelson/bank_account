salt = []
import numbers

def write_salts():
    file = open("salts.txt", "w")
    for i in range(0,26):
        file.write(random.randint_)

def get_salt():
    file = open("salts.txt", "r")
    for line in file:
        salt.append(line)
    print(salt)

def salt_password(password):
    indexA = ord('a')
    password = password.lower()
    last_letter = password[-1]
    indexL = ord(last_letter)
    index = indexL - indexA
    if not last_letter.isalnum():
        index = 26
    if last_letter is numbers.Number:
        index = 27
    return salt[index]

def write_file():
    f = open("accounts.txt", "w")
    for username in accounts:
        f.write(username + " ")
        info = accounts[username]
        for item in info:
            f.write(str(item) + " ")
        f.write('\n')
    f.close()

import os.path

def read_file():
    if not os.path.isfile("accounts.txt"):
        return
    f = open("accounts.txt", "r")
    for line in f:
        words = line.split(" ")
        words.pop()
        username = words[0]
        password = words[1]
        PIN = words[2]
        balance = words[3]
        accounts.update({words[0] : [password, PIN, 0]})
    f.close()

import hashlib
accounts = {}
import time

def hasher(password):
    b = bytes(password, 'utf-8')
    m = hashlib.sha256(b)
    m = m.hexdigest ()
    return m


def edit(username):
    which = input("Would you like to change your username or password? ")
    if which == 'username' or which == 'user':
        userchange = input("What would you like to change your username to? ")
        for i in range(0,6):
            PIN = input("Please enter your PIN for security purposes. ")
            if PIN == 'Q' or PIN == 'q':
                return
            if i == 5:
                print("Incorrect PIN. You have been locked out.")
            elif hasher(PIN) == accounts[username][1]:
                info=accounts[username]
                del accounts[username]
                accounts[userchange]=info
                print("Username successfully changed to " + userchange)
                break
            else:
                print('Incorrect pin')
    elif which =='password' or which == 'pass':
        passchange = input('What would you like to change your password to? ')
        for i in range(0,6):
                PIN = input("Please enter your PIN for security purposes. ")
                if PIN == 'Q' or PIN == 'q':
                    return
                if i == 5:
                    print("Incorrect PIN. You have been locked out.")
                elif hasher(PIN) == accounts[username][1]:
                    accounts[username][0] = passchange
                    print('Password successfully changed to ' + passchange)


def modify(username):
    print("Welcome, " + username + "!")
    print("Your current balance is $" + str(accounts[username][2]))
    choice = input("Press 'T' to transfer funds, or 'A' to edit your account ")
    while choice != 'Q' or 'q':
        if choice == 'T' or choice == 't':
            destination = input("Who would you like to transfer money to? ")
            if destination == 'Q' or destination == 'q':
                return
            while not accounts.get(destination):
                print("User not found. Please enter a valid username")
                destination = input("Who would you like to transfer money to? ")
                
            valid = False
            while not valid:
                try:
                    transfer = int(input("How many funds would you like to transfer to " + destination + "? $"))
                    break
                except:
                    print("Please enter an integer only.")
                    pass
            while transfer > accounts[username][2]:
                print("You do not have enough funds to do that. Your current account balance is " + str(accounts[username][2]))
                destination = input("Who would you like to transfer money to? ")
                valid = False
                while not valid:
                    try:
                        transfer = int(input("How many funds would you like to transfer to " + destination + "? $"))
                        break
                    except:
                        print("Please enter an integer only.")
                        pass
                
            for i in range(0,6):
                PIN = input("Please enter your PIN for security purposes. ")
                if PIN == 'Q' or PIN == 'q':
                    return
                if i == 5:
                    print("Incorrect PIN. You have been locked out.")
                elif hasher(PIN) == accounts[username][1]:
                    print("Thank you! Transferring funds now...")
                    accounts[destination][2] += transfer
                    accounts[username][2] -= transfer
                    time.sleep(2)
                    print("Transfer successful! Your current account balance is $" + str(accounts[username][2]))
                    break
            choice = input("Press 'T' to transfer funds, or 'A' to edit your account ")    
        elif choice == 'A' or choice == 'a':
            edit(username)

def login():
    username = input("Username: ")
    if username == 'Q' or username == 'q':
        return
    if not accounts.get(username):
        print("Username not found. Please enter a valid username.")
        return
    corrpassword = accounts[username][0]
    for i in range(0,6):
        password = input("Password: ")
        password = hasher(password)
        if password == 'Q' or password == 'q':
            return
        elif i == 5:
            print("Incorrect password. You have been locked out.")
            return   
        elif password == corrpassword:
            modify(username)
            break
        else:
            print("Incorrect password. Please try again.")

#######################################################################################################################
get_salt()
salt_password("tac")

read_file()            
prompt = input("Enter \'C\' to create a new bank account, or \'L\' to login to an existing account. ")


while prompt != 'Q' and prompt != 'q':
    if prompt == 'C' or prompt == 'c':
        print("Welcome to Central Bank!")
        username = input("Create a username: ")
        while accounts.get(username):
            username=input("That username has already been taken. Please choose a differenent username: ")
        password = input("Create a secure password: ")
        password = password + salt_password(password)
        PIN = input("Create a secure four digit pin: ")
        password = hasher(password)
        while len(PIN) != 4:
            PIN = input("Please create a four digit secure pin code: ")
        PIN = hasher(PIN)
        accounts.update({username : [password, PIN, 0]})
        print("Your account has been successfully been created.\nPlease log into it on the homepage.")
        time.sleep(0.2)
    elif prompt == 'L' or prompt =='l':
       login()
       
    else:
        print("Please enter a valid option.")

    prompt = input("Enter \'C\' to create a new bank account, or \'L\' to login to an existing account. ")
write_file()
