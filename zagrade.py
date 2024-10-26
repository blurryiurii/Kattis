def remove_brackets(expression):
    def is_valid(expr):
        stack = []
        for char in expr:
            if char == '(':
                stack.append('(')
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    def generate_expressions(expr, index):
        if index == len(expr):
            if is_valid(expr):
                results.add(expr)
            return

        if expr[index] == '(':
            # Try removing the bracket
            generate_expressions(expr[:index] + expr[index+1:], index)
            # Try keeping the bracket
            generate_expressions(expr, index + 1)
        else:
            generate_expressions(expr, index + 1)

    results = set()
    generate_expressions(expression, 0)
    return list(results)

# Input
input_expression = input()

# Call the function and print the results
expressions = remove_brackets(input_expression)
for exp in expressions:
    print(exp)
