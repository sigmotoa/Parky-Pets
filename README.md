## Parky Pets
The app to control the vaccines of your loved animal friends 🐶

branch g_2 -> Animals
branch g_3 
branch g_4 

### Class Diagram

classDiagram

class Persona {
    +id
    +nombres
    +apellidos
    +documento
    +telefono
    +email
}

class Tenedor

class Veterinario {
    +numeroLicencia
    +especialidad
}

class Animal {
    +id
    +nombre
    +especie
    +raza
}

class ProductoVeterinario {
    +id
    +nombre
    +tipo
}

class AplicacionProducto {
    +id
    +fechaAplicacion
    +fechaProxima
    +observaciones
}

Persona <|-- Tenedor
Persona <|-- Veterinario

Tenedor "1" --> "0..*" Animal

Animal "1" --> "0..*" AplicacionProducto

ProductoVeterinario "1" --> "0..*" AplicacionProducto

Veterinario "1" --> "0..*" AplicacionProducto