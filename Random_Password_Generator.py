import random
import string

def password_generator(length, use_uppercase, use_numbers, use_special_chars):
    
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    password = password_generator(length, use_uppercase, use_numbers, use_special_chars)
    print("Generated Password : ", password)

if __name__ == "__main__":
    main()