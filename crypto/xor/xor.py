import sys
import random

# Flag Parts
flag_parts = [
    "shellmates{x0r_m4k3s_1t_s3cur3}"[0:len("shellmates{")],  # Part 1: "shellmates{"
    "shellmates{x0r_m4k3s_1t_s3cur3}"[len("shellmates{"):len("shellmates{x0r")],  # Part 2: "x0r"
    "shellmates{x0r_m4k3s_1t_s3cur3}"[len("shellmates{x0r"):len("shellmates{x0r_m4k")],  # Part 3: "m4k3"
    "shellmates{x0r_m4k3s_1t_s3cur3}"[len("shellmates{x0r_m4k3s_1t"):len("shellmates{x0r_m4k3s_1t_s3cur3")]   # Part 4: "1t_s3cur3}"
]

# Part 1: XOR Between Two Random Numbers
def xor_between_numbers():
    num1 = random.randint(1, 100)  # Random number between 1 and 100
    num2 = random.randint(1, 100)  # Random number between 1 and 100
    return num1, num2, num1 ^ num2

# Part 2: XOR with a Random Key
def xor_with_key(text):
    key = random.randint(0, 9)  # Random key between 0 and 9
    return ''.join(chr(ord(c) ^ key) for c in text), key

# Part 3: XOR in Random Binary Numbers
def xor_binary():
    bin1 = format(random.randint(0, 15), '04b')  # Random binary number (4 bits)
    bin2 = format(random.randint(0, 15), '04b')  # Random binary number (4 bits)
    return bin1, bin2, format(int(bin1, 2) ^ int(bin2, 2), 'b')

# Part 4: XOR between Numbers and Text with Random Numbers
def xor_with_numbers_and_text(flag_part):
    numbers = [random.randint(0, 9) for _ in range(len(flag_part))]  # Random numbers for each character
    result = []
    for i, char in enumerate(flag_part):
        xor_result = chr(ord(char) ^ numbers[i])
        result.append(xor_result)
    return ''.join(result), numbers

# Function to ask and check the answers for each part, and exit on wrong answer
def ask_part(part_number, prompt, correct_answer, flag_part):
    answer = input(prompt)
    if answer == correct_answer:
        print(f"✅ Correct! You unlocked Part {part_number}: {flag_part}")
    else:
        print(f"❌ Incorrect answer for Part {part_number}! Exiting the program.")
        sys.exit()  # Exit the program immediately if the answer is incorrect

# The script will ask and check the answers for each part
def solve_challenge():
    print("\n=== Welcome to the XOR-based Challenge! ===\n")
    print("In this challenge, you will solve different XOR puzzles to uncover a hidden flag.\n")

    # Part 1: XOR Between Two Numbers (randomized)
    print("\n--- Part 1: XOR Between Two Numbers ---")
    num1, num2, part_1_answer = xor_between_numbers()
    ask_part(1, f"XOR the numbers {num1} and {num2}. What is the result? ", str(part_1_answer), flag_parts[0])

    # Part 2: XOR with a Key (randomized)
    print("\n--- Part 2: XOR with a Key ---")
    text1 = "flag"
    part_2_answer, key = xor_with_key(text1)
    ask_part(2, f"XOR this string '{text1}' with the key {key}. What is the result? ", part_2_answer, flag_parts[1])

    # Part 3: XOR in Binary (randomized)
    print("\n--- Part 3: XOR in Binary ---")
    bin1, bin2, part_3_answer = xor_binary()
    ask_part(3, f"XOR these binary numbers: {bin1} and {bin2}. What is the result? ", part_3_answer, flag_parts[2])

    # Part 4: XOR between Numbers and Text (randomized)
    print("\n--- Part 4: XOR between Numbers and Text ---")
    flag_part = "m4k3"
    part_4_answer, numbers = xor_with_numbers_and_text(flag_part)
    ask_part(4, f"XOR each character of '{flag_part}' with the corresponding number in the list {numbers}. What is the result? ", part_4_answer, flag_parts[3])

    print("\n🎉 Congratulations! You have completed the XOR-based challenge. The full flag is revealed!")

if __name__ == "__main__":
    solve_challenge()
