def count_words(text):
    if not text:
        return 0
    words = text.split()
    return len(words)

def main():

    user_input = input("Please enter a sentence or paragraph: ").strip()


    if not user_input:
        print("No input provided By User")
    
    word_count = count_words(user_input)
    print(f"The word count is: {word_count}")


if __name__ == "__main__":
    main()