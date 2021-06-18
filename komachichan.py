import json
from difflib import get_close_matches
data = json.load(open("Enter your path for the json 'data.json' file."))
data =  {k.lower(): v for k, v in data.items()}

def di(dicti):
    x = data[dicti]
    c = ' '.join(x)
    return ("{}, Onii-chan~.").format(c)

def nt(user_input):
    if user_input in data:
        b = di(user_input)
        return b
    
    elif len(get_close_matches(user_input, data.keys())) > 0:
        j = get_close_matches(user_input, data.keys())[0]
        yn = input(f"Did you mean {j}, Onii-chan~? Y for yes and N for no: ")
        yn = yn.upper()
        if yn == 'Y':
            v = get_close_matches(user_input, data.keys())[0]
            r = di(v)
            return r
        elif yn == 'N':
            return 'What word do want to define, Onii-chan~: '
        else:
            return 'Komachi-chan doens\'t understand'
        
    else:    
        return 'Onii-chan, are you stupid? That word doesn\'t exist.'

print('Welcome Back Onii-chan~!')
while True:
    user_input = input('What word do want to define, Onii-chan~: ')
    user_input = user_input.lower()   
    
    if user_input == 'byebye':
        h = 'Bye Onii-chan~'
        break
    else:
        uu = nt(user_input)
        if uu != 'What word do want to define, Onii-chan~: ':
            print(uu)
        continue
print(h)
