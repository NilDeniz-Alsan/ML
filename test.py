import os
import random
os.system("CLS")

name_txt_file = 'isimler.txt'
surname_txt_file = 'soyad.txt'

surname_list = []
name_list = []

if os.path.isfile(name_txt_file):
    with open(name_txt_file) as file:
        name_list = file.read().split()   

if os.path.isfile(surname_txt_file):
    with open(surname_txt_file) as file2:
        surname_list = file2.read().split() 


def letter_counting_function(func_list):
    if func_list in numbers:
        return False
    else:
        return True
numbers = [0,1,2,3,4,5,6,7,8,9]

def password_generator(name_and_surname):
    password = []
    name_and_surname = list(name_and_surname.lower()) 
    int_or_str_letter_list = numbers + name_and_surname
    
    while len(password) < 6:
        password.append(random.choice(int_or_str_letter_list))
        #print(password,"normal")
        if len(password) > 1:
            #3 tane harf olamaz algoritması
            letter_count = list(filter(letter_counting_function,password))
            if len(letter_count) > 2:
                password.pop(len(password)-1)
                #print("3")

            #sıralı rakam olamaz algoritması
            if type(password[len(password)-2]) and type(password[-1]) is int and (password[len(password)-2] == password[-1] - 1):
                password.pop(len(password)-1)
                #print("sıralı")
            #art arta rakam veya sayı olamaz algoritması
            if password[len(password)-2] == password[-1]:
                password.pop(len(password)-1)
                #print("art")
    
    return "".join(map(str, password))
    
 
            
filename = "veri.dat"
if os.path.isfile(filename):
    f = open(filename, "w",encoding="utf-8")
else:
    f = open(filename, "x",encoding="utf-8")
     
for i in range(200):
    random_name = random.choice(name_list)
    random_surname = random.choice(surname_list)
    user_name_and_surname = random_name + random_surname
    #password_generator(user_name_and_surname)
    f.write(user_name_and_surname + " " + password_generator(user_name_and_surname) + "\n")






