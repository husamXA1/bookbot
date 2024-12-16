def count_words(s):
    return len(s.split())

def count_characters(s):
    s = s.lower()
    frequencies = {}
    for c in s:
        if not (ord(c) >= ord('a') and ord(c) <= ord('z')):
            continue
        if c in frequencies:
            frequencies[c] += 1
        else:
            frequencies[c] = 1
    return frequencies

with open("books/frankenstein.txt") as f:
    content = f.read()
    print("Frankenstein Book Report".center(50, "="))
    word_count = count_words(content)
    print(f"The book has {word_count} words.")
    print("Characters Frequencies:")
    characters = count_characters(content)
    for c in characters:
        print(f"Character {c} repeated {characters[c]} times.")
    print("End of report".center(50, "="))