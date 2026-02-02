def data_filter(data_type, random_data):
    if data_type == 'string':
        return string(random_data)
    elif data_type == "int":
        return integer(random_data)
    elif data_type == "real":
        return floating(random_data)
    return None


def string(random_data):
    result = f'${random_data}$'
    return result


def integer(random_data):
    random_data = int(random_data)
    result = random_data * 2
    return result

def floating(random_data):
    random_data = float(random_data)
    result = f'{(random_data * 1.5):.2f}'
    return result


data_type_ = input()
random_data_ = input()
result_ = data_filter(data_type_, random_data_)
print(result_)