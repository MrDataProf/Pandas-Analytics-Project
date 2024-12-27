import os

path = input("Enter path: ")

print(path)

print(os.listdir(path)) #After writing/pasting your path DON'T FORGET to put '/' after the directory.

def main():
    i=1
    for filename in os.listdir(path):
        new_name = path + str(i) + '.jpg' #write the suitable file extension at the end as per your needs.
        old_name = path + filename
        os.rename(old_name,new_name)
        i+=1

main()