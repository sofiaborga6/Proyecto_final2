from ejemplo.models import Mascotas
Mascotas(nombre="Poli", tipo = "Perro", direccion="Montevideo 745", numero_registro=123123).save()
Mascotas(nombre="Roco",tipo = "Perro", direccion="Colonia 745", numero_registro=890890).save()
Mascotas(nombre="Rafiki", tipo = "Gato", direccion="Buenos Aires 745", numero_registro=345345).save()
Mascotas(nombre="Florencia", tipo = "Gato", direccion="Rosario 745", numero_registro=567567).save()
print("Se cargo con éxito los usuarios de pruebas")