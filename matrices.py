import flet as ft
import numpy as np

matriz_coef = []
vector_ind = []

def gauss_jordan(matriz_coef, vector_ind):
    num_filas = matriz_coef.shape[0]

    # Crear la matriz aumentada
    matriz_aumentada = np.zeros(shape=(num_filas, num_filas + 1))
    matriz_aumentada[:num_filas, :num_filas] = matriz_coef
    matriz_aumentada[:, num_filas] = vector_ind.flatten()

    # Guardar la matriz aumentada original
    matriz_aumentada_original = matriz_aumentada.copy()

    # Resolver el sistema de ecuaciones lineales por el método de Gauss-Jordan
    matriz_escalona_paso_a_paso = []
    for i in range(num_filas):
        columna_pivote = i
        while columna_pivote < num_filas and matriz_aumentada[columna_pivote][i] == 0:
            columna_pivote += 1
        if columna_pivote == num_filas:
            return None
        if columna_pivote != i:
            i_aux = np.copy(matriz_aumentada[i])
            matriz_aumentada[i] = matriz_aumentada[columna_pivote]
            matriz_aumentada[columna_pivote] = i_aux
        for fila_inferior in range(i + 1, num_filas):
            factor = -matriz_aumentada[fila_inferior, columna_pivote] / matriz_aumentada[i, columna_pivote]
            matriz_aumentada[fila_inferior] += factor * matriz_aumentada[i]
        matriz_aumentada[i] /= matriz_aumentada[i, i]

    vector_solucion = matriz_aumentada[:, num_filas]

    resultado = (matriz_aumentada_original, matriz_escalona_paso_a_paso, vector_solucion)
    # Devolver los resultados
    return resultado

def cambio_aleatorio(lista_aleatoria, boton_agregar, campo_texto_ingresar2, boton_ejecutar, page):
    """
    This function handles the event when the user selects an option from the 'lista_aleatoria' dropdown.
    It disables or enables certain buttons and fields based on the selected option.
    """
    if str(lista_aleatoria.value) == "aleatorio":
        boton_agregar.disabled = True
        campo_texto_ingresar2.disabled = True
        boton_ejecutar.disabled = False
        page.update()
    else:
        boton_agregar.disabled = False
        campo_texto_ingresar2.disabled = False
        boton_ejecutar.disabled = False
        page.update()


def ejecutar(lista_aleatoria, lista_dimension, page,area_texto,campo_texto_ingresar2,boton_ejecutar, boton_agregar):
    resultado = None
    # Validación para determinar si se está trabajando en modo aleatorio o manual
    if lista_aleatoria.value == "aleatorio":
        # Crear matrices de coeficientes y vectores independientes aleatorios
        if lista_dimension.value == "2X2":
            a = np.random.randint(1, 9, (2, 2)).astype(float)
            b = np.random.randint(1, 9, (2))
        elif lista_dimension.value == "3X3":
            a = np.random.randint(1, 9, (3, 3)).astype(float)
            b = np.random.randint(1, 9, (3))
        elif lista_dimension.value == "4X4":
            a = np.random.randint(1, 9, (4, 4)).astype(float)
            b = np.random.randint(1, 9, (4))
        elif lista_dimension.value == "5X5":
            a = np.random.randint(1, 9, (5, 5)).astype(float)
            b = np.random.randint(1, 9, (5))
        elif lista_dimension.value == "6X6":
            a = np.random.randint(1, 9, (6, 6)).astype(float)
            b = np.random.randint(1, 9, (6))
    # Resolver el sistema de ecuaciones lineales utilizando el método de Gauss-Jordan
        resultado = gauss_jordan(a, b)
        update_text(resultado, area_texto, page)

    else:
            
        num_filas = int(lista_dimension.value.split("X")[0])
        matriz_valores = []
        for i in range(num_filas):
            fila = campo_texto_ingresar2.value.split(",")
            fila_valores = [float(valor) for valor in fila.split(",")]
            matriz_valores.append(fila_valores)
            campo_texto_ingresar2.value = ""  # Limpiar el campo de texto para la próxima fila

        matriz_coeficiente = np.array([fila[:-1] for fila in matriz_valores])
        vector_independiente = np.array([fila[-1] for fila in matriz_valores])
            
        resultado = gauss_jordan(matriz_coeficiente, vector_independiente)
        update_text(resultado, area_texto, page)




def update_text(resultado, area_texto, page):
    matriz_aumentada_original, matriz_escalona_paso_a_paso, vector_solucion = resultado
    
    area_texto.value = ""
    
    area_texto.value += "Matriz aumentada original:\n"
    for fila in matriz_aumentada_original:
        area_texto.value += f"[{', '.join(map(lambda x: f"{x:.1f}", fila))}]\n"
        area_texto.value += "\n"
    
    for i, matriz in enumerate(matriz_escalona_paso_a_paso):
        area_texto.value += f"Matriz escalonada después del paso #{i+1}\n"
        for fila in matriz:
            area_texto.value += f"[{', '.join(map(lambda x: f"{x:.1f}", fila))}]\n"
        area_texto.value += "\n"
    
    area_texto.value += "Vector solución:\n"
    for i, valor in enumerate(vector_solucion):
        area_texto.value += f"x{i+1} = {valor:.1f}\n"
    
    page.update()
   


def main2(page:ft.Page):
    page.title="Gauss-Jordan"
    page.window_width=600
    page.window_height=600
    page.padding=0
    
    lista_aleatoria = ft.Dropdown(
        label="Elige el modo",
        width=150,
        options=[
            ft.dropdown.Option("aleatorio"),
            ft.dropdown.Option("manual"),
        ],
        on_change = lambda e: cambio_aleatorio(lista_aleatoria, boton_agregar, campo_texto_ingresar2, boton_ejecutar, page)
    )

    lista_dimension = ft.Dropdown(
        label="Elige la dimension",
        width=150,
        options=[
            ft.dropdown.Option("2X2"),
            ft.dropdown.Option("3X3"),
            ft.dropdown.Option("4X4"),
            ft.dropdown.Option("5X5"),
            ft.dropdown.Option("6X6"),
        ]
    )

    campo_texto_ingresar2 = ft.TextField(
        label="Ingresa las filas",
        text_align=ft.TextAlign.LEFT,
        width=150
    )

    area_texto = ft.TextField(
        label="Resultados",
        width=450,
        height=270,
        multiline=True,
        read_only=True
    )
    
    boton_ejecutar = ft.ElevatedButton(
        text="Ejecutar",
        width=100,
        
        on_click = lambda e: ejecutar(lista_aleatoria, lista_dimension, page, area_texto, campo_texto_ingresar2,boton_ejecutar, boton_agregar)
    )
    
    boton_agregar = ft.ElevatedButton(
    text="Agregar",
    width=100,
    on_click=lambda e: ejecutar(lista_aleatoria, lista_dimension, page, area_texto, campo_texto_ingresar2,boton_ejecutar, boton_agregar)
    )
    
    # Agregar los controles a la página
    page.add(
    lista_aleatoria,
    lista_dimension,
    campo_texto_ingresar2,
    area_texto,
    boton_agregar,
    boton_ejecutar
    )
    



    # También puedes agregar otros elementos o lógica según tus necesidades
