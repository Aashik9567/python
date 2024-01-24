# Define a function to check if a character is an operator
def is_operator(char):
    operators = "+-*/^"
    return char in operators

# Define a function to get the precedence of an operator
def get_precedence(char):
    if char == "+" or char == "-":
        return 1
    elif char == "*" or char == "/":
        return 2
    elif char == "^":
        return 3
    else:
        return -1

# Define the main function to convert infix to postfix
def infix_to_postfix(infix):
    postfix = ""
    stack = []
    for char in infix:
        if char == "(":
            stack.append(char)
        elif char == ")":
            while len(stack) > 0 and stack[-1] != "(":
                postfix += stack.pop()
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
        elif not is_operator(char):
            postfix += char
        else:
            while len(stack) > 0 and get_precedence(char) <= get_precedence(stack[-1]):
                postfix += stack.pop()
            stack.append(char)
    while len(stack) > 0:
        postfix += stack.pop()
    return postfix

# Test the function
infix=input("Enter infix expression-->")
postfix_expression = infix_to_postfix(infix)
print(f"Infix expression: {infix}")
print(f"Postfix expression: {postfix_expression}")
