# Simulador de Bolsa Educativa - Grupo B13

Este es el proyecto final de programación del Grupo B13. Es un simulador de bolsa desarrollado en Python que sirve para gestionar carteras de inversión, comprar y vender activos, y generar reportes. Hemos aplicado los principios de la Programación Orientada a Objetos y una arquitectura en capas para estructurar el código.

## Estructura del proyecto

El código está dividido en 4 capas principales para separar la lógica de la interfaz:

- Entidades: Donde están las clases base como Inversor, Cartera, Activo y Bono (haciendo uso de herencia y clases abstractas). Aquí también hemos implementado la sobrecarga de operadores en la clase Cartera para poder sumar o comparar saldos.
- Servicios: Contiene toda la lógica de negocio. Se encarga de hacer las comprobaciones, como ver si hay saldo suficiente o si el activo existe en el mercado. Si algo falla, lanza nuestras propias excepciones personalizadas.
