
def first_unique_char(text: str):
    for i in range(0, len(text)-1):
        print(f"text[{i}]- {text[i]} text[{i+1}] - {text[i+1]}")
        if text[i] == text[i+1] or text[i] == text[i-1]:
            continue
        return text[i]



print(first_unique_char("aabbccded"))