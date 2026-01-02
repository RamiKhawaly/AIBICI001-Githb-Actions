def calculate_sum():
    total_sum = 0
    
    print("Welcome to our program...")
    print("Type a number to add it to the sum.")
    print("Type 'exit' to finish and see the result.\n")

    while True:
        user_input = input("Enter a number: ")

        # Check if user wants to exit (handling case sensitivity)
        if user_input.lower() == 'exit':
            break
        
        try:
            # Convert input to a float to handle decimals
            number = float(user_input)
            total_sum += number
            print(f"Current sum: {total_sum}")
            
        except ValueError:
            # Handle cases where the input is not a number
            print("Invalid input. Please enter a number or 'exit'.")

    print("---")
    print(f"Final Total Sum: {total_sum}")

# Run the program
if __name__ == "__main__":
    calculate_sum()