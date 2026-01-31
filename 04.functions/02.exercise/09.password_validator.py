def digits(password):
    digits_counter = 0
    for digit in password:
        if digit.isdigit():
            digits_counter += 1

    if digits_counter < 2:
        digits_result = 'Password must have at least 2 digits'
        return digits_result
    return None

def letters(password):
    if 6 <= len(password) <= 10:
        return None
    else:
        letter_result = 'Password must be between 6 and 10 characters'
        return letter_result

def symbols(password):
    for symbol in password:
        if not symbol.isalnum():
            symbol_result = 'Password must consist only of letters and digits'
            return symbol_result
    return None



def password_validator(password):
    return digits(password), letters(password), symbols(password)



password_ = input()
password_symbol_by_symbol = []
for symbol_ in password_:
    password_symbol_by_symbol.append(symbol_)
digits_result_, letters_result_, symbols_result_ = password_validator(password_symbol_by_symbol)

if digits_result_ is None and letters_result_ is None and symbols_result_ is None:
    print("Password is valid")
else:
    if letters_result_ is not None:
        print(letters_result_)
    if symbols_result_ is not None:
        print(symbols_result_)
    if digits_result_ is not None:
        print(digits_result_)