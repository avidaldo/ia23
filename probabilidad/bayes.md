# Probabilidad Bayesiana

El Teorema de Bayes es una fórmula que describe cómo actualizar nuestras creencias sobre una hipótesis en función de la evidencia. Se utiliza en una amplia variedad de contextos, incluyendo la detección de spam en los correos electrónicos.

## Teorema de Bayes

El Teorema de Bayes se puede expresar de la siguiente manera:

$$ P(A|B) = \frac{P(B|A) \times P(A)}{P(B)} $$

donde:

- $P(A)$ y $P(B)$ son las probabilidades *a priori* de dichos eventos. Las probabilidades de que dichos eventos sucedan sin estar condicionados por ningún otro evento.
- $P(A|B)$ es la probabilidad condicional o *a posteriori* de la hipótesis $A$ dado el evento $B$, o sea: la probabilidad de que A se dé dado que B se ha dado.

## Ejemplo del teorema de Bayes aplicado a un filtro de *spam*

Supongamos que estamos construyendo un filtro de spam y queremos determinar la probabilidad de que un correo electrónico sea spam, $P(S)$, dado que contiene una palabra específica, $X$, por ejemplo, "oferta". Usando el Teorema de Bayes, podemos expresar esto como:

$$ P(S|X) = \frac{P(X|S) \times P(S)}{P(X)} $$

donde:

- $P(S|X)$ es la probabilidad de que un correo electrónico sea spam dado que contiene la palabra "oferta".
- $P(X|S)$ es la probabilidad de que un correo electrónico, siendo spam, contenga la palabra "oferta".
- $P(S)$ es la probabilidad *a priori* de que cualquier correo electrónico sea spam.
- $P(X)$ es la probabilidad total de que cualquier correo electrónico contenga la palabra "oferta".

Al calcular estas probabilidades y sustituirlas en la fórmula del Teorema de Bayes, podemos obtener una probabilidad actualizada de que un correo electrónico sea spam dado que contiene la palabra "oferta".

Esta versión simplificada al mínimo, puede extenderse a múltiples palabras y características para mejorar la precisión del filtro de spam, y puede irse actualizando (y por tanto, afinando) a medida que se reciben nuevos emails.

## Demostración del teorema de Bayes

La demostración del Teorema de Bayes se basa en la definición de [**probabilidad condicionada**](https://es.wikipedia.org/wiki/Probabilidad_condicionada). La probabilidad condicionada de un evento A dado que ha ocurrido un evento B se define como:

$$ P(A|B) = \frac{P(A \cap B)}{P(B)} $$

donde:

- $P(A|B)$ es la probabilidad de que ocurra el evento A dado que ha ocurrido el evento B.
- $P(A \cap B)$ es la probabilidad de que ocurran ambos eventos A y B.
- $P(B)$ es la probabilidad de que ocurra el evento B.

De esta formula sacamos que $ {P(A \cap B)} = P(A|B) \times P(B) $ y que $ {P(A \cap B)} = P(B|A) \times P(A) $, por lo que, sustituyendo en la fórmula anterior, obtenemos el Teorema de Bayes:

$$ P(A|B) = \frac{P(A \cap B)}{P(B)} \quad\Rightarrow\quad P(A|B) = \frac{P(B|A) \times P(A)}{P(B)} $$

## Material complementario

- [Conditional probability Explained Visually](https://setosa.io/ev/conditional-probability/)
- [Jesús Conde - Ciencia de Datos para aprendizaje automático. Teoría de la Probabilidad y Teorema de Bayes.](https://www.youtube.com/watch?v=foBVe1MuT5s)
- [Matemáticas profe Alex - Teorema de Bayes](https://www.youtube.com/watch?v=bDfCURXoKkU&list=PLeySRPnY35dH7Pnamtm2xxaCuT6jxt1vn&index=28)
- [3Blue1Brown - Bayes theorem, the geometry of changing beliefs](https://www.youtube.com/watch?v=HZGCoVF3YvM)  
- https://www.upgrad.com/blog/bayes-theorem-explained-with-example-complete-guide/
