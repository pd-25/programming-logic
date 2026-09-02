# reverse a string - hello


from re import split


def do_reverse(text):
    return text[::-1]


# def reverse_string(text: str):
#     return " ".join(list(map(do_reverse, text.split(" "))))


# def reverse_string(text: str):
#     text_list = text.split(' ')
#     return " ".join(t[::-1] for t in text_list)

# def reverse_string(text: str):
#     lst = []
#     count = 1
#     for i in range(0, len(text)):

#         lst.append(text[len(text) - count])
#         count += 1
#     return "".join(lst)

def reverse_string(text: str):
    lst = []
    # return text_lst[count]
    split_text = text.split()
    for t in range(len(split_text)-1, -1, -1):
       lst.append(split_text[t])
    return " ".join(lst)


print(
    reverse_string(
        "in Many Programming Language such as JavaScript, Golang etc. map is a higher order Function that applies a given function and iterable the element one by one from the list , array , dict and set etc. the map function get element one by one from the list of dict and set on which the map function apply and send the element to the specified function which is given or pass the first args/parameter of the map."
    )
)
