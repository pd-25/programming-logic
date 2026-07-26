#reverse a string - hello

def do_reverse(text):
    return text[::-1]
def reverse_string(text: str):
    return " ".join(list(map(do_reverse, text.split(' '))))
    


def reverse_string(text: str):
    text_list = text.split(' ')
    return " ".join(t[::-1] for t in text_list)

print(reverse_string('in Many Programming Language such as JavaScript, Golang etc. map is a higher order Function that applies a given function and iterable the element one by one from the list , array , dict and set etc. the map function get element one by one from the list of dict and set on which the map function apply and send the element to the specified function which is given or pass the first args/parameter of the map.'))




    