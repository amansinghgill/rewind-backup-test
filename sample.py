def greet_user(name):
    print(f"Hello, {name}! Welcome to the sample Python program.")

def square_number(number):
    return number ** 2

if __name__ == "__main__":
    # Greet the user
    user_name = input("Enter your name: ")
    greet_user(user_name)

    # Calculate the square of a number with input validation
    while True:
        num_input = input("Enter a number to square: ")
        try:
            num = float(num_input)
            result = square_number(num)
            print(f"The square of {num} is {result}.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
