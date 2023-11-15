"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Student Name}
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

def get_account():
    """
    prompt the user to input account number 
    Returns:
    int: the account number entered
    Raises:
    ValueError: whenever the account entered does not exist 
    """
    while True:    
        try:
            account_number = int(input("Please enter your account number: "))
            if account_number in ACCOUNTS:
                return account_number
            else:
                raise Exception("Account number entered does not exist.")
        except ValueError:
            raise ValueError("Account number must be a whole number.")

def get_amount() -> float:
    """
    Prompt the user to enter an amount.

    Returns:
        float: The entered amount.

    Raises:
        ValueError: If the entered amount is not numeric or is zero/negative.
    """
    while True:
        try:
            # Prompt the user to enter the transaction amount.
            amount_string = input("Enter the transaction amount: ")

            # Attempt to parse the input as a float.
            try:
                amount = float(amount_string)
            except ValueError:
                raise ValueError("Invalid amount. Amount must be numeric.")

            # Check if the amount is greater than zero.
            if amount <= 0:
                raise ValueError("Invalid amount. Please enter a positive number.")

            return amount

        except ValueError as error:
            raise(error)

def get_balance(account: int) -> str:
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    balance = ACCOUNTS[account]["balance"]
    return f'Your current balance for account {account} is ${balance:.2f}.'

def make_deposit(account: int, amount: float) -> str:
    """
    deposit the specified amount into the specified account

    Args:
        account (int):account number
        amount (float):amount to deposit

    Returns:
        str: A message indicating a successful deposit.

    Raises:
        Exception: account is not listed in the ACCOUNTS library 
        ValueError: amount is greater than zero 
    """
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")

    if amount <= 0:
        raise ValueError("Invalid Amount. Amount must be positive.")

    ACCOUNTS[account]["balance"] += amount

    return f"You have made a deposit of ${amount:.2f} to account {account}."

def user_selection() -> str:
    # Define valid task options
    VALID_TASKS = ["balance", "deposit", "exit"]
    
    while True:
        # Prompt the user to enter their selection
        task = input("What would you like to do (balance/deposit/exit)? ").lower()

        # Validate the user's selection
        if task in VALID_TASKS:
            return task
        else:
            raise ValueError("Invalid task. Please choose balance, deposit, or exit.")



## GIVEN CHATBOT FUNCTION
