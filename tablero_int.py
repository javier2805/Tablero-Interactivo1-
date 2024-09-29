import streamlit as st

# Título principal
st.title("Tablero Interactivo")
st.sidebar.title("Ejercicios")

# Menú en la barra lateral para seleccionar la función
opcion = st.sidebar.selectbox("Escoge el ejercicio de tu agrado:", 
                              ["Inicio", "Saludo Simple", "Suma de dos números", "Área de un triángulo", 
                               "Calcular Precio Final", "Suma de una Lista", "Producto Total", 
                               "Números Pares e Impares", "Multiplicación de Números", 
                               "Información Personal", "Calculadora Flexible"])

# Mostrar mensaje con el apartado escogido
st.write(f"Haz escogido {opcion}")

# Sección "Inicio"
if opcion == "Inicio":
    st.write("""
    En esta aplicación, puedes interactuar con diferentes ejercicios que te permiten realizar 
    operaciones básicas como la suma de números, calcular el área de un triángulo, manipular listas de números, 
    y mucho más.
    
    Usa la barra lateral para seleccionar el ejercicio que deseas realizar y sigue las instrucciones en pantalla.
    """)

# Función de saludo simple
def saludar(nombre):
    st.write(f"Hola, {nombre}! Bienvenid@.")
if opcion == "Saludo Simple":
    veces = st.number_input("¿Cuántas veces quieres ingresar un nombre?", min_value=1, step=1)
    for _ in range(veces):
        nombre_usuario = st.text_input(f"Introduce tu nombre (intento {_+1} de {veces}):", key=f"nombre_{_}")
        if nombre_usuario:
            saludar(nombre_usuario)

# Función de suma de dos números
if opcion == "Suma de dos números":
    n1 = st.number_input("Ingresa el primer número", step=1.0, key="n1")
    n2 = st.number_input("Ingresa el segundo número", step=1.0, key="n2")
    if st.button("Sumar"):
        st.write(f"El resultado de la suma es: {n1 + n2}")

# Función para calcular el área de un triángulo
if opcion == "Área de un triángulo":
    base = st.number_input("Ingresa la base", step=0.1)
    altura = st.number_input("Ingresa la altura", step=0.1)
    if st.button("Calcular área"):
        area = base * altura / 2
        st.write(f"El área del triángulo es: {area:.2f}")

# Función para calcular el precio final con descuento e impuesto
if opcion == "Calcular Precio Final":
    p_original = st.number_input("Ingrese el precio original del producto", step=0.01)
    desc = st.number_input("Ingrese el descuento (%)", value=10.0, step=0.1)
    impuesto = st.number_input("Ingrese el impuesto (%)", value=16.0, step=0.1)
    if st.button("Calcular precio final"):
        precio_con_descuento = p_original * (1 - desc / 100)
        p_final = precio_con_descuento * (1 + impuesto / 100)
        st.write(f"El precio final es: ${p_final:.2f}")

# Función para sumar una lista de números
if opcion == "Suma de una Lista":
    numeros = st.text_input("Ingresa una lista de números separados por comas")
    if st.button("Sumar lista"):
        if numeros:
            lista_numeros = [float(num) for num in numeros.split(",")]
            suma = sum(lista_numeros)
            st.write(f"La suma de los números es: {suma}")

# Función para calcular el producto total de una compra
if opcion == "Producto Total":
    nombre_producto = st.text_input("Ingresa el nombre del producto")
    cantidad = st.number_input("Ingresa la cantidad", value=1, step=1)
    precio_unidad = st.number_input("Ingrese el precio unitario", value=10.0, step=0.1)
    if st.button("Calcular precio total"):
        precio_total = cantidad * precio_unidad
        st.write(f"Usted pagará ${precio_total:.2f} por comprar {cantidad} {nombre_producto}")

# Función para separar números pares e impares
if opcion == "Números Pares e Impares":
    numeros = st.text_input("Ingresa una lista de números separados por comas")
    if st.button("Separar pares e impares"):
        if numeros:
            lista_numeros = [int(num) for num in numeros.split(",")]
            pares = [num for num in lista_numeros if num % 2 == 0]
            impares = [num for num in lista_numeros if num % 2 != 0]
            st.write(f"Números pares: {pares}")
            st.write(f"Números impares: {impares}")

# Función para multiplicar todos los números
if opcion == "Multiplicación de Números":
    numeros = st.text_input("Ingresa los números separados por espacios")
    if st.button("Multiplicar"):
        if numeros:
            lista_numeros = [float(num) for num in numeros.split()]
            resultado = 1
            for num in lista_numeros:
                resultado *= num
            st.write(f"El resultado de multiplicar todos los números es: {resultado:.2f}")

# Función para ingresar información personal
if opcion == "Información Personal":
    datos = {}
    while True:
        clave = st.text_input("Ingrese el nombre del dato (o deje en blanco para terminar)", key=f"clave_{len(datos)}")
        if not clave:
            break
        valor = st.text_input(f"Ingrese el valor para {clave}", key=f"valor_{len(datos)}")
        datos[clave] = valor
    if datos:
        st.write("Información ingresada:")
        for clave, valor in datos.items():
            st.write(f"{clave}: {valor}")

# Calculadora flexible
if opcion == "Calculadora Flexible":
    num1 = st.number_input("Ingrese el primer número", step=0.1, key="num1")
    num2 = st.number_input("Ingrese el segundo número", step=0.1, key="num2")
    operacion = st.selectbox("Elige la operación", ["Suma", "Resta", "Multiplicación", "División"])

    if st.button("Calcular"):
        if operacion == "Suma":
            resultado = num1 + num2
        elif operacion == "Resta":
            resultado = num1 - num2
        elif operacion == "Multiplicación":
            resultado = num1 * num2
        elif operacion == "División":
            resultado = num1 / num2 if num2 != 0 else "Error: División por cero"
        st.write(f"Resultado: {resultado}")
