# ========================================
# Sistema de Gestión de Vehículos - POO
# ========================================

class Motor:
    """Clase Motor - Composición para Vehiculos"""
    
    def __init__(self, tipo, potencia):
        self._tipo = tipo
        self._potencia = potencia
        self._encendido = False
    
    # Propiedades con @property y @setter
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor
    
    @property
    def potencia(self):
        return self._potencia
    
    @potencia.setter
    def potencia(self, valor):
        if valor > 0:
            self._potencia = valor
        else:
            print("La potencia debe ser mayor a 0")
    
    # Métodos de comportamiento
    def encender_motor(self):
        if not self._encendido:
            self._encendido = True
            return f" Motor {self._tipo} encendido ({self._potencia} HP)"
        return f" El motor ya está encendido"
    
    def detener_motor(self):
        if self._encendido:
            self._encendido = False
            return f"Motor {self._tipo} detenido"
        return f"⚠️  El motor ya está detenido"
    
    def acelerar(self):
        if self._encendido:
            return f" Motor acelerando a {self._potencia}"
        return f" Debes encender el motor primero"
    
    def diagnosticar(self):
        estado = "encendido " if self._encendido else "apagado "
        return f" Diagnóstico - Tipo: {self._tipo}, Potencia: {self._potencia} HP, Estado: {estado}"
    
    def __str__(self):
        return f"Motor[Tipo: {self._tipo}, Potencia: {self._potencia} HP]"


class Vehiculo:
    """Superclase Vehiculo"""
    
    def __init__(self, marca, modelo, anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._encendido = False
    
    # Propiedades con @property y @setter
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, valor):
        self._marca = valor
    
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor
    
    @property
    def anio(self):
        return self._anio
    
    @anio.setter
    def anio(self, valor):
        if valor > 1900:
            self._anio = valor
        else:
            print("Año inválido")
    
    # Métodos de comportamiento
    def encender(self):
        if not self._encendido:
            self._encendido = True
            return f"{self._marca} {self._modelo} encendido"
        return f"El vehículo ya está encendido"
    
    def apagar(self):
        if self._encendido:
            self._encendido = False
            return f" {self._marca} {self._modelo} apagado"
        return f" El vehículo ya está apagado"
    
    def mostrar_edad(self):
        edad = 2025 - self._anio
        return f"Este vehículo tiene {edad} años"
    
    def realizar_mantenimiento(self):
        return f"Realizando mantenimiento a {self._marca} {self._modelo}"
    
    def __str__(self):
        return f"{self._marca} {self._modelo} ({self._anio})"


class Automovil(Vehiculo):
    """Clase Automovil - Hereda de Vehiculo"""
    
    def __init__(self, marca, modelo, anio, numero_puertas, motor):
        super().__init__(marca, modelo, anio)
        self._numero_puertas = numero_puertas
        self._motor = motor
        self._maletero_abierto = False
    
    @property
    def numero_puertas(self):
        return self._numero_puertas
    
    @numero_puertas.setter
    def numero_puertas(self, valor):
        if valor in [2, 3, 4, 5]:
            self._numero_puertas = valor
        else:
            print("Número de puertas inválido")
    
    @property
    def motor(self):
        return self._motor
    
    # Métodos de comportamiento
    def abrir_maletero(self):
        if not self._maletero_abierto:
            self._maletero_abierto = True
            return f"Maletero abierto del {self._marca} {self._modelo}"
        return f"El maletero ya está abierto"
    
    def cerrar_maletero(self):
        if self._maletero_abierto:
            self._maletero_abierto = False
            return f"Maletero cerrado del {self._marca} {self._modelo}"
        return f"El maletero ya está cerrado"
    
    def tocar_claxon(self):
        return f"{self._marca} {self._modelo}"

    def activar_aire_acondicionado(self):
        if self._encendido:
            return f"Aire acondicionado activado en {self._marca} {self._modelo}"
        return f" Debes encender el vehículo primero"
    
    def __str__(self):
        return f" Automovil: {super().__str__()} | Puertas: {self._numero_puertas} | {self._motor}"


