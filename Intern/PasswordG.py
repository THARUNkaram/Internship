import random
import string

def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += random.choices(all_characters, k=length-4)

    
    random.shuffle(password)

    
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        for i in range(num_passwords):
            print(f"Password {i+1}: {generate_password(length)}")

    except ValueError:
        print("Please enter valid numbers for length and quantity.")

if __name__ == "__main__":
    main()
