#find the ocurance of each char in a string

text: str = 'The current URL loading the Maps JavaScript API has not been added to the list of allowed referrers. Please check the referrer settings of your API key in the Cloud console.'

def find_occurance(text: str):
    occurance = {}
    for char in text.lower():
        if char in occurance:
            occurance[char]+=1
        else:
            occurance[char] = 1
    return occurance

print(find_occurance(text))