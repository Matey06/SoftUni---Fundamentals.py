import re

number_of_barcodes = int(input())

pattern = r'^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$'

for current_barcode in range(number_of_barcodes):
    barcode = input()
    match = re.search(pattern, barcode)

    if match:
        text = match.group(1)
        product_group = ''
        for char in text:
            if char.isdigit():
                product_group += char
        if not product_group:
            product_group = '00'

        print(f'Product group: {product_group}')

    else:
        print('Invalid barcode')
