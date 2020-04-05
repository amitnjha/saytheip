
from subprocess import call

number = int(input('Give me a number(0-9) : '))

for i in range(number, -1, -1):
    call(['afplay' , str(i)+'.mp3'])

