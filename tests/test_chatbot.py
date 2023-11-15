"""
Description: creating a chatbot for the pixell river transaction  
Author:Aman
Date:15-11-2023
Usage: prompts the user for various inputs and performs functions. 
"""
import unittest
from unittest.mock import patch
from src.chatbot import VALID_TASKS, ACCOUNTS,get_account

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


