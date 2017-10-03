# Pregunta1
## Single Responsability
No cumple este principio ya que este se basa en la cohesión, y en los códigos de ambos cines(Stark y Planeta) se puede observar que ambos tienen
una gran cantidad de funcionalidades.
## Open Close
No se cumple este principio porque no existe una clase padre de cine que permita heredar métodos y funciones que puedan
manipular cada uno de los cines, esto ocasiona que el código se tenga que modificar en caso se quieran agregar más cines.
La creación de una clase padre Cine permitiría estructurar mejor el código y no tener que modificarlo cada vez que se agreguen nuevos cines.
## Liskov Substitution
No se cumple este principio porque no hay generalización de los cines ya que se interactúa con ellos directamente.
