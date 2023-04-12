def safe_calculate(func):
    def wrapper(expression):
        try:
            result = func(expression)
        except Exception as error:
            result = f"Error: {(error)}"
        return result
    return wrapper

@safe_calculate
def calculate(expression):
    return eval(expression)

print(calculate('789+15'))
print(calculate('18-4'))
print(calculate('7/0'))
print(calculate('256*4'))