def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    letter_count = count_words(text)
    count_of_letters = count_letters(text)

    cleaned_letters = clean_up(count_of_letters)

    print_report(book_path, letter_count, cleaned_letters)



def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(texts):
    words = texts.split()
    return len(words)

def count_letters(texts):
    # orgainzed list, but probably not worth
    counts_of_letters = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }

    # words = texts.split()  // cleans up spaces, but not needed?

    # iterates over each letter in string and adds to count_of_letters dictionary based on the lowercase version of letter. Doesn't clean up non-letters
    for word in texts:
        if word.lower() in counts_of_letters:
            counts_of_letters[word.lower()] +=1
    return counts_of_letters

def clean_up(dictionary):
    sorted_letters = dict(sorted(dictionary.items(), key=lambda x:x[1], reverse=True))
    
    return sorted_letters

def output_stats(letters):
    for letter in letters:
        print(f"The '{letter}' character was found {letters[letter]} times")

def print_report(file_location, word_count, sorted_letter_count):
    print(f"--- Begin report of {file_location} ---")
    print(f"{word_count} words found in the document\n")
    output_stats(sorted_letter_count)

    
main()