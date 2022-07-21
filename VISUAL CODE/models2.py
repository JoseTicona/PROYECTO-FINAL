class Producto:
    def __init__(self, codigo, nombre, detalle, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.detalle = detalle
        self.precio = precio

    def __str__(self):
        return "{};{};{};{}\n".format(
            self.codigo, self.nombre, self.detalle, self.precio
        )

class Cliente:
    # atributos
    def __init__(self, dni, nombres_apellidos, direccion, telefono, email):
        self.dni = dni
        self.nombres_apellidos = nombres_apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    # metodos
    def __str__(self):
        return "{};{};{};{};{}\n".format(
            self.dni, self.nombres_apellidos, self.direccion, self.telefono, self.email
        )