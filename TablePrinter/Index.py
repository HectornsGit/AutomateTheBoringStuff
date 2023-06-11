tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def PrintTable(data):
    # Mira cuantas columnas hay y por cada una de ellas guarda guarda en una lista de anchos un cero.
    colWidths = [0] * len(data)

    # Comprueba cual es la string más larga añadiendo el número de caracteres que la componen.
    for index in range(len(data)):
        for string in data[index]:
            if len(string) > colWidths[index]:
                colWidths[index] = len(string)

    # Itera sobre la información de la tabla.
    for row in range(len(data)):
        # variable donde guardamos cada fila que formará nuestra tabla.
        new_row = ""
        # Iteramos cada fila de nuestros datos y justificamos a la izquierda
        # usando la longitud de la string más larga como argumento.
        for string in range(len(data[row])):
            new_row += " " + data[row][string].ljust(colWidths[row])
        print(new_row)


PrintTable(tableData)
