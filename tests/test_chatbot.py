"""
Description: creating a chatbot for the pixell river transaction  
Author:Aman
Date:15-11-2023
Usage: prompts the user for various inputs and performs functions. 
"""
import unittest
from unittest.mock import patch
from src.chatbot import VALID_TASKS, ACCOUNTS,get_account,get_amount,get_balance

class ChatbotTests(unittest.TestCase):
    def test_get_account_valid_account(self):
        # Act
        with patch("builtins.input", side_effect=["123456"]):
            account_number = get_account()
            # Assert
            self.assertEqual(account_number, 123456)
    
    def test_get_account_non_numeric_input(self):
        # Act
        with patch("builtins.input", side_effect=["non_numeric_data"]):
            with self.assertRaises(ValueError) as context:
                get_account()
            # Assert
            self.assertEqual(str(context.exception), "Account number must be a whole number.")

    def test_get_account_account_not_in_accounts(self):
        # Act
        with patch("builtins.input", side_effect=["112233"]):
            with self.assertRaises(Exception) as context:
                get_account()
            # Assert
            self.assertEqual(str(context.exception), "Account number entered does not exist.")
    
    def test_get_amount_valid_amount(self):
        # Act
        with patch("builtins.input", side_effect=["500.01"]):
            result = get_amount()
            # Assert
            self.assertEqual(result, 500.01)

    
    def test_get_amount_non_numeric_input(self):
        # Act
        with patch("builtins.input", side_effect=["non_numeric_data"]):
            with self.assertRaises(ValueError) as context:
                get_amount()
            # Assert
            self.assertEqual(str(context.exception), "Invalid amount. Amount must be numeric.")

    
    def test_get_amount_zero_or_negative_amount(self):
        # Act
        with patch("builtins.input", side_effect=["0"]):
            with self.assertRaises(ValueError) as context:
                get_amount()
            # Assert
            self.assertEqual(str(context.exception), "Invalid amount. Please enter a positive number.")

    def test_get_balance_valid_account(self):
        # Arrange & Act
        with patch("builtins.input", side_effect=["123456"]):
            balance_info = get_balance(int(input("Enter account number: ")))
            expected_output = 'Your current balance for account 123456 is $1000.00.'
            # Assert
            self.assertEqual(balance_info, expected_output)

    def test_get_balance_account_not_in_accounts(self):
        # Act
        with patch("builtins.input", return_value="112233"):  # Input an account number not in ACCOUNTS
            with self.assertRaises(Exception) as context:
                get_balance(int(input("Enter account number: ")))
        # Assert
        self.assertEqual(str(context.exception), "Account number does not exist.")
    
    def test_make_deposit_updated_balance(self):
        # Arrange
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        deposit_amount = 1500.01
        # Act
        make_deposit(account_number, deposit_amount)
        # Assert
        self.assertEqual(ACCOUNTS[account_number]["balance"], 2500.01)

    def test_make_deposit_successful_message(self):
        # Arrange
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        # Act
        result = make_deposit(account_number, 1500.01)
        # Assert
        self.assertEqual(result, "You have made a deposit of $1500.01 to account 123456.")


    def test_make_deposit_account_not_exist(self):
        # Arrange
        account_number = 112233
        deposit_amount = 1500.01
        # Act
        with self.assertRaises(Exception) as context:
            make_deposit(account_number, deposit_amount)
        # Assert
        self.assertEqual(str(context.exception), "Account number does not exist.")

    def test_make_deposit_negative_amount(self):
        # Arrange
        account_number = 123456
        deposit_amount = -50.01
        # Act
        with self.assertRaises(ValueError) as context:
            make_deposit(account_number, deposit_amount)
        # Assert
        self.assertEqual(str(context.exception), "Invalid Amount. Amount must be positive.")

    def test_user_selection_valid_lowercase(self):
        # Act
        with patch("builtins.input", return_value="balance"):
            result = user_selection()
            # Assert
            self.assertEqual(result, "balance")

    def test_user_selection_valid_mixed_case(self):
        # Act
        with patch("builtins.input", return_value="DePosiT"):
            result = user_selection()
            # Assert
            self.assertEqual(result, "deposit")

    def test_user_selection_invalid(self):
        # Act
        with patch("builtins.input", return_value="invalid_selection"):
            with self.assertRaises(ValueError) as context:
                user_selection()
            # Assert
            self.assertEqual(str(context.exception), "Invalid task. Please choose balance, deposit, or exit.")