import string


password = input("\nType a password and see its security rating out of 7 points: ")

print("\nYOUR PASSWORD: '" + password + "'")

lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])

characters = [upper_case, lower_case, special, digits]

length = len(password)

score = 0

with open('passwords.txt', "r") as f:
    common = f.read().splitlines()

if password in common:
    print("SCORE: Password is too common, score 0 / 7")
    print("\nHINT: 'try for over 20 characters in length, include numbers and letters'")
    print("HINT: 'include special characters such as ' " + string.punctuation + " '")
    quit()

if length > 10:
    score += 1
if length > 14:
    score += 1
if length > 17:
    score += 1
if length > 20:
    score += 1

print("\nGrading below: ".upper())

print(f"Password length is {str(length)} characters, adding {str(score)} points!")

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) >= 3:
    score += 1

print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters))} points (try 3 different 'special' character types for the best score)")

if score < 4:
    print(f"\nSCORE: Password strength is weak, dont use this! Score: {str(score)} / 7")

elif score == 4:
    print(f"\nSCORE: Password is okay! Score: {str(score)} / 7")

elif score < 4 and score < 6:
    print(f"\nSCORE: Password is good! Score: {str(score)} / 7")

elif score > 6:
    print(f"\nSCORE: Password is Strong! Score: {str(score)} / 7")

print("\nTips Below: ".upper())
print("try for over 20 characters in length for the best score, include numbers and letters")
print("Have at least 3 special characters. Here is a list of 'special' characters to try (" + string.punctuation + ")")