
rd = None
a = 10
b = 0
try:

    rd = a/b
except ZeroDivisionError as e:
    print(f'ERROR {e}')

except TypeError as e:
    print(f'Error {e}')

except Exception as e:
    print(f'Error {e}')

print(f'RESULTADO {rd}')


# se pueden manejar excepciones mas especificas