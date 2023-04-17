# Importar el modulo creado anteriormente #
import EjercicioModulo as em

# Crear el objeto 'coche_1' al instanciar la clase 'Coche'
coche_1 = em.Coche('Figo','gris','gasolina',4)
# Mediante print mostrar las caracteristicas del coche #
coche_1.mostrar_caracteristicas()
# Calcular la media de 3 notas y mostrar el resultado con print #
calif_1 = int(input('Introduce tu calificación 1: '))
calif_2 = int(input('Introduce tu calificación 2: '))
calif_3 = int(input('Introduce tu calificación 3: '))
media = em.media(calif_1,calif_2,calif_3)
print(f'La media de calificaciones es {media:.2f}')