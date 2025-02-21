def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

options = {
    "A": "1414884937242655719669145562427394884141",
    "B": "6892149109325320763773670235239019412986",
    "C": "6800923757255865070000705685527573290086",
    "D": "9847255590886266818998186626880955527489"
}


for key, value in options.items():
    result = palindrome(value)
    print(f"Option {key}: {'Palindrome' if result else 'Not a palindrome'}")