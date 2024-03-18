# Ejemplo de probabilidad bayesiana aplicado a un test diagnóstico

Basado en el ejemplo propuesto aquí: <https://www.ugr.es/~jsalinas/bayes.htm>

Definimos los siguientes eventos:

- $Diabético$: El paciente tiene diabetes.
- $\neg Diabético$: El paciente no tiene diabetes.
- $Positivo$: El test es positivo.
- $\neg Positivo$: El test es negativo.

Si seleccionamos una persona al azar, la probabilidad de que sea diabética es 0,03. Obviamente la probabilidad de que no lo sea es 0,97.

$$ P(Diabético) = 0,03 \quad;\quad P(\neg Diabético) = 0,97 $$

Si no disponemos de información adicional nada más podemos decir, pero supongamos que al realizar un análisis de sangre los niveles de glucosa son superiores a 1.000 mg/l, lo que ocurre en el 95% de los diabéticos y sólo en un 2% de las personas sanas.

$$ P(Positivo|Diabético) = 0,95 \quad;\quad P(Positivo|\neg Diabético) = 0,02 $$

Partiendo de estos datos sabemos tambien las probabilidades complementarias:

- La probabilidad de que el paciente no tenga diabetes. Esta probabilidad es la complementaria de la probabilidad de que el paciente tenga diabetes.

$$ P(\neg Diabético) = 1 - P(Diabético) = 1 - 0,03= 0,97 $$

- La probabilidad de que el test sea positivo dado que el paciente no tiene diabetes es la probabilidad de un falso positivo, que es la inversa de la especificidad.

$$ P(Positivo|\neg Diabético) = 1 - P(Negativo|\neg Diabético) = 1 - 0,98= 0,02 $$

¿Cuál será ahora la probabilidad de que esa persona sea diabética?

La respuesta que nos dá el teorema de Bayes es que esa información adicional hace que la probabilidad sea ahora 0,595.

$$ P (Diabético|Positivo) = \frac{P (Positiva|Diabético) \times P (Diabético)}{P(Positivo)} $$

$$ P (Diabético|Positivo) = \frac{0,95 \times 0,03}{P(Positivo)} $$

La probabilidad de que el test sea positivo en general es la suma de las probabilidades de que el test sea positivo y el paciente tenga diabetes, y de que el test sea positivo y el paciente no tenga diabetes. O sea: la probabilidad de que el test sea positivo es la suma de la probabilidad de un verdadero positivo y de un falso positivo.

$$ P(Positivo) = P(Positivo\cap Diabético) + P(Positivo\cap \neg Diabético) $$

La probabilidad de un verdadero positivo es la probabilidad de que el paciente tenga diabetes y el test sea positivo , que es la probabilidad de que el paciente tenga diabetes por la probabilidad de que el test sea positivo dado que el paciente tiene diabetes.

$$ P(Verdadero\ Positivo) = P(Positivo\cap Diabético) = P(Positivo|Diabético) \times P(Diabético) $$

Lo mismo aplica de modo análogo a la probabilidad de un falso positivo: es la probabilidad de que el paciente no tenga diabetes y el test sea positivo, que es la probabilidad de que el paciente no tenga diabetes por la probabilidad de que el test sea positivo dado que el paciente no tiene diabetes.

$$ P(Falso\ Positivo) = P(Positivo\cap \neg Diabético) = P(Positivo|\neg Diabético) \times P(\neg Diabético) $$

Por tanto, la probabilidad de que el test sea positivo es:

$$ P(Positivo) = P(Positivo\cap Diabético) + P(Positivo\cap \neg Diabético) = P(Positivo|Diabético) \times P(Diabético) + P(Positivo|\neg Diabético) \times P(\neg Diabético) $$

que viene a ser el [teorema de probabilidad total](https://es.wikipedia.org/wiki/Teorema_de_la_probabilidad_total).

Así que podemos desarrollar la fórmula de Bayes de la siguiente manera:

$$
P(Diabético|Positivo) = \frac{P (Positivo|Diabético)\times P(Diabético)} {P(Positivo|Diabético)\times P(Diabético) + P(Positivo|\neg Diabético) \times P(\neg Diabético)}
\\ \ \\= \frac{0,95 \times 0,03}{0,95 \times 0,03 + 0.02*0.97} \approx 0.595
$$

Vemos así que la información proporcionada por el análisis de sangre hace pasar la probabilidad inicial de padecer diabetes de 0,03 a 0,595.

Evidentemente si la prueba del análisis de sangre hubiese sido negativa, esta información modificaría las probabilidades en sentido contrario. En este caso la probabilidad de padecer diabetes se reduciría a 0,0016.

## Material complementario

- [Matemáticas con Juan - Ejercicio similar resuelto](https://www.youtube.com/watch?v=n11NDXIIcLI)
- [Veritasium - The Bayesian Trap](https://www.youtube.com/watch?v=R13BD8qKeTg) ([Versión doblada al español](https://www.youtube.com/watch?v=D7KKlC0LOyw))
- [3Blue1Brown - The medical test paradox, and redesigning Bayes' rule](https://www.youtube.com/watch?v=lG4VkPoG3ko)
