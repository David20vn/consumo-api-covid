from api_handler import get_api_data
from ui import display_ui

def main():
    # Pedir al usuario el límite de registros
    limite_registros = int(input("Digite el límite de registros a extraer: "))

    # Pedir al usuario el nombre del departamento (opcional)
    nombre_departamento = input("Digite el nombre del departamento a filtrar (o presione Enter para no filtrar): ")
    
    # Obtener los datos de la API usando la función de api_handler
    df = get_api_data(limite_registros, nombre_departamento)
    
    # Llamar a la UI para mostrar los datos
    display_ui(df)

# main.py

from api_handler import get_api_data
from ui import display_ui

def main():
    # Pedir al usuario el límite de registros
    try:
        limite_registros = int(input("Digite el límite de registros a extraer: "))
    except ValueError:
        print("Por favor, ingrese un número válido para el límite de registros.")
        return

    # Pedir al usuario el nombre del departamento (opcional)
    nombre_departamento = input("Digite el nombre del departamento a filtrar (o presione Enter para no filtrar): ")
    
    # Obtener los datos de la API usando la función de api_handler
    df = get_api_data(limite_registros, nombre_departamento)
    
    # Mostrar por consola las columnas disponibles (opcional)
    print("Columnas disponibles:", list(df.columns))
    
    # Llamar a la UI para mostrar los datos
    display_ui(df)

main()

