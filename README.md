Ya tenemos montado el núcleo del simulador en la carpeta Entidades.
El sistema separa bien las clases para que cada uno pueda modificar lo que quiera en
Git sin romper nada; ahora mismo, Bono hereda correctamente 
de Activo, y tanto Inversor como Transaccion ya gestionan la lógica 
base con datetime para que no se pierda el rastro de las operaciones. 
La idea era dejar una base limpia donde las estrategias y las alertas 
de precio funcionen de forma independiente antes de meterle más peso al código.

Lo siguiente es mejorar a la clase Cartera. Queremos usar sobrecarga de 
operadores para que sumar o comparar carteras sea tan fácil como un p1 + p2, 
y dejar listas las excepciones para cuando alguien intente meter importes 
negativos o activos que no existen. Básicamente, pasar de tener piezas 
sueltas a un sistema robusto que aguante cualquier burrada que intente 
hacer el usuario en el simulador.