import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input ("how long do you want your password to be?"))
password = ""

for i in range(length):
    password += random.choice(symbols)

print(password)
