import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
# This is a global constant that's why it's in alll caps

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
# Underscore is an anonymous varible in python so whenever user needs to loop for something nut the user don't actually care about the count or iterartion then just put the underscore and then you don't have an anused varaible anymore
           all_symbols.append(symbol) 

    columns = [[], [], []]
    for col in range(cols):
        # for every coloum we need to generate a certain number of symbols 
        for row in range(rows):
            value = random.choice(all_symbols)

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            # The above check is must because we must know that prior that the user has entered a digit and not any random stuff then after the next line makes sense 
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
                print("Please enter a number")


    return amount

deposit()                    


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) +")? " )
        # Above is happening a concatenation
        if lines.isdigit():
            # The above check is must because we must know that prior that the user has entered a digit and not any random stuff then after the next line makes sense 
            lines =int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
                print("Please enter a number")


    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? " )
        # Above is happening a concatenation
        if amount.isdigit():
            # The above check is must because we must know that prior that the user has entered a digit and not any random stuff then after the next line makes sense 
            amount =int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between &{MIN_BET} - ${MAX_BET}.")
                # Automatically converts into string for us
        else:
                print("Please enter a number")



    return amount



def main():
    # We can re-run the program when we call the main function
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough to bet that amount, your current balance is: ${balance}")
        else:
                break
    bet = get_bet()
   
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    # print(balance, lines)
main()