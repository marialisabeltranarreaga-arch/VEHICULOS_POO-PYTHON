# Sistema de Gestión de Vehículos - POO en Python

## Descripción
Sistema orientado a objetos que implementa herencia, encapsulamiento, composición y métodos de comportamiento para gestionar vehículos (automóviles y motocicletas).

## Conceptos Aplicados
- ✅ **Encapsulamiento**: Atributos privados con `@property` y `@setter`
- ✅ **Herencia**: Clases `Automovil` y `Motocicleta` heredan de `Vehiculo`
- ✅ **Composición**: Uso de la clase `Motor` dentro de vehículos
- ✅ **Polimorfismo**: Sobrescritura del método `__str__()`
- ✅ **Métodos de Comportamiento**: Múltiples métodos por clase

## Diagrama UML
```mermaid
classDiagram
    class Motor {
        -_tipo: str
        -_potencia: int
        -_encendido: bool
        +tipo: property
        +potencia: property
        +encender_motor() str
        +detener_motor() str
        +acelerar() str
        +diagnosticar() str
        +__str__() str
    }
    
    class Vehiculo {
        -_marca: str
        -_modelo: str
        -_anio: int
        -_encendido: bool
        +marca: property
        +modelo: property
        +anio: property
        +encender() str
        +apagar() str
        +mostrar_edad() str
        +realizar_mantenimiento() str
        +__str__() str
    }
    
    class Automovil {
        -_numero_puertas: int
        -_motor: Motor
        -_maletero_abierto: bool
        +numero_puertas: property
        +motor: property
        +abrir_maletero() str
        +cerrar_maletero() str
        +tocar_claxon() str
        +activar_aire_acondicionado() str
        +__str__() str
    }
    
    class Motocicleta {
        -_cilindraje: int
        -_motor: Motor
        -_caballito_activo: bool
        +cilindraje: property
        +motor: property
        +hacer_caballito() str
        +terminar_caballito() str
        +usar_patada_arranque() str
        +activar_turbo() str
        +__str__() str
    }
    
    Vehiculo <|-- Automovil : Herencia
    Vehiculo <|-- Motocicleta : Herencia
    Automovil *-- Motor : Composición
    Motocicleta *-- Motor : Composición
```

## Estructura de Clases

### Motor (Composición)
- **Atributos**: tipo, potencia
- **Métodos**: encender_motor(), detener_motor(), acelerar(), diagnosticar()

### Vehiculo (Superclase)
- **Atributos**: marca, modelo, año
- **Métodos**: encender(), apagar(), mostrar_edad(), realizar_mantenimiento()

### Automovil (Hereda de Vehiculo)
- **Atributo adicional**: número_puertas
- **Composición**: Motor
- **Métodos**: abrir_maletero(), tocar_claxon(), activar_aire_acondicionado()

### Motocicleta (Hereda de Vehiculo)
- **Atributo adicional**: cilindraje
- **Composición**: Motor
- **Métodos**: hacer_caballito(), usar_patada_arranque(), activar_turbo()

##  Ejecución
```bash
python VEHICULOS_POO.PY
```

pa- `README.md` - Documentación del proyecto
- `Captura.PNG` - Captura de pantalla de la ejecución
