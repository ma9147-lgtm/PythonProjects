name= input('please enter your first and last name in lower case \n ')
bday= input(' please enter your birthday as an 8-digit number yyyymmdd \n')

name = (name.title())

bday = bday[6:8], bday[4:6], bday[0:4] 

print (name,'was born on', bday)