class Motocicleta(Vehiculo):
    """Clase Motocicleta - Hereda de Vehiculo"""
    
    def __init__(self, marca, modelo, anio, cilindraje, motor):
        super().__init__(marca, modelo, anio)
        self._cilindraje = cilindraje
        self._motor = motor
        self._caballito_activo = False
    
    @property
    def cilindraje(self):
        return self._cilindraje
    
    @cilindraje.setter
    def cilindraje(self, valor):
        if valor > 0:
            self._cilindraje = valor
        else:
            print("Cilindraje inválido")
    
    @property
    def motor(self):
        return self._motor
    
    # Métodos de comportamiento
    def hacer_caballito(self):
        if self._encendido and not self._caballito_activo:
            self._caballito_activo = True
            return f"🏍️  ¡Haciendo caballito con la {self._marca} {self._modelo}! ¡WOOHOO!"
        elif not self._encendido:
            return f"Debes encender la moto primero"
        return f"Ya estás haciendo un caballito"
    
    def terminar_caballito(self):
        if self._caballito_activo:
            self._caballito_activo = False
            return f"Caballito terminado con éxito"
        return f"No estás haciendo un caballito"
    
    def usar_patada_arranque(self):
        if not self._encendido:
            self._encendido = True
            return f"Patada de arranque! {self._marca} {self._modelo} encendida"
        return f"La moto ya está encendida"
    
    def activar_turbo(self):
        if self._encendido:
            return f"TURBO ACTIVADO en {self._marca} {self._modelo} {self._cilindraje}"
        return f" Debes encender la moto primero"
    
    def __str__(self):
        return f"Motocicleta: {super().__str__()} | Cilindraje: {self._cilindraje}cc | {self._motor}"


# ========================================
# PROGRAMA PRINCIPAL
# ========================================

def main():
    print("=" * 60)
    print("SISTEMA DE GESTIÓN DE VEHÍCULOS - POO EN PYTHON ")
    print("=" * 60)
    print()
    
    # Crear motores
    motor1 = Motor("V8 Gasolina", 450)
    motor2 = Motor("V6 Híbrido", 320)
    motor3 = Motor("Monocilíndrico 4T", 35)
    motor4 = Motor("Bicilíndrico Paralelo", 180)
    
    # Crear automóviles
    print("CREANDO AUTOMÓVILES...")
    print("-" * 60)
    auto1 = Automovil("Toyota", "Camry", 2023, 4, motor1)
    auto2 = Automovil("Honda", "Civic", 2022, 4, motor2)
    
    print(auto1)
    print(auto2)
    print()
    
    # Crear motocicletas
    print("CREANDO MOTOCICLETAS...")
    print("-" * 60)
    moto1 = Motocicleta("Yamaha", "YZF-R1", 2024, 998, motor3)
    moto2 = Motocicleta("Kawasaki", "Ninja 650", 2023, 649, motor4)
    
    print(moto1)
    print(moto2)
    print()
    
    # Demostración con Automóvil 1
    print(" PROBANDO AUTOMÓVIL 1: Toyota Camry")
    print("-" * 60)
    print(auto1.encender())
    print(auto1.motor.encender_motor())
    print(auto1.tocar_claxon())
    print(auto1.abrir_maletero())
    print(auto1.activar_aire_acondicionado())
    print(auto1.motor.acelerar())
    print(auto1.mostrar_edad())
    print(auto1.cerrar_maletero())
    print(auto1.motor.detener_motor())
    print(auto1.apagar())
    print()
    
    # Demostración con Automóvil 2
    print("PROBANDO AUTOMÓVIL 2: Honda Civic")
    print("-" * 60)
    print(auto2.encender())
    print(auto2.motor.encender_motor())
    print(auto2.tocar_claxon())
    print(auto2.motor.diagnosticar())
    print(auto2.realizar_mantenimiento())
    print(auto2.apagar())
    print()
    
    # Demostración con Motocicleta 1
    print(" PROBANDO MOTOCICLETA 1: Yamaha YZF-R1")
    print("-" * 60)
    print(moto1.usar_patada_arranque())
    print(moto1.motor.encender_motor())
    print(moto1.hacer_caballito())
    print(moto1.activar_turbo())
    print(moto1.terminar_caballito())
    print(moto1.mostrar_edad())
    print(moto1.motor.detener_motor())
    print(moto1.apagar())
    print()
    
    # Demostración con Motocicleta 2
    print(" PROBANDO MOTOCICLETA 2: Kawasaki Ninja 650")
    print("-" * 60)
    print(moto2.encender())
    print(moto2.motor.encender_motor())
    print(moto2.hacer_caballito())
    print(moto2.motor.acelerar())
    print(moto2.activar_turbo())
    print(moto2.terminar_caballito())
    print(moto2.motor.diagnosticar())
    print(moto2.apagar())
    print()
    
    # Resumen final
    print("=" * 60)
    print("RESUMEN DE VEHÍCULOS CREADOS")
    print("=" * 60)
    print(f"Automóvil 1: {auto1}")
    print(f"Automóvil 2: {auto2}")
    print(f"Motocicleta 1: {moto1}")
    print(f"Motocicleta 2: {moto2}")
    print("=" * 60)
    print("PROGRAMA FINALIZADO CON ÉXITO")
    print("=" * 60)


if __name__ == "__main__":
    main()