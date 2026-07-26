text = "dskfjhkjdssdsdfsdiowew"


  

def string_freq(text: str) -> str:
    store_count ={}
    for s in text:
        store_count[s] = store_count.get(s, 0)+1

    return " ".join(f"{k}-{v}" for k, v in store_count.items())

print(string_freq(text))