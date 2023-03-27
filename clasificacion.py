productos = []  # lista para almacenar los datos de los productos

# pedir al usuario los datos de los productos
while True:
    nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if nombre == 'fin':
        break
    cantidad = float(input("Ingrese la cantidad de unidades del producto: "))
    costo_unitario = float(input("Ingrese el costo unitario del producto: "))
    productos.append([nombre, cantidad, costo_unitario])  # añadir los datos a la lista de productos

# calcular el valor total de cada producto y el valor total del inventario
valor_total_inventario = 0
for producto in productos:
    valor_total_producto = producto[1] * producto[2]  # cantidad * costo unitario
    valor_total_inventario += valor_total_producto
    producto.append(valor_total_producto)  # añadir el valor total del producto a la lista de datos del producto

# ordenar los productos de forma descendente según su valor total
productos.sort(key=lambda x: x[3], reverse=True)

# calcular el porcentaje acumulado del valor total del inventario y asignar la clasificación A, B o C a cada producto
porcentaje_acumulado = 0
for i, producto in enumerate(productos):
    porcentaje_acumulado += producto[3] / valor_total_inventario
    if porcentaje_acumulado <= 0.8:
        clasificacion = 'A'
    elif porcentaje_acumulado <= 0.95:
        clasificacion = 'B'
    else:
        clasificacion = 'C'
    productos[i] = producto + [clasificacion]  # añadir la clasificación a la lista de datos del producto

# imprimir la tabla de ejecución y la lista de productos clasificados
print("\nTabla de ejecución:")
print(f"{'Producto':<15} {'Cantidad':<10} {'Costo unitario':<15} {'Valor total':<15}")
for producto in productos:
    print(f"{producto[0]:<15} {producto[1]:<10.2f} {producto[2]:<15.2f} {producto[3]:<15.2f}")

print("\nLista de productos clasificados:")
print(f"{'Producto':<15} {'Clasificación':<15}")
for producto in productos:
    print(f"{producto[0]:<15} {producto[4]:<15}")
