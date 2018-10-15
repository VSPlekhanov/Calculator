class BracketValidationException(RuntimeError):
    def __init__(self, message: str):
        self.message = message


class Validator:
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']

    @classmethod
    def validate_brackets(cls, expression: str) -> None:

        def brackets_pare_is_fine(c1: str, c2: str) -> bool:
            return (c1 == '(' and c2 == ')') or (c1 == '[' and c2 == ']') or (c1 == '{' and c2 == '}')

        stack = []
        for i, c in enumerate(expression):
            if c in Validator.open_brackets:
                stack.append(c)
            elif c in Validator.close_brackets:
                if len(stack) == 0:
                    raise BracketValidationException('Extra close bracket: \'{0}\' on position {1}'.format(c, i))
                if not brackets_pare_is_fine(stack.pop(), c):
                    raise BracketValidationException('Wrong close bracket: \'{0}\' on position {1}'.format(c, i))
        if len(stack) != 0:
            raise BracketValidationException('Extra open bracket(s): \'{0}\''.format(', '.join(stack)))
