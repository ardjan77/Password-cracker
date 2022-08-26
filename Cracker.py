import hashlib
flag = 0
counter = 0

pass_hash = input("Enter md5 hash:")
wordlist = input("Passwords file name:")

try:
    pass_file = open(wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:
    word_format = word.encode('utf-8')
    digest = hashlib.md5(word_format.strip()).hexdigest()
    counter += 1

    if digest == pass_hash:
        print("Password found")
        print("Password is:" + word)
        print("After",counter, "tries.")
        flag = 1
        break

if flag == 0:
    print("Password not found in the file")
    print("Tried", counter, "different passwords.")


