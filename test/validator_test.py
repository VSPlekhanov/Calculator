import unittest
from main.validator import Validator, BracketValidationException


class ValidatorTest(unittest.TestCase):
    def test_bracket_validation(self):
        self.assertRaises(BracketValidationException, Validator.validate_brackets, '()[]}')
        self.assertRaises(BracketValidationException, Validator.validate_brackets, '()[]}')
        self.assertRaises(BracketValidationException, Validator.validate_brackets, '{{[()]]')
        self.assertRaises(BracketValidationException, Validator.validate_brackets, '{{{[][][]')
        self.assertRaises(BracketValidationException, Validator.validate_brackets, '{*{{}')
        self.assertRaises(BracketValidationException, Validator.validate_brackets, '[[*')
        self.assertRaises(BracketValidationException, Validator.validate_brackets, '{{')
        self.assertRaises(BracketValidationException, Validator.validate_brackets, '}')
        self.assertRaises(BracketValidationException, Validator.validate_brackets, '{{{**[][][]')
        self.assertRaises(BracketValidationException, Validator.validate_brackets, '{{{**[][][}')
        self.assertRaises(BracketValidationException, Validator.validate_brackets, '15(25+1')
        self.assertIsNone(Validator.validate_brackets('([](){([])})'))
        self.assertIsNone(Validator.validate_brackets('{*}'))
        self.assertIsNone(Validator.validate_brackets('*{}'))
        self.assertIsNone(Validator.validate_brackets('{}'))
        self.assertIsNone(Validator.validate_brackets(''))
