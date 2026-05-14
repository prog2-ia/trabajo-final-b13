# Simulador de Bolsa Educativa - Grupo B13

Este es el proyecto final de programación del Grupo B13. Es un simulador de bolsa desarrollado en Python que sirve para gestionar carteras de inversión, comprar y vender activos, y generar reportes. Hemos aplicado los principios de la Programación Orientada a Objetos y una arquitectura en capas para estructurar el código.

## Estructura del proyecto

El código está dividido en 4 capas principales para separar la lógica de la interfaz:

- Entidades: Donde están las clases base como Inversor, Cartera, Activo y Bono (haciendo uso de herencia y clases abstractas). Aquí también hemos implementado la sobrecarga de operadores en la clase Cartera para poder sumar o comparar saldos.
- Servicios: Contiene toda la lógica de negocio. Se encarga de hacer las comprobaciones, como ver si hay saldo suficiente o si el activo existe en el mercado. Si algo falla, lanza nuestras propias excepciones personalizadas.
- Persistencia: Se encarga de leer y guardar los datos. Usamos archivos de texto plano (.txt) para generar los reportes y ficheros binarios (.pkl) para guardar el estado completo del programa.
- UI: Es el menú de la consola. Su única función es recoger los datos del usuario, validar que los formatos sean correctos y pasárselos a los servicios.

## Cómo ejecutar y probar el programa

Para arrancar el simulador, colócate en la carpeta del proyecto y ejecuta el archivo principal desde la terminal:

`python main.py`

No se necesitan instalar librerías externas (el requirements.txt está vacío porque solo usamos librerías estándar de Python).

Al arrancar, el programa carga automáticamente unos datos de prueba: un inversor (ID: 123) que tiene 1000 euros en su cartera, y un activo en el mercado (Ticker: AAPL) que cuesta 150 euros. 

Para comprobar que todas las partes del código funcionan, se pueden seguir estos pasos en el menú principal:

1. Probar el control de errores: Intenta comprar el activo AAPL usando el ID 123, pero indica una cantidad de 10. Como 10 acciones cuestan 1500 euros y el inversor solo tiene 1000, el programa bloqueará la operación y saltará la excepción de saldo insuficiente que hemos programado.
2. Hacer una compra válida: Vuelve a seleccionar la opción de comprar, pero esta vez pon una cantidad de 2. El sistema hará la compra y descontará 300 euros del saldo del inversor.
3. Probar el guardado de ficheros: Usa la opción 2 del menú para generar un reporte del usuario 123. Esto creará un archivo .txt en la carpeta data. Luego usa la opción 3 para guardar la partida, lo que creará el archivo binario .pkl en la misma carpeta.7



Participantes del proyecto:
Daniel Fernandez García y Juan Herraiz López

### Aclaración 
Juan Herraiz López no tiene los commits reales realizados ya que hubo un error con el correo de pycharmp y a la hora de hacer los commits el trabajo en githbub se actualizaba pero no se le atribuian los commits, por ello tiene casi todos su commits al final.

