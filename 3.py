# Частота символов в строке

def char_frequency(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char,0) + 1
    return frequency

print(char_frequency('Hello, Honey'))