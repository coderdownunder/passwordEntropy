import sys, math
import webbrowser

from pip._vendor.distlib.compat import raw_input

keyspace = 0
good_password_length = 6634204312890624
bad_password_length = 0
tip = "https://www.cyber.gov.au/"

def get_keyspace(password):

    global keyspace
    char_set = 95
    keyspace = char_set ** len(password)
    print('Password:', password, 'has a total of: ', str(keyspace), 'K combinations')

    if int(keyspace) > good_password_length:
        print("Your password is secure")
    else:
        print("Your password needs securing")
        print("You can visit the Australian cyber Security Centre for \nmore information on how to secure "
              "yourself online at: " + tip)

def main():
    password = raw_input("Please enter your password: ")
    get_keyspace(password)

