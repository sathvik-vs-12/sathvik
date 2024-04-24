def find_vowels(name):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in name.lower() if vowel in vowels]

if __name__ == "__main__":
    name = input("Enter a name: ")
    print("Vowels in the name:", find_vowels(name))