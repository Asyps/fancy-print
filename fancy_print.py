from time import sleep
from json import load

def json_setup(path):
    with open(path, encoding="UTF-8") as f:
        return load(f)

def fancy_print(*to_print, end="\n", rate:float=0.05, delay:float=1, does_clear:bool=False):
    pass_on = ""
    
    if does_clear:
        print("033c", end="")

    for i in to_print:
        pass_on += str(i) + " "
    
    for i in pass_on[:-1]:
        print(i, end="", flush=True)
        sleep(rate)
    print(end, end="")

    sleep(delay)

def fancy_input(*to_print, end="\n", rate:float=0.05, delay:float=1, does_clear:bool=False):  
    fancy_print(*to_print, end=end, rate=rate, delay=0, does_clear=does_clear)
    inp = input()
    sleep(delay)
    return inp

def say(json_entry, path, rate:float=0.05, delay:float=1, does_clear:bool=False):
    data = json_setup(path)
    fancy_print(data[json_entry], rate=rate, delay=delay, does_clear=does_clear)

def ask(json_entry, path, end=":", rate:float=0.05, delay:float=1, does_clear:bool=False):
    data = json_setup(path)[json_entry]
    
    options = ""
    for i in data.keys():
        if i != "context" and i != "ask":
            options += "/" + i
    options = "[" + options[1:] + "]"

    fancy_print(data["context"], rate=rate, delay=delay, does_clear=does_clear)

    while True:
        inp = fancy_input(data["ask"], options + end, rate=rate, delay=delay)
        
        if inp in data.keys() and inp != "context" and inp != "ask":
            fancy_print(data[inp], rate=rate, delay=delay)
            return inp
