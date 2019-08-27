import pickle
import os
from cryptography.fernet import Fernet

def read_pickle():
    if os.path.exists('password_book.pkl'):
        with open('password_book.pkl','rb') as fp:
            if len(fp.read()):
                fp.seek(0)
                pl = pickle.load(fp)
            else:
                pl = {}
    else:
        pl = {}
    return pl

def write_pickle(pl):
    with open('password_book.pkl','wb') as fp:
        pickle.dump(pl, fp)
    return 'Done'

def new_password(cipsut, site_name,site_user,site_pass):
    pl = read_pickle()
    if site_name and site_name in pl.keys():
        pl[site_name].update({site_user:site_pass})
    else:
        pl.update({site_name:{site_user:site_pass}})
    return write_pickle(pl)

def del_password(cipsut, site_name,site_user):
    pl = read_pickle()
    if site_name and site_name in pl.keys():
        if site_user and site_user in pl[site_name].keys() and len(pl[site_name]) > 1:
            pl[site_name].pop(site_user)
        else:
            pl.pop(site_name)
    else:
        print('Sorry! Entered details does not exist !!!')
    return write_pickle(pl)

def show_password(cipsut, site_name,site_user):
    pl = read_pickle()
    if len(pl) < 1:
        print('File is empty!')
    elif site_name and site_name in pl:
        if site_user and site_user in pl[site_name]:
            print(cipsut.decrypt(pl[site_name][site_user]))
        else:
            for i in pl[site_name]:
                print(cipsut.decrypt(i), cipsut.decrypt(pl[site_name][i]))
    else:
        for i in pl:
            for j in pl[i]:
                print(cipsut.decrypt(j),cipsut.decrypt(pl[i][j]))
    return 'Done'


def selected_choice(user_choice):
    cipsut = user_key()
    site_name = cipsut.encrypt(bytes(input('Site Name: '),'utf-8'))
    site_user = cipsut.encrypt(bytes(input('Site Username: '), 'utf-8'))
    site_pass = cipsut.encrypt(bytes(input('Site Password: '), 'utf-8'))
    if user_choice == '1':
        return_string = new_password(cipsut, site_name,site_user, site_pass)
    elif user_choice == '2':
        return_string = new_password(cipsut, site_name,site_user, site_pass)
    elif user_choice == '3':
        return_string = show_password(cipsut, site_name, site_user)
    elif user_choice == '4':
        return_string = del_password(cipsut, site_name, site_user)
    else:
        return_string = "You've choosen to exit!"
    return return_string

def user_key():
    with open('pass_key.dat','rb') as fp:
        key = fp.read()
    return Fernet(key)

def pass_menu():
    print('1. New Password')
    print('2. Change Password')
    print('3. Show Password')
    print('4. Delete Password')
    print('5. Exit')
    user_choice = input('Enter a choice: ')
    return_string = selected_choice(user_choice)
    return return_string

if __name__ == '__main__':
    final_string = pass_menu()
    print(final_string)