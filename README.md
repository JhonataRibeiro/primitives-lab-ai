# Vector Lab — Fundamentos Matemáticos de Embeddings

> Laboratório prático para compreender a matemática por trás dos embeddings, implementando operações vetoriais do zero, sem depender de bibliotecas matemáticas.

## Objetivo

Entender como vetores são representados, medidos, normalizados e comparados — conceitos fundamentais para embeddings, busca semântica e bancos vetoriais.

A proposta não é simplesmente utilizar funções prontas, mas **compreender e implementar cada operação matematicamente**, validando os resultados com testes unitários.

## Princípios do laboratório

- Implementar os algoritmos manualmente, utilizando Python.
- Evitar NumPy e outras bibliotecas que escondam os cálculos.
- Resolver exemplos pequenos antes de escrever código.
- Criar testes unitários para validar as propriedades matemáticas.
- Documentar dúvidas, descobertas e limitações.
- Avançar somente depois de compreender cada conceito.

## 01 — Dimensão de um vetor

A dimensão representa a quantidade de coordenadas de um vetor.

Por exemplo:

```python
a = [3, 4]        # 2 dimensões
b = [3, 4, 5]     # 3 dimensões
```

Um vetor com 384 dimensões pode ser representado matematicamente como:

\[
v = [x_1, x_2, \ldots, x_{384}]
\]

**O que aprendi:**

- Cada posição representa uma coordenada associada a um eixo.
- A dimensão não depende dos valores das coordenadas.
- Um embedding pode possuir centenas de dimensões.
- As dimensões de um embedding não necessariamente possuem significados individuais interpretáveis.

**Implementação:** `dimension(vector)`

## 02 — Magnitude (norma L2)

A magnitude representa o comprimento do vetor.

Para um vetor bidimensional:

\[
v=[3,4]
\]

A norma L2 é calculada por:

\[
\|v\|_2=\sqrt{3^2+4^2}=5
\]

Para um vetor de qualquer dimensão:

\[
\|v\|_2=\sqrt{\sum_{i=1}^{n}x_i^2}
\]

**O que aprendi:**

- Magnitude e dimensão são propriedades diferentes.
- A magnitude corresponde ao comprimento da seta que representa o vetor.
- Multiplicar todas as coordenadas por 3 triplica a magnitude.
- Vetores com dimensões iguais podem apresentar magnitudes diferentes.

**Implementação:** `magnitude(vector)`

## 03 — Normalização L2

Normalizar um vetor não nulo pela norma L2 significa dividir cada coordenada por sua magnitude.

\[
\hat v=\frac{v}{\|v\|_2}
\]

Exemplo:

\[
[3,4]\rightarrow[0.6,0.8]
\]

O vetor resultante possui magnitude igual a 1.

**O que aprendi:**

- A normalização não altera a quantidade de dimensões.
- Preserva a direção e o sentido de vetores não nulos.
- Produz um vetor de magnitude 1.
- Um vetor nulo exige tratamento especial, pois sua magnitude é zero.

**Implementação:** `normalize(vector)`

## 04 — Produto escalar

O produto escalar combina dois vetores multiplicando suas coordenadas correspondentes e somando os resultados.

\[
a\cdot b=\sum_{i=1}^{n}a_i b_i
\]

Exemplo:

\[
[1,2]\cdot[3,4]=1(3)+2(4)=11
\]

**A investigar:**

- Por que vetores perpendiculares possuem produto escalar zero?
- Como o produto escalar está relacionado ao ângulo entre vetores?
- Como o sinal do produto escalar se relaciona com a direção?

**Implementação:** `dot_product(a, b)`

## 05 — Similaridade de cosseno

A similaridade de cosseno permite comparar a orientação de dois vetores não nulos.

\[
\cos(\theta)=\frac{a\cdot b}{\|a\|_2\|b\|_2}
\]

Casos importantes:

| Relação entre vetores | Similaridade |
|---|---|
| Mesma direção e sentido | 1 |
| Perpendiculares | 0 |
| Mesma direção, sentidos opostos | -1 |

**A investigar:**

- Por que a magnitude não altera a similaridade de cosseno?
- Qual é o papel da normalização?
- Por que essa métrica é utilizada em buscas semânticas?

**Implementação:** `cosine_similarity(a, b)`

## Testes unitários

O laboratório utiliza `unittest`, biblioteca nativa do Python.

Executar os testes:

```bash
python3 -m unittest test_vectory -v
```

Operações estudadas:

- [x] Conceito de dimensão
- [x] Conceito de magnitude / norma L2
- [x] Conceito inicial de normalização L2
- [ ] Implementar e validar magnitude
- [ ] Implementar e validar normalização
- [ ] Estudar e implementar produto escalar
- [ ] Estudar e implementar similaridade de cosseno
- [ ] Tratar vetores nulos e dimensões incompatíveis
- [ ] Criar demonstrações com embeddings reais

*As marcações representam o progresso conceitual, não necessariamente código concluído.*

## Relação com embeddings

Um modelo de embeddings transforma uma entrada, como um texto, em um vetor numérico.

Exemplo ilustrativo:

```text
"Como funciona um banco vetorial?"
             |
             v
    Modelo de embeddings
             |
             v
 [0.12, -0.45, ..., 0.31]
```

O objetivo deste laboratório é compreender as operações que permitem comparar esses vetores, antes de utilizar modelos reais ou bancos vetoriais.

**Importante:** conhecer dimensão, magnitude e cosseno não explica sozinho como um modelo aprende a representar significados. Essa será uma etapa posterior.

## Próximos passos

1. Finalizar os testes matemáticos.
2. Implementar todas as operações sem NumPy.
3. Visualizar vetores em duas dimensões.
4. Comparar vetores normalizados e não normalizados.
5. Gerar embeddings reais com um modelo local.
6. Investigar como a similaridade é aplicada na recuperação semântica.

---

**Filosofia do projeto:** entender antes de abstrair. Usar bibliotecas prontas depois de compreender o que acontece por baixo delas.