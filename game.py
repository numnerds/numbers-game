import random

def fibonacci(n, first=0, second=1):
    """Generate a Fibonacci sequence of length n with custom starting values."""
    seq = [first, second]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

def next_number_challenge():
    """Challenge: Guess the next Fibonacci number in a complete sequence."""
    length = random.randint(5, 8)
    seq = fibonacci(length)
    print("Complete the sequence by entering the next Fibonacci number:")
    print(seq)
    correct_answer = seq[-1] + seq[-2]
    try:
        user_input = int(input("Your answer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    if user_input == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong, the correct answer is {correct_answer}.")

def missing_number_challenge():
    """Challenge: Identify the missing number in a Fibonacci sequence."""
    length = random.randint(6, 9)
    seq = fibonacci(length)
    missing_index = random.randint(1, length - 2)  # avoid the first two numbers
    missing_value = seq[missing_index]
    seq_display = seq.copy()
    seq_display[missing_index] = "___"
    print("Fill in the missing number in the Fibonacci sequence:")
    print(seq_display)
    try:
        user_input = int(input("Your answer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    if user_input == missing_value:
        print("Correct!")
    else:
        print(f"Wrong, the correct answer is {missing_value}.")

def custom_fibonacci_challenge():
    """Challenge: Calculate a term in a Fibonacci-like sequence with custom start values."""
    first = random.randint(1, 5)
    second = random.randint(1, 5)
    n = random.randint(6, 10)
    seq = fibonacci(n, first, second)
    print(f"Given a Fibonacci-like sequence starting with {first} and {second}, what is the {n}th term?")
    try:
        user_input = int(input("Your answer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    correct_answer = seq[-1]
    if user_input == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong, the correct answer is {correct_answer}.")

def main():
    print("Welcome to the Fibonacci Challenge!")
    rounds = 3  # Number of rounds to play
    for i in range(rounds):
        print(f"\nRound {i + 1}:")
        # Randomly select one of the three challenges
        challenge = random.choice([next_number_challenge, missing_number_challenge, custom_fibonacci_challenge])
        challenge()
    print("\nThanks for playing the Fibonacci Challenge!")

if __name__ == '__main__':
    main()
