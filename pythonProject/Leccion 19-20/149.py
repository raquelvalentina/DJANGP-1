# menejo de errores en python
# tips de errores
# bloque try, except, tipo de error que se quiere capturar ---> exception
from ppo import same
try:
    10/0
except ZeroDivisionError as e:
    print(f'ERROR: {e}')

except Exception as e:
    print(f'ERROR{e}')

print(f'RESULTADO {rd}')
