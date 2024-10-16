import math
import re

class AdvancedCalculator:
    def __init__(self):
        pass

    # Function to handle basic operations
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return 'undefined'
        return a / b

    # Function to handle powers and roots
    def square(self, a):
        return a ** 2

    def power(self, a, n):
        return a ** n

    def square_root(self, a):
        if a < 0:
            return 'undefined'
        return math.sqrt(a)

    # def nth_root(self, a, n):
    #     if a < 0 and n % 2 == 0:
    #         return 'undefined'
    #     return a ** (1 / n)

    def nth_root(self, a, n):
        # Handle the case where 'a' is negative and 'n' is odd
        if a < 0 and n % 2 != 0:
            return -(-a) ** (1 / n)  # Take the nth root of the positive part and apply the negative sign

        # Handle the case where 'a' is negative and 'n' is even (undefined in real numbers)
        if a < 0 and n % 2 == 0:
            return 'undefined'

        # For non-negative 'a' or even roots of non-negative 'a'
        return a ** (1 / n)

    # Trigonometric functions in radians
    def sin(self, a):
        return math.sin(a)  # Works in radians

    def cos(self, a):
        return math.cos(a)  # Works in radians

    def tan(self, a):
        return math.tan(a)  # Works in radians

    # Preprocess expression to handle nth roots and exponents
    def preprocess_expression(self, expression):
        # Use regex to match nth root pattern n√a
        root_pattern = r"(\d+)√(\d+)"

        # Replace nth root with the power expression (a ** (1/n))
        def root_replacer(match):
            n = match.group(1)
            a = match.group(2)
            return f"({a} ** (1/{n}))"

        # Substitute nth root pattern with power equivalent
        expression = re.sub(root_pattern, root_replacer, expression)

        # Replace '^' with '**' for exponentiation
        expression = expression.replace('^', '**')

        return expression

    # Function to evaluate the expression with brackets and precedence
    def evaluate_expression(self, expression):
        try:
            # Preprocess the expression to handle nth roots and exponents
            expression = self.preprocess_expression(expression)

            # Replacing symbols for readability
            expression = expression.replace('✕', '*').replace('➗', '/')

            # Using eval to evaluate the expression (handling large numbers automatically)
            result = eval(expression, {"__builtins__": None}, {
                'sin': self.sin, 'cos': self.cos, 'tan': self.tan,
                'sqrt': self.square_root, 'pow': self.power, 'nth_root': self.nth_root,
                'abs': abs, 'math': math
            })
            return result
        except ZeroDivisionError:
            return 'undefined'
        except OverflowError:
            return 'overflow'
        except Exception as e:
            return str(e)


# Main function to run the calculator
def main():
    calculator = AdvancedCalculator()

    # Continuously take input from the user
    while True:
        try:
            # Read expression from command line input
            user_input = input("Enter a mathematical expression (or type 'exit' to quit): ")

            # Exit the loop if the user types 'exit'
            if user_input.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                break

            # Evaluate the input expression
            result = calculator.evaluate_expression(user_input)
            print(f"Output: {result}")
            print("-" * 40)
        except KeyboardInterrupt:
            print("\nExiting the calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
