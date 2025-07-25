import random

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def main():
    roll_count = 0
    print("Welcome to the Dice Roller!")
    while True:
        try:
            num_dice = int(input("How many dice would you like to roll? "))
            if num_dice < 1:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        results = roll_dice(num_dice)
        roll_count += 1
        print(f"Roll {roll_count}: You rolled: {results}")

        again = input("Roll again? (y/n): ").strip().lower()
        if again != 'y':
            print(f"Total rolls this session: {roll_count}")
            break

if __name__ == "__main__":
    main()
