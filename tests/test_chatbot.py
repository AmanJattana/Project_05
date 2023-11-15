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