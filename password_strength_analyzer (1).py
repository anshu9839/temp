# Password Strength Analyzer with Custom Wordlist Generator

import datetime
from collections import OrderedDict
from zxcvbn import zxcvbn

# ---- PASSWORD STRENGTH ANALYSIS ----
def analyze_password(password):
    result = zxcvbn(password)
    score = result['score']  # 0 (weak) to 4 (strong)
    feedback = result['feedback']
    suggestions = feedback.get('suggestions', [])
    warning = feedback.get('warning', '')

    print("\n[Password Analysis Result]")
    print(f"Score: {score}/4")
    if warning:
        print(f"Warning: {warning}")
    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print(f" - {s}")

    return score, suggestions

# ---- DATE VALIDATION ----
def is_valid_dob(dob):
    try:
        datetime.datetime.strptime(dob, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# ---- WORDLIST GENERATOR ----
def generate_wordlist(name, dob, pet):
    name = name.lower()
    pet = pet.lower()
    dob_parts = dob.split("-")  # Format: YYYY-MM-DD
    year = dob_parts[0]
    month = dob_parts[1]
    day = dob_parts[2]

    patterns = [
        name, pet, year, month + day,
        name + year, pet + year,
        name + "123", name + "@123",
        name + "!", name.capitalize(),
        name + "2024", name + "2025",
        name.replace('a', '@'),
        name.replace('s', '$'),
        name[::-1],
        name + "!" + year,
        pet.capitalize() + "@" + day,
        name + pet,
        name + pet + year
    ]

    unique_words = list(OrderedDict.fromkeys(patterns))
    return unique_words

# ---- SAVE WORDLIST TO FILE ----
def save_wordlist(wordlist, filename):
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(word + '\n')
    print(f"\n[+] Wordlist saved as {filename}")

# ---- USER INPUT COLLECTION ----
def collect_user_info():
    name = input("Enter your name: ")
    dob = input("Enter your DOB (YYYY-MM-DD): ")
    while not is_valid_dob(dob):
        dob = input("Invalid format. Enter DOB (YYYY-MM-DD): ")
    pet = input("Enter your pet name/fav word: ")
    return name, dob, pet

# ---- MAIN PROGRAM ----
def main():
    print("\n=== Password Strength Analyzer ===")
    password = input("Enter your password: ")
    analyze_password(password)

    print("\n=== Wordlist Generator ===")
    name, dob, pet = collect_user_info()
    wordlist = generate_wordlist(name, dob, pet)
    filename = f"custom_wordlist_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    save_wordlist(wordlist, filename)

if __name__ == '__main__':
    main()
