from fractions import Fraction
import math

def solve_proportion(a, b, c, d):
    variables = [a, b, c, d]
    if variables.count(None) != 1:
        return None
    index = variables.index(None)
    try:
        if index == 0:
            return (b * c) / d
        elif index == 1:
            return (a * d) / c
        elif index == 2:
            return (a * d) / b
        elif index == 3:
            return (b * c) / a
    except ZeroDivisionError:
        return None

def solve_linear_equation(a1, b1, a2, b2):
    denominator = a1 - a2
    if denominator == 0:
        if (b2 - b1) == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    else:
        return (b2 - b1) / denominator

def factor_sqrt(n):
    if n < 0:
        return (None, None)
    max_k = 0
    m = n
    for i in range(int(math.isqrt(n)), 0, -1):
        if n % (i*i) == 0:
            max_k = i
            m = n // (i*i)
            break
    return (max_k, m)

def decimal_to_fraction_percent(decimal_str):
    if not decimal_str:
        return None, None
    sign = 1
    if decimal_str.startswith('-'):
        sign = -1
        decimal_str = decimal_str[1:]
    if '.' in decimal_str:
        integer_part, fractional_part = decimal_str.split('.')
    else:
        integer_part = decimal_str
        fractional_part = ''
    if not integer_part:
        integer_part = '0'
    denominator = 10 ** len(fractional_part) if fractional_part else 1
    numerator = int(integer_part) * denominator
    if fractional_part:
        numerator += int(fractional_part)
    numerator *= sign
    try:
        fraction = Fraction(numerator, denominator).limit_denominator()
    except ZeroDivisionError:
        return None, None
    decimal = numerator / denominator
    percent = decimal * 100
    return fraction, percent

def percent_to_decimal_fraction(percent_str):
    if not percent_str.endswith('%'):
        return None, None
    percent_part = percent_str[:-1].strip()
    if not percent_part:
        return None, None
    if '.' in percent_part:
        integer_part, fractional_part = percent_part.split('.')
        combined = integer_part + fractional_part
        denominator = 10 ** (len(fractional_part) + 2)
        try:
            numerator = int(combined)
        except:
            return None, None
    else:
        try:
            numerator = int(percent_part)
        except:
            return None, None
        denominator = 100
    sign = 1
    if numerator < 0:
        sign = -1
        numerator = abs(numerator)
    try:
        fraction = Fraction(sign * numerator, denominator).limit_denominator()
    except ZeroDivisionError:
        return None, None
    decimal = sign * numerator / denominator
    return decimal, fraction

def main():
    while True:
        print("\nMulti-Function Calculator")
        print("1. Solve Proportions")
        print("2. Solve for X in Linear Equations")
        print("3. Factor Square Roots")
        print("4. Convert Decimals to Fractions and Percents")
        print("5. Convert Fractions to Decimals and Percents")
        print("6. Convert Percents to Decimals and Fractions")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            print("Enter the four terms of the proportion a/b = c/d. Use 'x' for the unknown.")
            terms = []
            valid = True
            for term_name in ['a', 'b', 'c', 'd']:
                term = input(f"Enter {term_name}: ").strip().lower()
                if term == 'x':
                    terms.append(None)
                else:
                    try:
                        terms.append(float(term))
                    except:
                        print("Invalid input. Please enter a number or 'x'.")
                        valid = False
                        break
            if not valid:
                continue
            if terms.count(None) != 1:
                print("Error: Exactly one term must be 'x'.")
                continue
            a, b, c, d = terms
            result = solve_proportion(a, b, c, d)
            if result is None:
                print("Error: Invalid calculation (possibly division by zero).")
            else:
                index = terms.index(None)
                term_names = ['a', 'b', 'c', 'd']
                print(f"{term_names[index]} = {result:.2f}".rstrip('0').rstrip('.') if result == int(result) else f"{term_names[index]} = {result}")

        elif choice == '2':
            try:
                a1 = float(input("Enter coefficient of x on the left side: "))
                b1 = float(input("Enter constant term on the left side: "))
                a2 = float(input("Enter coefficient of x on the right side: "))
                b2 = float(input("Enter constant term on the right side: "))
            except:
                print("Invalid input. Please enter numbers.")
                continue
            solution = solve_linear_equation(a1, b1, a2, b2)
            if isinstance(solution, str):
                print(solution)
            else:
                print(f"x = {solution:.2f}".rstrip('0').rstrip('.') if solution == int(solution) else f"x = {solution}")

        elif choice == '3':
            try:
                n = int(input("Enter a non-negative integer to factor the square root: "))
            except:
                print("Invalid input. Please enter an integer.")
                continue
            if n < 0:
                print("Error: Please enter a non-negative integer.")
                continue
            k, m = factor_sqrt(n)
            if k == 0:
                print(f"√{n} cannot be simplified further.")
            else:
                print(f"√{n} = {k}√{m}")

        elif choice == '4':
            decimal_str = input("Enter a decimal number (e.g., 0.75): ").strip()
            fraction, percent = decimal_to_fraction_percent(decimal_str)
            if fraction is None:
                print("Invalid decimal format.")
            else:
                print(f"Fraction: {fraction}")
                print(f"Percent: {percent:.2f}%")

        elif choice == '5':
            fraction_str = input("Enter a fraction (e.g., 3/4): ").strip()
            try:
                numerator, denominator = map(int, fraction_str.split('/'))
                if denominator == 0:
                    print("Error: Denominator cannot be zero.")
                    continue
                decimal = numerator / denominator
                percent = decimal * 100
            except:
                print("Invalid fraction format. Use numerator/denominator.")
                continue
            decimal_str = f"{decimal:.2f}".rstrip('0').rstrip('.') if decimal == int(decimal) else f"{decimal:.2f}"
            percent_str = f"{percent:.2f}".rstrip('0').rstrip('.') if percent == int(percent) else f"{percent:.2f}"
            print(f"Decimal: {decimal_str}")
            print(f"Percent: {percent_str}%")

        elif choice == '6':
            percent_str = input("Enter a percent (e.g., 75%): ").strip()
            decimal, fraction = percent_to_decimal_fraction(percent_str)
            if decimal is None:
                print("Invalid percent format.")
            else:
                decimal_str = f"{decimal:.2f}".rstrip('0').rstrip('.') if decimal == int(decimal) else f"{decimal:.2f}"
                print(f"Decimal: {decimal_str}")
                print(f"Fraction: {fraction}")

        elif choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()