import hello

a = input("What is your name?")
hello.say_hello(a)


if __name__ =='__main__':
    from hello import say_hello
    say_hello(a)

import datetime
today = datetime.datetime.now()
str(today) 
repr(today)