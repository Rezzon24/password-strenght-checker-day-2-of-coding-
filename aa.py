#age = int(input("enter your age:"))
#if age < 13:
    #print ("you are a child")
#elif age < 18:
    #print ("you are a teenager")
#else:
   # print("you are an adult")




#name = input("enter your name:")
#print ("welcome back " , name)
#hi = input("do you want me to say hi 20 times? (yes/no):")
#if "yes" .lower() == hi:
# for i in range (20):
  #  print ("hi")
  #  if "no" .lower() == hi:
      #  print ("ok byee")
      #  exit()



#import random


##secret = random.randint(1, 20)

#guess = int(input("enter a number beetween 1 and 20:"))
#while guess != secret:
  #  if guess > secret:
       #"" print("too high")
  #  elif guess < secret:
    #    print("too low")

  #  guess = int(input("try again:"))

#print ("congrats you guessed it right the number was" , secret)
    




password = input("enter a password:")

special = "!@#$%&*"


has_upper = False
has_lower = False
has_digit = False
has_special = False



if len (password) < 8:
        print ("passsword to short")
        exit()


for char in password:
        if char.isupper():
                has_upper = True
        elif char.islower():
                has_lower = True
        elif char.isdigit():
                has_digit = True
        elif char in special:
                has_special = True
           



if not has_upper and not has_lower and not has_digit and not has_special:
        print ("password is very weak")
elif not has_upper or not has_lower or not has_digit or not has_special:
        print ("password is meadium")
else:
        print ("strong password")