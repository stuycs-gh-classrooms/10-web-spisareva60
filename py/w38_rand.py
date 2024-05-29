#!/usr/bin/python
print('Content-type: text/html\n')

def python():
    text = "hi there"
    random_number = random.randint(1, 100)  
    print(f"{text} {random_number}")
