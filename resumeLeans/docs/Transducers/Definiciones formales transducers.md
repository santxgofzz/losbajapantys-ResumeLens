# Definiciones formales de transductores por rol

Documento que reúne las **33 definiciones formales de transductores** asociadas al diccionario `transformaciones`, organizadas según sus cuatro roles profesionales.

> Las definiciones, incluidos los alfabetos, estados y las funciones de transición (δ) y salida (ω), se conservan tal como aparecen en los archivos `.txt` originales. No se modifican ni se validan sus transiciones.

## Resumen

| Rol | Cantidad de transductores |
| --- | ---: |
| Full Stack Developer | 13 |
| Machine Learning Engineer | 7 |
| DevOps Engineer | 8 |
| Data Engineer | 5 |
| **Total** | **33** |

## Índice

- [Full Stack Developer](#full-stack-developer) (13 transductores): [JAVASCRIPT](#javascript), [TYPESCRIPT](#typescript), [REACT](#react), [ANGULAR](#angular), [VUE](#vue), [NODE_JS](#node_js), [DJANGO](#django), [SPRING_BOOT](#spring_boot), [SQL](#sql), [NOSQL](#nosql), [POSTGRESQL](#postgresql), [REST_API](#rest_api), [GIT](#git)
- [Machine Learning Engineer](#machine-learning-engineer) (7 transductores): [PYTHON](#python), [PANDAS](#pandas), [NUMPY](#numpy), [SCIKIT_LEARN](#scikit_learn), [TENSORFLOW](#tensorflow), [PYTORCH](#pytorch), [MACHINE_LEARNING](#machine_learning)
- [DevOps Engineer](#devops-engineer) (8 transductores): [DOCKER](#docker), [KUBERNETES](#kubernetes), [LINUX](#linux), [CI_CD](#ci_cd), [AMAZON_WEB_SERVICES](#amazon_web_services), [GOOGLE_CLOUD](#google_cloud), [AZURE](#azure), [TERRAFORM](#terraform)
- [Data Engineer](#data-engineer) (5 transductores): [SPARK](#spark), [AIRFLOW](#airflow), [ETL](#etl), [KAFKA](#kafka), [DATA_WAREHOUSE](#data_warehouse)

## Full Stack Developer

### JAVASCRIPT

```text
=== DEFINICIÓN FORMAL 7-TUPLA: JAVASCRIPT ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18}

2. Alfabeto de entrada (Σ):
   Σ = {A, C, I, J, P, R, S, T, V, a, c, i, j, p, r, s, t, v}

3. Alfabeto de salida (Γ):
   Γ = {A, C, I, J, P, R, S, T, V}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, j) = q2,  ω(q0, j) = J
  δ(q0, J) = q2,  ω(q0, J) = J
  δ(q2, s) = q3,  ω(q2, s) = A
  δ(q2, S) = q3,  ω(q2, S) = A
  δ(q2, a) = q11,  ω(q2, a) = A
  δ(q2, A) = q11,  ω(q2, A) = A
  δ(q3, ε) = q4,  ω(q3, ε) = V
  δ(q4, ε) = q5,  ω(q4, ε) = A
  δ(q5, ε) = q6,  ω(q5, ε) = S
  δ(q6, ε) = q7,  ω(q6, ε) = C
  δ(q7, ε) = q8,  ω(q7, ε) = R
  δ(q8, ε) = q9,  ω(q8, ε) = I
  δ(q9, ε) = q10,  ω(q9, ε) = P
  δ(q10, ε) = q1,  ω(q10, ε) = T
  δ(q11, v) = q12,  ω(q11, v) = V
  δ(q11, V) = q12,  ω(q11, V) = V
  δ(q12, a) = q13,  ω(q12, a) = A
  δ(q12, A) = q13,  ω(q12, A) = A
  δ(q13, s) = q14,  ω(q13, s) = S
  δ(q13, S) = q14,  ω(q13, S) = S
  δ(q14, c) = q15,  ω(q14, c) = C
  δ(q14, C) = q15,  ω(q14, C) = C
  δ(q15, r) = q16,  ω(q15, r) = R
  δ(q15, R) = q16,  ω(q15, R) = R
  δ(q16, i) = q17,  ω(q16, i) = I
  δ(q16, I) = q17,  ω(q16, I) = I
  δ(q17, p) = q18,  ω(q17, p) = P
  δ(q17, P) = q18,  ω(q17, P) = P
  δ(q18, t) = q1,  ω(q18, t) = T
  δ(q18, T) = q1,  ω(q18, T) = T
====================================================
```

### TYPESCRIPT

```text
=== DEFINICIÓN FORMAL 7-TUPLA: TYPESCRIPT ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18}

2. Alfabeto de entrada (Σ):
   Σ = {C, E, I, P, R, S, T, Y, c, e, i, p, r, s, t, y}

3. Alfabeto de salida (Γ):
   Γ = {C, E, I, P, R, S, T, Y}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, t) = q2,  ω(q0, t) = T
  δ(q0, T) = q2,  ω(q0, T) = T
  δ(q2, s) = q3,  ω(q2, s) = Y
  δ(q2, S) = q3,  ω(q2, S) = Y
  δ(q2, y) = q11,  ω(q2, y) = Y
  δ(q2, Y) = q11,  ω(q2, Y) = Y
  δ(q3, ε) = q4,  ω(q3, ε) = P
  δ(q4, ε) = q5,  ω(q4, ε) = E
  δ(q5, ε) = q6,  ω(q5, ε) = S
  δ(q6, ε) = q7,  ω(q6, ε) = C
  δ(q7, ε) = q8,  ω(q7, ε) = R
  δ(q8, ε) = q9,  ω(q8, ε) = I
  δ(q9, ε) = q10,  ω(q9, ε) = P
  δ(q10, ε) = q1,  ω(q10, ε) = T
  δ(q11, p) = q12,  ω(q11, p) = P
  δ(q11, P) = q12,  ω(q11, P) = P
  δ(q12, e) = q13,  ω(q12, e) = E
  δ(q12, E) = q13,  ω(q12, E) = E
  δ(q13, s) = q14,  ω(q13, s) = S
  δ(q13, S) = q14,  ω(q13, S) = S
  δ(q14, c) = q15,  ω(q14, c) = C
  δ(q14, C) = q15,  ω(q14, C) = C
  δ(q15, r) = q16,  ω(q15, r) = R
  δ(q15, R) = q16,  ω(q15, R) = R
  δ(q16, i) = q17,  ω(q16, i) = I
  δ(q16, I) = q17,  ω(q16, I) = I
  δ(q17, p) = q18,  ω(q17, p) = P
  δ(q17, P) = q18,  ω(q17, P) = P
  δ(q18, t) = q1,  ω(q18, t) = T
  δ(q18, T) = q1,  ω(q18, T) = T
====================================================
```

### REACT

```text
=== DEFINICIÓN FORMAL 7-TUPLA: REACT ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9}

2. Alfabeto de entrada (Σ):
   Σ = {., A, C, E, J, R, S, T, a, c, e, j, r, s, t}

3. Alfabeto de salida (Γ):
   Γ = {A, C, E, R, T}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, r) = q2,  ω(q0, r) = R
  δ(q0, R) = q2,  ω(q0, R) = R
  δ(q2, e) = q3,  ω(q2, e) = E
  δ(q2, E) = q3,  ω(q2, E) = E
  δ(q3, a) = q4,  ω(q3, a) = A
  δ(q3, A) = q4,  ω(q3, A) = A
  δ(q4, c) = q5,  ω(q4, c) = C
  δ(q4, C) = q5,  ω(q4, C) = C
  δ(q5, t) = q6,  ω(q5, t) = T
  δ(q5, T) = q6,  ω(q5, T) = T
  δ(q5, t) = q1,  ω(q5, t) = T
  δ(q5, T) = q1,  ω(q5, T) = T
  δ(q6, .) = q7,  ω(q6, .) = ε
  δ(q6, j) = q9,  ω(q6, j) = ε
  δ(q6, J) = q9,  ω(q6, J) = ε
  δ(q7, j) = q8,  ω(q7, j) = ε
  δ(q7, J) = q8,  ω(q7, J) = ε
  δ(q8, s) = q1,  ω(q8, s) = ε
  δ(q8, S) = q1,  ω(q8, S) = ε
  δ(q9, s) = q1,  ω(q9, s) = ε
  δ(q9, S) = q1,  ω(q9, S) = ε
====================================================
```

### ANGULAR

```text
=== DEFINICIÓN FORMAL 7-TUPLA: ANGULAR ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11}

2. Alfabeto de entrada (Σ):
   Σ = {., A, G, J, L, N, R, S, U, a, g, j, l, n, r, s, u}

3. Alfabeto de salida (Γ):
   Γ = {A, G, L, N, R, U}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, a) = q2,  ω(q0, a) = A
  δ(q0, A) = q2,  ω(q0, A) = A
  δ(q2, n) = q3,  ω(q2, n) = N
  δ(q2, N) = q3,  ω(q2, N) = N
  δ(q3, g) = q4,  ω(q3, g) = G
  δ(q3, G) = q4,  ω(q3, G) = G
  δ(q4, u) = q5,  ω(q4, u) = U
  δ(q4, U) = q5,  ω(q4, U) = U
  δ(q5, l) = q6,  ω(q5, l) = L
  δ(q5, L) = q6,  ω(q5, L) = L
  δ(q6, a) = q7,  ω(q6, a) = A
  δ(q6, A) = q7,  ω(q6, A) = A
  δ(q7, r) = q1,  ω(q7, r) = R
  δ(q7, R) = q1,  ω(q7, R) = R
  δ(q7, r) = q8,  ω(q7, r) = R
  δ(q7, R) = q8,  ω(q7, R) = R
  δ(q8, .) = q9,  ω(q8, .) = ε
  δ(q8, j) = q11,  ω(q8, j) = ε
  δ(q8, J) = q11,  ω(q8, J) = ε
  δ(q9, j) = q10,  ω(q9, j) = ε
  δ(q9, J) = q10,  ω(q9, J) = ε
  δ(q10, s) = q1,  ω(q10, s) = ε
  δ(q10, S) = q1,  ω(q10, S) = ε
  δ(q11, s) = q1,  ω(q11, s) = ε
  δ(q11, S) = q1,  ω(q11, S) = ε
====================================================
```

### VUE

```text
=== DEFINICIÓN FORMAL 7-TUPLA: VUE ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7}

2. Alfabeto de entrada (Σ):
   Σ = {., E, J, S, U, V, e, j, s, u, v}

3. Alfabeto de salida (Γ):
   Γ = {E, U, V}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, v) = q2,  ω(q0, v) = V
  δ(q0, V) = q2,  ω(q0, V) = V
  δ(q2, u) = q3,  ω(q2, u) = U
  δ(q2, U) = q3,  ω(q2, U) = U
  δ(q3, e) = q4,  ω(q3, e) = E
  δ(q3, E) = q4,  ω(q3, E) = E
  δ(q3, e) = q1,  ω(q3, e) = E
  δ(q3, E) = q1,  ω(q3, E) = E
  δ(q4, .) = q5,  ω(q4, .) = ε
  δ(q4, j) = q7,  ω(q4, j) = ε
  δ(q4, J) = q7,  ω(q4, J) = ε
  δ(q5, j) = q6,  ω(q5, j) = ε
  δ(q5, J) = q6,  ω(q5, J) = ε
  δ(q6, s) = q1,  ω(q6, s) = ε
  δ(q6, S) = q1,  ω(q6, S) = ε
  δ(q7, s) = q1,  ω(q7, s) = ε
  δ(q7, S) = q1,  ω(q7, S) = ε
====================================================
```

### NODE_JS

```text
=== DEFINICIÓN FORMAL 7-TUPLA: NODE_JS ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11}

2. Alfabeto de entrada (Σ):
   Σ = {., D, E, J, N, O, S, d, e, j, n, o, s}

3. Alfabeto de salida (Γ):
   Γ = {D, E, J, N, O, S, _}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, n) = q2,  ω(q0, n) = N
  δ(q0, N) = q2,  ω(q0, N) = N
  δ(q2, o) = q3,  ω(q2, o) = O
  δ(q2, O) = q3,  ω(q2, O) = O
  δ(q3, d) = q4,  ω(q3, d) = D
  δ(q3, D) = q4,  ω(q3, D) = D
  δ(q4, e) = q5,  ω(q4, e) = E
  δ(q4, E) = q5,  ω(q4, E) = E
  δ(q5, j) = q6,  ω(q5, j) = _
  δ(q5, J) = q6,  ω(q5, J) = _
  δ(q5, .) = q8,  ω(q5, .) = _
  δ(q5, ε) = q10,  ω(q5, ε) = _
  δ(q6, s) = q7,  ω(q6, s) = J
  δ(q6, S) = q7,  ω(q6, S) = J
  δ(q7, ε) = q1,  ω(q7, ε) = S
  δ(q8, j) = q9,  ω(q8, j) = J
  δ(q8, J) = q9,  ω(q8, J) = J
  δ(q9, s) = q1,  ω(q9, s) = S
  δ(q9, S) = q1,  ω(q9, S) = S
  δ(q10, ε) = q11,  ω(q10, ε) = J
  δ(q11, ε) = q1,  ω(q11, ε) = S
====================================================
```

### DJANGO

```text
=== DEFINICIÓN FORMAL 7-TUPLA: DJANGO ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6}

2. Alfabeto de entrada (Σ):
   Σ = {A, D, G, J, N, O, a, d, g, j, n, o}

3. Alfabeto de salida (Γ):
   Γ = {A, D, G, J, N, O}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, d) = q2,  ω(q0, d) = D
  δ(q0, D) = q2,  ω(q0, D) = D
  δ(q2, j) = q3,  ω(q2, j) = J
  δ(q2, J) = q3,  ω(q2, J) = J
  δ(q3, a) = q4,  ω(q3, a) = A
  δ(q3, A) = q4,  ω(q3, A) = A
  δ(q4, n) = q5,  ω(q4, n) = N
  δ(q4, N) = q5,  ω(q4, N) = N
  δ(q5, g) = q6,  ω(q5, g) = G
  δ(q5, G) = q6,  ω(q5, G) = G
  δ(q6, o) = q1,  ω(q6, o) = O
  δ(q6, O) = q1,  ω(q6, O) = O
====================================================
```

### SPRING_BOOT

```text
=== DEFINICIÓN FORMAL 7-TUPLA: SPRING_BOOT ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19}

2. Alfabeto de entrada (Σ):
   Σ = { , B, G, I, N, O, P, R, S, T, b, g, i, n, o, p, r, s, t}

3. Alfabeto de salida (Γ):
   Γ = {B, G, I, N, O, P, R, S, T, _}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, s) = q2,  ω(q0, s) = S
  δ(q0, S) = q2,  ω(q0, S) = S
  δ(q2, p) = q3,  ω(q2, p) = P
  δ(q2, P) = q3,  ω(q2, P) = P
  δ(q3, r) = q4,  ω(q3, r) = R
  δ(q3, R) = q4,  ω(q3, R) = R
  δ(q4, i) = q5,  ω(q4, i) = I
  δ(q4, I) = q5,  ω(q4, I) = I
  δ(q5, n) = q6,  ω(q5, n) = N
  δ(q5, N) = q6,  ω(q5, N) = N
  δ(q6, g) = q7,  ω(q6, g) = G
  δ(q6, G) = q7,  ω(q6, G) = G
  δ(q7,  ) = q8,  ω(q7,  ) = _
  δ(q7, b) = q12,  ω(q7, b) = _
  δ(q7, B) = q12,  ω(q7, B) = _
  δ(q7, ε) = q16,  ω(q7, ε) = _
  δ(q8, b) = q9,  ω(q8, b) = B
  δ(q8, B) = q9,  ω(q8, B) = B
  δ(q9, o) = q10,  ω(q9, o) = O
  δ(q9, O) = q10,  ω(q9, O) = O
  δ(q10, o) = q11,  ω(q10, o) = O
  δ(q10, O) = q11,  ω(q10, O) = O
  δ(q11, t) = q1,  ω(q11, t) = T
  δ(q11, T) = q1,  ω(q11, T) = T
  δ(q12, o) = q13,  ω(q12, o) = B
  δ(q12, O) = q13,  ω(q12, O) = B
  δ(q13, o) = q14,  ω(q13, o) = O
  δ(q13, O) = q14,  ω(q13, O) = O
  δ(q14, t) = q15,  ω(q14, t) = O
  δ(q14, T) = q15,  ω(q14, T) = O
  δ(q15, ε) = q1,  ω(q15, ε) = T
  δ(q16, ε) = q17,  ω(q16, ε) = B
  δ(q17, ε) = q18,  ω(q17, ε) = O
  δ(q18, ε) = q19,  ω(q18, ε) = O
  δ(q19, ε) = q1,  ω(q19, ε) = T
====================================================
```

### SQL

```text
=== DEFINICIÓN FORMAL 7-TUPLA: SQL ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3}

2. Alfabeto de entrada (Σ):
   Σ = {L, Q, S, l, q, s}

3. Alfabeto de salida (Γ):
   Γ = {L, Q, S}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, s) = q2,  ω(q0, s) = S
  δ(q0, S) = q2,  ω(q0, S) = S
  δ(q2, q) = q3,  ω(q2, q) = Q
  δ(q2, Q) = q3,  ω(q2, Q) = Q
  δ(q3, l) = q1,  ω(q3, l) = L
  δ(q3, L) = q1,  ω(q3, L) = L
====================================================
```

### NOSQL

```text
=== DEFINICIÓN FORMAL 7-TUPLA: NOSQL ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8}

2. Alfabeto de entrada (Σ):
   Σ = { , L, N, O, Q, S, l, n, o, q, s}

3. Alfabeto de salida (Γ):
   Γ = {L, N, O, Q, S}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, n) = q2,  ω(q0, n) = N
  δ(q0, N) = q2,  ω(q0, N) = N
  δ(q2, o) = q3,  ω(q2, o) = O
  δ(q2, O) = q3,  ω(q2, O) = O
  δ(q3, s) = q4,  ω(q3, s) = S
  δ(q3, S) = q4,  ω(q3, S) = S
  δ(q3,  ) = q6,  ω(q3,  ) = S
  δ(q4, q) = q5,  ω(q4, q) = Q
  δ(q4, Q) = q5,  ω(q4, Q) = Q
  δ(q5, l) = q1,  ω(q5, l) = L
  δ(q5, L) = q1,  ω(q5, L) = L
  δ(q6, s) = q7,  ω(q6, s) = Q
  δ(q6, S) = q7,  ω(q6, S) = Q
  δ(q7, q) = q8,  ω(q7, q) = L
  δ(q7, Q) = q8,  ω(q7, Q) = L
  δ(q8, l) = q1,  ω(q8, l) = ε
  δ(q8, L) = q1,  ω(q8, L) = ε
====================================================
```

### POSTGRESQL

```text
=== DEFINICIÓN FORMAL 7-TUPLA: POSTGRESQL ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11}

2. Alfabeto de entrada (Σ):
   Σ = {E, G, L, O, P, Q, R, S, T, e, g, l, o, p, q, r, s, t}

3. Alfabeto de salida (Γ):
   Γ = {E, G, L, O, P, Q, R, S, T}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, p) = q2,  ω(q0, p) = P
  δ(q0, P) = q2,  ω(q0, P) = P
  δ(q2, o) = q3,  ω(q2, o) = O
  δ(q2, O) = q3,  ω(q2, O) = O
  δ(q3, s) = q4,  ω(q3, s) = S
  δ(q3, S) = q4,  ω(q3, S) = S
  δ(q4, t) = q5,  ω(q4, t) = T
  δ(q4, T) = q5,  ω(q4, T) = T
  δ(q5, g) = q6,  ω(q5, g) = G
  δ(q5, G) = q6,  ω(q5, G) = G
  δ(q6, r) = q7,  ω(q6, r) = R
  δ(q6, R) = q7,  ω(q6, R) = R
  δ(q7, e) = q8,  ω(q7, e) = E
  δ(q7, E) = q8,  ω(q7, E) = E
  δ(q8, s) = q9,  ω(q8, s) = S
  δ(q8, S) = q9,  ω(q8, S) = S
  δ(q9, ε) = q10,  ω(q9, ε) = Q
  δ(q9, q) = q11,  ω(q9, q) = Q
  δ(q9, Q) = q11,  ω(q9, Q) = Q
  δ(q10, ε) = q1,  ω(q10, ε) = L
  δ(q11, l) = q1,  ω(q11, l) = L
  δ(q11, L) = q1,  ω(q11, L) = L
====================================================
```

### REST_API

```text
=== DEFINICIÓN FORMAL 7-TUPLA: REST_API ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14}

2. Alfabeto de entrada (Σ):
   Σ = { , A, E, F, I, L, P, R, S, T, U, a, e, f, i, l, p, r, s, t, u}

3. Alfabeto de salida (Γ):
   Γ = {A, E, I, P, R, S, T, _}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, r) = q2,  ω(q0, r) = R
  δ(q0, R) = q2,  ω(q0, R) = R
  δ(q1, s) = q1,  ω(q1, s) = ε
  δ(q1, S) = q1,  ω(q1, S) = ε
  δ(q2, e) = q3,  ω(q2, e) = E
  δ(q2, E) = q3,  ω(q2, E) = E
  δ(q3, s) = q4,  ω(q3, s) = S
  δ(q3, S) = q4,  ω(q3, S) = S
  δ(q4, t) = q5,  ω(q4, t) = T
  δ(q4, T) = q5,  ω(q4, T) = T
  δ(q5,  ) = q6,  ω(q5,  ) = _
  δ(q5, f) = q9,  ω(q5, f) = _
  δ(q5, F) = q9,  ω(q5, F) = _
  δ(q6, a) = q7,  ω(q6, a) = A
  δ(q6, A) = q7,  ω(q6, A) = A
  δ(q7, p) = q8,  ω(q7, p) = P
  δ(q7, P) = q8,  ω(q7, P) = P
  δ(q8, i) = q1,  ω(q8, i) = I
  δ(q8, I) = q1,  ω(q8, I) = I
  δ(q9, u) = q10,  ω(q9, u) = A
  δ(q9, U) = q10,  ω(q9, U) = A
  δ(q10, l) = q11,  ω(q10, l) = P
  δ(q10, L) = q11,  ω(q10, L) = P
  δ(q11,  ) = q12,  ω(q11,  ) = I
  δ(q12, a) = q13,  ω(q12, a) = ε
  δ(q12, A) = q13,  ω(q12, A) = ε
  δ(q13, p) = q14,  ω(q13, p) = ε
  δ(q13, P) = q14,  ω(q13, P) = ε
  δ(q14, i) = q1,  ω(q14, i) = ε
  δ(q14, I) = q1,  ω(q14, I) = ε
====================================================
```

### GIT

```text
=== DEFINICIÓN FORMAL 7-TUPLA: GIT ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3}

2. Alfabeto de entrada (Σ):
   Σ = {G, I, T, g, i, t}

3. Alfabeto de salida (Γ):
   Γ = {G, I, T}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, g) = q2,  ω(q0, g) = G
  δ(q0, G) = q2,  ω(q0, G) = G
  δ(q2, i) = q3,  ω(q2, i) = I
  δ(q2, I) = q3,  ω(q2, I) = I
  δ(q3, t) = q1,  ω(q3, t) = T
  δ(q3, T) = q1,  ω(q3, T) = T
====================================================
```

## Machine Learning Engineer

### PYTHON

```text
=== DEFINICIÓN FORMAL 7-TUPLA: PYTHON ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9}

2. Alfabeto de entrada (Σ):
   Σ = {H, N, O, P, T, Y, h, n, o, p, t, y}

3. Alfabeto de salida (Γ):
   Γ = {H, N, O, P, T, Y}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, p) = q2,  ω(q0, p) = P
  δ(q0, P) = q2,  ω(q0, P) = P
  δ(q2, y) = q3,  ω(q2, y) = Y
  δ(q2, Y) = q3,  ω(q2, Y) = Y
  δ(q3, t) = q4,  ω(q3, t) = T
  δ(q3, T) = q4,  ω(q3, T) = T
  δ(q3, ε) = q7,  ω(q3, ε) = T
  δ(q4, h) = q5,  ω(q4, h) = H
  δ(q4, H) = q5,  ω(q4, H) = H
  δ(q5, o) = q6,  ω(q5, o) = O
  δ(q5, O) = q6,  ω(q5, O) = O
  δ(q6, n) = q1,  ω(q6, n) = N
  δ(q6, N) = q1,  ω(q6, N) = N
  δ(q7, ε) = q8,  ω(q7, ε) = H
  δ(q8, ε) = q9,  ω(q8, ε) = O
  δ(q9, ε) = q1,  ω(q9, ε) = N
====================================================
```

### PANDAS

```text
=== DEFINICIÓN FORMAL 7-TUPLA: PANDAS ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6}

2. Alfabeto de entrada (Σ):
   Σ = {A, D, N, P, S, a, d, n, p, s}

3. Alfabeto de salida (Γ):
   Γ = {A, D, N, P, S}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, p) = q2,  ω(q0, p) = P
  δ(q0, P) = q2,  ω(q0, P) = P
  δ(q2, a) = q3,  ω(q2, a) = A
  δ(q2, A) = q3,  ω(q2, A) = A
  δ(q3, n) = q4,  ω(q3, n) = N
  δ(q3, N) = q4,  ω(q3, N) = N
  δ(q4, d) = q5,  ω(q4, d) = D
  δ(q4, D) = q5,  ω(q4, D) = D
  δ(q5, a) = q6,  ω(q5, a) = A
  δ(q5, A) = q6,  ω(q5, A) = A
  δ(q6, s) = q1,  ω(q6, s) = S
  δ(q6, S) = q1,  ω(q6, S) = S
====================================================
```

### NUMPY

```text
=== DEFINICIÓN FORMAL 7-TUPLA: NUMPY ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5}

2. Alfabeto de entrada (Σ):
   Σ = {M, N, P, U, Y, m, n, p, u, y}

3. Alfabeto de salida (Γ):
   Γ = {M, N, P, U, Y}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, n) = q2,  ω(q0, n) = N
  δ(q0, N) = q2,  ω(q0, N) = N
  δ(q2, u) = q3,  ω(q2, u) = U
  δ(q2, U) = q3,  ω(q2, U) = U
  δ(q3, m) = q4,  ω(q3, m) = M
  δ(q3, M) = q4,  ω(q3, M) = M
  δ(q4, p) = q5,  ω(q4, p) = P
  δ(q4, P) = q5,  ω(q4, P) = P
  δ(q5, y) = q1,  ω(q5, y) = Y
  δ(q5, Y) = q1,  ω(q5, Y) = Y
====================================================
```

### SCIKIT_LEARN

```text
=== DEFINICIÓN FORMAL 7-TUPLA: SCIKIT_LEARN ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27}

2. Alfabeto de entrada (Σ):
   Σ = { , -, A, C, E, I, K, L, N, R, S, T, a, c, e, i, k, l, n, r, s, t}

3. Alfabeto de salida (Γ):
   Γ = {A, C, E, I, K, L, N, R, S, T, _}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, s) = q2,  ω(q0, s) = S
  δ(q0, S) = q2,  ω(q0, S) = S
  δ(q2, k) = q3,  ω(q2, k) = C
  δ(q2, K) = q3,  ω(q2, K) = C
  δ(q2, c) = q13,  ω(q2, c) = C
  δ(q2, C) = q13,  ω(q2, C) = C
  δ(q3, l) = q4,  ω(q3, l) = I
  δ(q3, L) = q4,  ω(q3, L) = I
  δ(q4, e) = q5,  ω(q4, e) = K
  δ(q4, E) = q5,  ω(q4, E) = K
  δ(q5, a) = q6,  ω(q5, a) = I
  δ(q5, A) = q6,  ω(q5, A) = I
  δ(q6, r) = q7,  ω(q6, r) = T
  δ(q6, R) = q7,  ω(q6, R) = T
  δ(q7, n) = q8,  ω(q7, n) = _
  δ(q7, N) = q8,  ω(q7, N) = _
  δ(q8, ε) = q9,  ω(q8, ε) = L
  δ(q9, ε) = q10,  ω(q9, ε) = E
  δ(q10, ε) = q11,  ω(q10, ε) = A
  δ(q11, ε) = q12,  ω(q11, ε) = R
  δ(q12, ε) = q1,  ω(q12, ε) = N
  δ(q13, i) = q14,  ω(q13, i) = I
  δ(q13, I) = q14,  ω(q13, I) = I
  δ(q14, k) = q15,  ω(q14, k) = K
  δ(q14, K) = q15,  ω(q14, K) = K
  δ(q15, i) = q16,  ω(q15, i) = I
  δ(q15, I) = q16,  ω(q15, I) = I
  δ(q16, t) = q17,  ω(q16, t) = T
  δ(q16, T) = q17,  ω(q16, T) = T
  δ(q17,  ) = q18,  ω(q17,  ) = _
  δ(q17, -) = q23,  ω(q17, -) = _
  δ(q18, l) = q19,  ω(q18, l) = L
  δ(q18, L) = q19,  ω(q18, L) = L
  δ(q19, e) = q20,  ω(q19, e) = E
  δ(q19, E) = q20,  ω(q19, E) = E
  δ(q20, a) = q21,  ω(q20, a) = A
  δ(q20, A) = q21,  ω(q20, A) = A
  δ(q21, r) = q22,  ω(q21, r) = R
  δ(q21, R) = q22,  ω(q21, R) = R
  δ(q22, n) = q1,  ω(q22, n) = N
  δ(q22, N) = q1,  ω(q22, N) = N
  δ(q23, l) = q24,  ω(q23, l) = L
  δ(q23, L) = q24,  ω(q23, L) = L
  δ(q24, e) = q25,  ω(q24, e) = E
  δ(q24, E) = q25,  ω(q24, E) = E
  δ(q25, a) = q26,  ω(q25, a) = A
  δ(q25, A) = q26,  ω(q25, A) = A
  δ(q26, r) = q27,  ω(q26, r) = R
  δ(q26, R) = q27,  ω(q26, R) = R
  δ(q27, n) = q1,  ω(q27, n) = N
  δ(q27, N) = q1,  ω(q27, N) = N
====================================================
```

### TENSORFLOW

```text
=== DEFINICIÓN FORMAL 7-TUPLA: TENSORFLOW ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22}

2. Alfabeto de entrada (Σ):
   Σ = { , E, F, L, N, O, R, S, T, W, e, f, l, n, o, r, s, t, w}

3. Alfabeto de salida (Γ):
   Γ = {E, F, L, N, O, R, S, T, W}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, t) = q2,  ω(q0, t) = T
  δ(q0, T) = q2,  ω(q0, T) = T
  δ(q2, e) = q3,  ω(q2, e) = E
  δ(q2, E) = q3,  ω(q2, E) = E
  δ(q2, f) = q15,  ω(q2, f) = E
  δ(q2, F) = q15,  ω(q2, F) = E
  δ(q3, n) = q4,  ω(q3, n) = N
  δ(q3, N) = q4,  ω(q3, N) = N
  δ(q4, s) = q5,  ω(q4, s) = S
  δ(q4, S) = q5,  ω(q4, S) = S
  δ(q5, o) = q6,  ω(q5, o) = O
  δ(q5, O) = q6,  ω(q5, O) = O
  δ(q6, r) = q7,  ω(q6, r) = R
  δ(q6, R) = q7,  ω(q6, R) = R
  δ(q7,  ) = q8,  ω(q7,  ) = F
  δ(q7, f) = q12,  ω(q7, f) = F
  δ(q7, F) = q12,  ω(q7, F) = F
  δ(q8, f) = q9,  ω(q8, f) = L
  δ(q8, F) = q9,  ω(q8, F) = L
  δ(q9, l) = q10,  ω(q9, l) = O
  δ(q9, L) = q10,  ω(q9, L) = O
  δ(q10, o) = q11,  ω(q10, o) = W
  δ(q10, O) = q11,  ω(q10, O) = W
  δ(q11, w) = q1,  ω(q11, w) = ε
  δ(q11, W) = q1,  ω(q11, W) = ε
  δ(q12, l) = q13,  ω(q12, l) = L
  δ(q12, L) = q13,  ω(q12, L) = L
  δ(q13, o) = q14,  ω(q13, o) = O
  δ(q13, O) = q14,  ω(q13, O) = O
  δ(q14, w) = q1,  ω(q14, w) = W
  δ(q14, W) = q1,  ω(q14, W) = W
  δ(q15, ε) = q16,  ω(q15, ε) = N
  δ(q16, ε) = q17,  ω(q16, ε) = S
  δ(q17, ε) = q18,  ω(q17, ε) = O
  δ(q18, ε) = q19,  ω(q18, ε) = R
  δ(q19, ε) = q20,  ω(q19, ε) = F
  δ(q20, ε) = q21,  ω(q20, ε) = L
  δ(q21, ε) = q22,  ω(q21, ε) = O
  δ(q22, ε) = q1,  ω(q22, ε) = W
====================================================
```

### PYTORCH

```text
=== DEFINICIÓN FORMAL 7-TUPLA: PYTORCH ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12}

2. Alfabeto de entrada (Σ):
   Σ = { , C, H, O, P, R, T, Y, c, h, o, p, r, t, y}

3. Alfabeto de salida (Γ):
   Γ = {C, H, O, P, R, T, Y}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, p) = q2,  ω(q0, p) = P
  δ(q0, P) = q2,  ω(q0, P) = P
  δ(q2, y) = q3,  ω(q2, y) = Y
  δ(q2, Y) = q3,  ω(q2, Y) = Y
  δ(q3,  ) = q4,  ω(q3,  ) = T
  δ(q3, t) = q9,  ω(q3, t) = T
  δ(q3, T) = q9,  ω(q3, T) = T
  δ(q4, t) = q5,  ω(q4, t) = O
  δ(q4, T) = q5,  ω(q4, T) = O
  δ(q5, o) = q6,  ω(q5, o) = R
  δ(q5, O) = q6,  ω(q5, O) = R
  δ(q6, r) = q7,  ω(q6, r) = C
  δ(q6, R) = q7,  ω(q6, R) = C
  δ(q7, c) = q8,  ω(q7, c) = H
  δ(q7, C) = q8,  ω(q7, C) = H
  δ(q8, h) = q1,  ω(q8, h) = ε
  δ(q8, H) = q1,  ω(q8, H) = ε
  δ(q9, o) = q10,  ω(q9, o) = O
  δ(q9, O) = q10,  ω(q9, O) = O
  δ(q10, r) = q11,  ω(q10, r) = R
  δ(q10, R) = q11,  ω(q10, R) = R
  δ(q11, c) = q12,  ω(q11, c) = C
  δ(q11, C) = q12,  ω(q11, C) = C
  δ(q12, h) = q1,  ω(q12, h) = H
  δ(q12, H) = q1,  ω(q12, H) = H
====================================================
```

### MACHINE_LEARNING

```text
=== DEFINICIÓN FORMAL 7-TUPLA: MACHINE_LEARNING ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38}

2. Alfabeto de entrada (Σ):
   Σ = { , -, A, C, E, G, H, I, L, M, N, R, a, c, e, g, h, i, l, m, n, r}

3. Alfabeto de salida (Γ):
   Γ = {A, C, E, G, H, I, L, M, N, R, _}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, m) = q2,  ω(q0, m) = M
  δ(q0, M) = q2,  ω(q0, M) = M
  δ(q2, l) = q3,  ω(q2, l) = A
  δ(q2, L) = q3,  ω(q2, L) = A
  δ(q2, a) = q17,  ω(q2, a) = A
  δ(q2, A) = q17,  ω(q2, A) = A
  δ(q3, ε) = q4,  ω(q3, ε) = C
  δ(q4, ε) = q5,  ω(q4, ε) = H
  δ(q5, ε) = q6,  ω(q5, ε) = I
  δ(q6, ε) = q7,  ω(q6, ε) = N
  δ(q7, ε) = q8,  ω(q7, ε) = E
  δ(q8, ε) = q9,  ω(q8, ε) = _
  δ(q9, ε) = q10,  ω(q9, ε) = L
  δ(q10, ε) = q11,  ω(q10, ε) = E
  δ(q11, ε) = q12,  ω(q11, ε) = A
  δ(q12, ε) = q13,  ω(q12, ε) = R
  δ(q13, ε) = q14,  ω(q13, ε) = N
  δ(q14, ε) = q15,  ω(q14, ε) = I
  δ(q15, ε) = q16,  ω(q15, ε) = N
  δ(q16, ε) = q1,  ω(q16, ε) = G
  δ(q17, c) = q18,  ω(q17, c) = C
  δ(q17, C) = q18,  ω(q17, C) = C
  δ(q18, h) = q19,  ω(q18, h) = H
  δ(q18, H) = q19,  ω(q18, H) = H
  δ(q19, i) = q20,  ω(q19, i) = I
  δ(q19, I) = q20,  ω(q19, I) = I
  δ(q20, n) = q21,  ω(q20, n) = N
  δ(q20, N) = q21,  ω(q20, N) = N
  δ(q21, e) = q22,  ω(q21, e) = E
  δ(q21, E) = q22,  ω(q21, E) = E
  δ(q22,  ) = q23,  ω(q22,  ) = _
  δ(q22, -) = q31,  ω(q22, -) = _
  δ(q23, l) = q24,  ω(q23, l) = L
  δ(q23, L) = q24,  ω(q23, L) = L
  δ(q24, e) = q25,  ω(q24, e) = E
  δ(q24, E) = q25,  ω(q24, E) = E
  δ(q25, a) = q26,  ω(q25, a) = A
  δ(q25, A) = q26,  ω(q25, A) = A
  δ(q26, r) = q27,  ω(q26, r) = R
  δ(q26, R) = q27,  ω(q26, R) = R
  δ(q27, n) = q28,  ω(q27, n) = N
  δ(q27, N) = q28,  ω(q27, N) = N
  δ(q28, i) = q29,  ω(q28, i) = I
  δ(q28, I) = q29,  ω(q28, I) = I
  δ(q29, n) = q30,  ω(q29, n) = N
  δ(q29, N) = q30,  ω(q29, N) = N
  δ(q30, g) = q1,  ω(q30, g) = G
  δ(q30, G) = q1,  ω(q30, G) = G
  δ(q31, l) = q32,  ω(q31, l) = L
  δ(q31, L) = q32,  ω(q31, L) = L
  δ(q32, e) = q33,  ω(q32, e) = E
  δ(q32, E) = q33,  ω(q32, E) = E
  δ(q33, a) = q34,  ω(q33, a) = A
  δ(q33, A) = q34,  ω(q33, A) = A
  δ(q34, r) = q35,  ω(q34, r) = R
  δ(q34, R) = q35,  ω(q34, R) = R
  δ(q35, n) = q36,  ω(q35, n) = N
  δ(q35, N) = q36,  ω(q35, N) = N
  δ(q36, i) = q37,  ω(q36, i) = I
  δ(q36, I) = q37,  ω(q36, I) = I
  δ(q37, n) = q38,  ω(q37, n) = N
  δ(q37, N) = q38,  ω(q37, N) = N
  δ(q38, g) = q1,  ω(q38, g) = G
  δ(q38, G) = q1,  ω(q38, G) = G
====================================================
```

## DevOps Engineer

### DOCKER

```text
=== DEFINICIÓN FORMAL 7-TUPLA: DOCKER ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6}

2. Alfabeto de entrada (Σ):
   Σ = {C, D, E, K, O, R, c, d, e, k, o, r}

3. Alfabeto de salida (Γ):
   Γ = {C, D, E, K, O, R}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, d) = q2,  ω(q0, d) = D
  δ(q0, D) = q2,  ω(q0, D) = D
  δ(q2, o) = q3,  ω(q2, o) = O
  δ(q2, O) = q3,  ω(q2, O) = O
  δ(q3, c) = q4,  ω(q3, c) = C
  δ(q3, C) = q4,  ω(q3, C) = C
  δ(q4, k) = q5,  ω(q4, k) = K
  δ(q4, K) = q5,  ω(q4, K) = K
  δ(q5, e) = q6,  ω(q5, e) = E
  δ(q5, E) = q6,  ω(q5, E) = E
  δ(q6, r) = q1,  ω(q6, r) = R
  δ(q6, R) = q1,  ω(q6, R) = R
====================================================
```

### KUBERNETES

```text
=== DEFINICIÓN FORMAL 7-TUPLA: KUBERNETES ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18}

2. Alfabeto de entrada (Σ):
   Σ = {8, B, E, K, N, R, S, T, U, b, e, k, n, r, s, t, u}

3. Alfabeto de salida (Γ):
   Γ = {B, E, K, N, R, S, T, U}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, k) = q2,  ω(q0, k) = K
  δ(q0, K) = q2,  ω(q0, K) = K
  δ(q2, u) = q3,  ω(q2, u) = U
  δ(q2, U) = q3,  ω(q2, U) = U
  δ(q2, 8) = q11,  ω(q2, 8) = U
  δ(q3, b) = q4,  ω(q3, b) = B
  δ(q3, B) = q4,  ω(q3, B) = B
  δ(q4, e) = q5,  ω(q4, e) = E
  δ(q4, E) = q5,  ω(q4, E) = E
  δ(q5, r) = q6,  ω(q5, r) = R
  δ(q5, R) = q6,  ω(q5, R) = R
  δ(q6, n) = q7,  ω(q6, n) = N
  δ(q6, N) = q7,  ω(q6, N) = N
  δ(q7, e) = q8,  ω(q7, e) = E
  δ(q7, E) = q8,  ω(q7, E) = E
  δ(q8, t) = q9,  ω(q8, t) = T
  δ(q8, T) = q9,  ω(q8, T) = T
  δ(q9, e) = q10,  ω(q9, e) = E
  δ(q9, E) = q10,  ω(q9, E) = E
  δ(q10, s) = q1,  ω(q10, s) = S
  δ(q10, S) = q1,  ω(q10, S) = S
  δ(q11, s) = q12,  ω(q11, s) = B
  δ(q11, S) = q12,  ω(q11, S) = B
  δ(q12, ε) = q13,  ω(q12, ε) = E
  δ(q13, ε) = q14,  ω(q13, ε) = R
  δ(q14, ε) = q15,  ω(q14, ε) = N
  δ(q15, ε) = q16,  ω(q15, ε) = E
  δ(q16, ε) = q17,  ω(q16, ε) = T
  δ(q17, ε) = q18,  ω(q17, ε) = E
  δ(q18, ε) = q1,  ω(q18, ε) = S
====================================================
```

### LINUX

```text
=== DEFINICIÓN FORMAL 7-TUPLA: LINUX ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5}

2. Alfabeto de entrada (Σ):
   Σ = {I, L, N, U, X, i, l, n, u, x}

3. Alfabeto de salida (Γ):
   Γ = {I, L, N, U, X}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, l) = q2,  ω(q0, l) = L
  δ(q0, L) = q2,  ω(q0, L) = L
  δ(q2, i) = q3,  ω(q2, i) = I
  δ(q2, I) = q3,  ω(q2, I) = I
  δ(q3, n) = q4,  ω(q3, n) = N
  δ(q3, N) = q4,  ω(q3, N) = N
  δ(q4, u) = q5,  ω(q4, u) = U
  δ(q4, U) = q5,  ω(q4, U) = U
  δ(q5, x) = q1,  ω(q5, x) = X
  δ(q5, X) = q1,  ω(q5, X) = X
====================================================
```

### CI_CD

```text
=== DEFINICIÓN FORMAL 7-TUPLA: CI_CD ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25}

2. Alfabeto de entrada (Σ):
   Σ = { , -, /, A, B, C, D, G, H, I, L, N, O, S, T, U, a, b, c, d, g, h, i, l, n, o, s, t, u}

3. Alfabeto de salida (Γ):
   Γ = {C, D, I, _}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, c) = q2,  ω(q0, c) = C
  δ(q0, C) = q2,  ω(q0, C) = C
  δ(q0, g) = q8,  ω(q0, g) = C
  δ(q0, G) = q8,  ω(q0, G) = C
  δ(q2, i) = q3,  ω(q2, i) = I
  δ(q2, I) = q3,  ω(q2, I) = I
  δ(q3, /) = q4,  ω(q3, /) = _
  δ(q3, -) = q6,  ω(q3, -) = _
  δ(q4, c) = q5,  ω(q4, c) = C
  δ(q4, C) = q5,  ω(q4, C) = C
  δ(q5, d) = q1,  ω(q5, d) = D
  δ(q5, D) = q1,  ω(q5, D) = D
  δ(q6, c) = q7,  ω(q6, c) = C
  δ(q6, C) = q7,  ω(q6, C) = C
  δ(q7, d) = q1,  ω(q7, d) = D
  δ(q7, D) = q1,  ω(q7, D) = D
  δ(q8, i) = q9,  ω(q8, i) = I
  δ(q8, I) = q9,  ω(q8, I) = I
  δ(q9, t) = q10,  ω(q9, t) = _
  δ(q9, T) = q10,  ω(q9, T) = _
  δ(q10, h) = q11,  ω(q10, h) = C
  δ(q10, H) = q11,  ω(q10, H) = C
  δ(q10, l) = q21,  ω(q10, l) = C
  δ(q10, L) = q21,  ω(q10, L) = C
  δ(q11, u) = q12,  ω(q11, u) = D
  δ(q11, U) = q12,  ω(q11, U) = D
  δ(q12, b) = q13,  ω(q12, b) = ε
  δ(q12, B) = q13,  ω(q12, B) = ε
  δ(q13,  ) = q14,  ω(q13,  ) = ε
  δ(q14, a) = q15,  ω(q14, a) = ε
  δ(q14, A) = q15,  ω(q14, A) = ε
  δ(q15, c) = q16,  ω(q15, c) = ε
  δ(q15, C) = q16,  ω(q15, C) = ε
  δ(q16, t) = q17,  ω(q16, t) = ε
  δ(q16, T) = q17,  ω(q16, T) = ε
  δ(q17, i) = q18,  ω(q17, i) = ε
  δ(q17, I) = q18,  ω(q17, I) = ε
  δ(q18, o) = q19,  ω(q18, o) = ε
  δ(q18, O) = q19,  ω(q18, O) = ε
  δ(q19, n) = q20,  ω(q19, n) = ε
  δ(q19, N) = q20,  ω(q19, N) = ε
  δ(q20, s) = q1,  ω(q20, s) = ε
  δ(q20, S) = q1,  ω(q20, S) = ε
  δ(q21, a) = q22,  ω(q21, a) = D
  δ(q21, A) = q22,  ω(q21, A) = D
  δ(q22, b) = q23,  ω(q22, b) = ε
  δ(q22, B) = q23,  ω(q22, B) = ε
  δ(q23,  ) = q24,  ω(q23,  ) = ε
  δ(q24, c) = q25,  ω(q24, c) = ε
  δ(q24, C) = q25,  ω(q24, C) = ε
  δ(q25, i) = q1,  ω(q25, i) = ε
  δ(q25, I) = q1,  ω(q25, I) = ε
====================================================
```

### AMAZON_WEB_SERVICES

```text
=== DEFINICIÓN FORMAL 7-TUPLA: AMAZON_WEB_SERVICES ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36}

2. Alfabeto de entrada (Σ):
   Σ = { , A, B, C, E, I, M, N, O, R, S, V, W, Z, a, b, c, e, i, m, n, o, r, s, v, w, z}

3. Alfabeto de salida (Γ):
   Γ = {A, B, C, E, I, M, N, O, R, S, V, W, Z, _}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, a) = q2,  ω(q0, a) = A
  δ(q0, A) = q2,  ω(q0, A) = A
  δ(q2, w) = q3,  ω(q2, w) = M
  δ(q2, W) = q3,  ω(q2, W) = M
  δ(q2, m) = q20,  ω(q2, m) = M
  δ(q2, M) = q20,  ω(q2, M) = M
  δ(q3, s) = q4,  ω(q3, s) = A
  δ(q3, S) = q4,  ω(q3, S) = A
  δ(q4, ε) = q5,  ω(q4, ε) = Z
  δ(q5, ε) = q6,  ω(q5, ε) = O
  δ(q6, ε) = q7,  ω(q6, ε) = N
  δ(q7, ε) = q8,  ω(q7, ε) = _
  δ(q8, ε) = q9,  ω(q8, ε) = W
  δ(q9, ε) = q10,  ω(q9, ε) = E
  δ(q10, ε) = q11,  ω(q10, ε) = B
  δ(q11, ε) = q12,  ω(q11, ε) = _
  δ(q12, ε) = q13,  ω(q12, ε) = S
  δ(q13, ε) = q14,  ω(q13, ε) = E
  δ(q14, ε) = q15,  ω(q14, ε) = R
  δ(q15, ε) = q16,  ω(q15, ε) = V
  δ(q16, ε) = q17,  ω(q16, ε) = I
  δ(q17, ε) = q18,  ω(q17, ε) = C
  δ(q18, ε) = q19,  ω(q18, ε) = E
  δ(q19, ε) = q1,  ω(q19, ε) = S
  δ(q20, a) = q21,  ω(q20, a) = A
  δ(q20, A) = q21,  ω(q20, A) = A
  δ(q21, z) = q22,  ω(q21, z) = Z
  δ(q21, Z) = q22,  ω(q21, Z) = Z
  δ(q22, o) = q23,  ω(q22, o) = O
  δ(q22, O) = q23,  ω(q22, O) = O
  δ(q23, n) = q24,  ω(q23, n) = N
  δ(q23, N) = q24,  ω(q23, N) = N
  δ(q24,  ) = q25,  ω(q24,  ) = _
  δ(q25, w) = q26,  ω(q25, w) = W
  δ(q25, W) = q26,  ω(q25, W) = W
  δ(q26, e) = q27,  ω(q26, e) = E
  δ(q26, E) = q27,  ω(q26, E) = E
  δ(q27, b) = q28,  ω(q27, b) = B
  δ(q27, B) = q28,  ω(q27, B) = B
  δ(q28,  ) = q29,  ω(q28,  ) = _
  δ(q29, s) = q30,  ω(q29, s) = S
  δ(q29, S) = q30,  ω(q29, S) = S
  δ(q30, e) = q31,  ω(q30, e) = E
  δ(q30, E) = q31,  ω(q30, E) = E
  δ(q31, r) = q32,  ω(q31, r) = R
  δ(q31, R) = q32,  ω(q31, R) = R
  δ(q32, v) = q33,  ω(q32, v) = V
  δ(q32, V) = q33,  ω(q32, V) = V
  δ(q33, i) = q34,  ω(q33, i) = I
  δ(q33, I) = q34,  ω(q33, I) = I
  δ(q34, c) = q35,  ω(q34, c) = C
  δ(q34, C) = q35,  ω(q34, C) = C
  δ(q35, e) = q36,  ω(q35, e) = E
  δ(q35, E) = q36,  ω(q35, E) = E
  δ(q36, s) = q1,  ω(q36, s) = S
  δ(q36, S) = q1,  ω(q36, S) = S
====================================================
```

### GOOGLE_CLOUD

```text
=== DEFINICIÓN FORMAL 7-TUPLA: GOOGLE_CLOUD ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30}

2. Alfabeto de entrada (Σ):
   Σ = { , A, C, D, E, F, G, L, M, O, P, R, T, U, a, c, d, e, f, g, l, m, o, p, r, t, u}

3. Alfabeto de salida (Γ):
   Γ = {C, D, E, G, L, O, U, _}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, g) = q2,  ω(q0, g) = G
  δ(q0, G) = q2,  ω(q0, G) = G
  δ(q1,  ) = q23,  ω(q1,  ) = ε
  δ(q2, c) = q3,  ω(q2, c) = O
  δ(q2, C) = q3,  ω(q2, C) = O
  δ(q2, o) = q13,  ω(q2, o) = O
  δ(q2, O) = q13,  ω(q2, O) = O
  δ(q3, p) = q4,  ω(q3, p) = O
  δ(q3, P) = q4,  ω(q3, P) = O
  δ(q4, ε) = q5,  ω(q4, ε) = G
  δ(q5, ε) = q6,  ω(q5, ε) = L
  δ(q6, ε) = q7,  ω(q6, ε) = E
  δ(q7, ε) = q8,  ω(q7, ε) = _
  δ(q8, ε) = q9,  ω(q8, ε) = C
  δ(q9, ε) = q10,  ω(q9, ε) = L
  δ(q10, ε) = q11,  ω(q10, ε) = O
  δ(q11, ε) = q12,  ω(q11, ε) = U
  δ(q12, ε) = q1,  ω(q12, ε) = D
  δ(q13, o) = q14,  ω(q13, o) = O
  δ(q13, O) = q14,  ω(q13, O) = O
  δ(q14, g) = q15,  ω(q14, g) = G
  δ(q14, G) = q15,  ω(q14, G) = G
  δ(q15, l) = q16,  ω(q15, l) = L
  δ(q15, L) = q16,  ω(q15, L) = L
  δ(q16, e) = q17,  ω(q16, e) = E
  δ(q16, E) = q17,  ω(q16, E) = E
  δ(q17,  ) = q18,  ω(q17,  ) = _
  δ(q18, c) = q19,  ω(q18, c) = C
  δ(q18, C) = q19,  ω(q18, C) = C
  δ(q19, l) = q20,  ω(q19, l) = L
  δ(q19, L) = q20,  ω(q19, L) = L
  δ(q20, o) = q21,  ω(q20, o) = O
  δ(q20, O) = q21,  ω(q20, O) = O
  δ(q21, u) = q22,  ω(q21, u) = U
  δ(q21, U) = q22,  ω(q21, U) = U
  δ(q22, d) = q1,  ω(q22, d) = D
  δ(q22, D) = q1,  ω(q22, D) = D
  δ(q23, p) = q24,  ω(q23, p) = ε
  δ(q23, P) = q24,  ω(q23, P) = ε
  δ(q24, l) = q25,  ω(q24, l) = ε
  δ(q24, L) = q25,  ω(q24, L) = ε
  δ(q25, a) = q26,  ω(q25, a) = ε
  δ(q25, A) = q26,  ω(q25, A) = ε
  δ(q26, t) = q27,  ω(q26, t) = ε
  δ(q26, T) = q27,  ω(q26, T) = ε
  δ(q27, f) = q28,  ω(q27, f) = ε
  δ(q27, F) = q28,  ω(q27, F) = ε
  δ(q28, o) = q29,  ω(q28, o) = ε
  δ(q28, O) = q29,  ω(q28, O) = ε
  δ(q29, r) = q30,  ω(q29, r) = ε
  δ(q29, R) = q30,  ω(q29, R) = ε
  δ(q30, m) = q1,  ω(q30, m) = ε
  δ(q30, M) = q1,  ω(q30, M) = ε
====================================================
```

### AZURE

```text
=== DEFINICIÓN FORMAL 7-TUPLA: AZURE ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19}

2. Alfabeto de entrada (Σ):
   Σ = { , A, C, E, F, I, M, O, R, S, T, U, Z, a, c, e, f, i, m, o, r, s, t, u, z}

3. Alfabeto de salida (Γ):
   Γ = {A, E, R, U, Z}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, a) = q2,  ω(q0, a) = A
  δ(q0, A) = q2,  ω(q0, A) = A
  δ(q0, m) = q6,  ω(q0, m) = A
  δ(q0, M) = q6,  ω(q0, M) = A
  δ(q2, z) = q3,  ω(q2, z) = Z
  δ(q2, Z) = q3,  ω(q2, Z) = Z
  δ(q3, u) = q4,  ω(q3, u) = U
  δ(q3, U) = q4,  ω(q3, U) = U
  δ(q4, r) = q5,  ω(q4, r) = R
  δ(q4, R) = q5,  ω(q4, R) = R
  δ(q5, e) = q1,  ω(q5, e) = E
  δ(q5, E) = q1,  ω(q5, E) = E
  δ(q6, i) = q7,  ω(q6, i) = Z
  δ(q6, I) = q7,  ω(q6, I) = Z
  δ(q7, c) = q8,  ω(q7, c) = U
  δ(q7, C) = q8,  ω(q7, C) = U
  δ(q8, r) = q9,  ω(q8, r) = R
  δ(q8, R) = q9,  ω(q8, R) = R
  δ(q9, o) = q10,  ω(q9, o) = E
  δ(q9, O) = q10,  ω(q9, O) = E
  δ(q10, s) = q11,  ω(q10, s) = ε
  δ(q10, S) = q11,  ω(q10, S) = ε
  δ(q11, o) = q12,  ω(q11, o) = ε
  δ(q11, O) = q12,  ω(q11, O) = ε
  δ(q12, f) = q13,  ω(q12, f) = ε
  δ(q12, F) = q13,  ω(q12, F) = ε
  δ(q13, t) = q14,  ω(q13, t) = ε
  δ(q13, T) = q14,  ω(q13, T) = ε
  δ(q14,  ) = q15,  ω(q14,  ) = ε
  δ(q15, a) = q16,  ω(q15, a) = ε
  δ(q15, A) = q16,  ω(q15, A) = ε
  δ(q16, z) = q17,  ω(q16, z) = ε
  δ(q16, Z) = q17,  ω(q16, Z) = ε
  δ(q17, u) = q18,  ω(q17, u) = ε
  δ(q17, U) = q18,  ω(q17, U) = ε
  δ(q18, r) = q19,  ω(q18, r) = ε
  δ(q18, R) = q19,  ω(q18, R) = ε
  δ(q19, e) = q1,  ω(q19, e) = ε
  δ(q19, E) = q1,  ω(q19, E) = ε
====================================================
```

### TERRAFORM

```text
=== DEFINICIÓN FORMAL 7-TUPLA: TERRAFORM ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9}

2. Alfabeto de entrada (Σ):
   Σ = {A, E, F, M, O, R, T, a, e, f, m, o, r, t}

3. Alfabeto de salida (Γ):
   Γ = {A, E, F, M, O, R, T}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, t) = q2,  ω(q0, t) = T
  δ(q0, T) = q2,  ω(q0, T) = T
  δ(q2, e) = q3,  ω(q2, e) = E
  δ(q2, E) = q3,  ω(q2, E) = E
  δ(q3, r) = q4,  ω(q3, r) = R
  δ(q3, R) = q4,  ω(q3, R) = R
  δ(q4, r) = q5,  ω(q4, r) = R
  δ(q4, R) = q5,  ω(q4, R) = R
  δ(q5, a) = q6,  ω(q5, a) = A
  δ(q5, A) = q6,  ω(q5, A) = A
  δ(q6, f) = q7,  ω(q6, f) = F
  δ(q6, F) = q7,  ω(q6, F) = F
  δ(q7, o) = q8,  ω(q7, o) = O
  δ(q7, O) = q8,  ω(q7, O) = O
  δ(q8, r) = q9,  ω(q8, r) = R
  δ(q8, R) = q9,  ω(q8, R) = R
  δ(q9, m) = q1,  ω(q9, m) = M
  δ(q9, M) = q1,  ω(q9, M) = M
====================================================
```

## Data Engineer

### SPARK

```text
=== DEFINICIÓN FORMAL 7-TUPLA: SPARK ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22}

2. Alfabeto de entrada (Σ):
   Σ = { , A, C, E, H, K, P, R, S, Y, a, c, e, h, k, p, r, s, y}

3. Alfabeto de salida (Γ):
   Γ = {A, K, P, R, S}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, a) = q2,  ω(q0, a) = S
  δ(q0, A) = q2,  ω(q0, A) = S
  δ(q0, s) = q13,  ω(q0, s) = S
  δ(q0, S) = q13,  ω(q0, S) = S
  δ(q0, p) = q17,  ω(q0, p) = S
  δ(q0, P) = q17,  ω(q0, P) = S
  δ(q2, p) = q3,  ω(q2, p) = P
  δ(q2, P) = q3,  ω(q2, P) = P
  δ(q3, a) = q4,  ω(q3, a) = A
  δ(q3, A) = q4,  ω(q3, A) = A
  δ(q4, c) = q5,  ω(q4, c) = R
  δ(q4, C) = q5,  ω(q4, C) = R
  δ(q5, h) = q6,  ω(q5, h) = K
  δ(q5, H) = q6,  ω(q5, H) = K
  δ(q6, e) = q7,  ω(q6, e) = ε
  δ(q6, E) = q7,  ω(q6, E) = ε
  δ(q7,  ) = q8,  ω(q7,  ) = ε
  δ(q8, s) = q9,  ω(q8, s) = ε
  δ(q8, S) = q9,  ω(q8, S) = ε
  δ(q9, p) = q10,  ω(q9, p) = ε
  δ(q9, P) = q10,  ω(q9, P) = ε
  δ(q10, a) = q11,  ω(q10, a) = ε
  δ(q10, A) = q11,  ω(q10, A) = ε
  δ(q11, r) = q12,  ω(q11, r) = ε
  δ(q11, R) = q12,  ω(q11, R) = ε
  δ(q12, k) = q1,  ω(q12, k) = ε
  δ(q12, K) = q1,  ω(q12, K) = ε
  δ(q13, p) = q14,  ω(q13, p) = P
  δ(q13, P) = q14,  ω(q13, P) = P
  δ(q14, a) = q15,  ω(q14, a) = A
  δ(q14, A) = q15,  ω(q14, A) = A
  δ(q15, r) = q16,  ω(q15, r) = R
  δ(q15, R) = q16,  ω(q15, R) = R
  δ(q16, k) = q1,  ω(q16, k) = K
  δ(q16, K) = q1,  ω(q16, K) = K
  δ(q17, y) = q18,  ω(q17, y) = P
  δ(q17, Y) = q18,  ω(q17, Y) = P
  δ(q18, s) = q19,  ω(q18, s) = A
  δ(q18, S) = q19,  ω(q18, S) = A
  δ(q19, p) = q20,  ω(q19, p) = R
  δ(q19, P) = q20,  ω(q19, P) = R
  δ(q20, a) = q21,  ω(q20, a) = K
  δ(q20, A) = q21,  ω(q20, A) = K
  δ(q21, r) = q22,  ω(q21, r) = ε
  δ(q21, R) = q22,  ω(q21, R) = ε
  δ(q22, k) = q1,  ω(q22, k) = ε
  δ(q22, K) = q1,  ω(q22, K) = ε
====================================================
```

### AIRFLOW

```text
=== DEFINICIÓN FORMAL 7-TUPLA: AIRFLOW ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19}

2. Alfabeto de entrada (Σ):
   Σ = { , A, C, E, F, H, I, L, O, P, R, W, a, c, e, f, h, i, l, o, p, r, w}

3. Alfabeto de salida (Γ):
   Γ = {A, F, I, L, O, R, W}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, a) = q2,  ω(q0, a) = A
  δ(q0, A) = q2,  ω(q0, A) = A
  δ(q2, i) = q3,  ω(q2, i) = I
  δ(q2, I) = q3,  ω(q2, I) = I
  δ(q2, p) = q8,  ω(q2, p) = I
  δ(q2, P) = q8,  ω(q2, P) = I
  δ(q3, r) = q4,  ω(q3, r) = R
  δ(q3, R) = q4,  ω(q3, R) = R
  δ(q4, f) = q5,  ω(q4, f) = F
  δ(q4, F) = q5,  ω(q4, F) = F
  δ(q5, l) = q6,  ω(q5, l) = L
  δ(q5, L) = q6,  ω(q5, L) = L
  δ(q6, o) = q7,  ω(q6, o) = O
  δ(q6, O) = q7,  ω(q6, O) = O
  δ(q7, w) = q1,  ω(q7, w) = W
  δ(q7, W) = q1,  ω(q7, W) = W
  δ(q8, a) = q9,  ω(q8, a) = R
  δ(q8, A) = q9,  ω(q8, A) = R
  δ(q9, c) = q10,  ω(q9, c) = F
  δ(q9, C) = q10,  ω(q9, C) = F
  δ(q10, h) = q11,  ω(q10, h) = L
  δ(q10, H) = q11,  ω(q10, H) = L
  δ(q11, e) = q12,  ω(q11, e) = O
  δ(q11, E) = q12,  ω(q11, E) = O
  δ(q12,  ) = q13,  ω(q12,  ) = W
  δ(q13, a) = q14,  ω(q13, a) = ε
  δ(q13, A) = q14,  ω(q13, A) = ε
  δ(q14, i) = q15,  ω(q14, i) = ε
  δ(q14, I) = q15,  ω(q14, I) = ε
  δ(q15, r) = q16,  ω(q15, r) = ε
  δ(q15, R) = q16,  ω(q15, R) = ε
  δ(q16, f) = q17,  ω(q16, f) = ε
  δ(q16, F) = q17,  ω(q16, F) = ε
  δ(q17, l) = q18,  ω(q17, l) = ε
  δ(q17, L) = q18,  ω(q17, L) = ε
  δ(q18, o) = q19,  ω(q18, o) = ε
  δ(q18, O) = q19,  ω(q18, O) = ε
  δ(q19, w) = q1,  ω(q19, w) = ε
  δ(q19, W) = q1,  ω(q19, W) = ε
====================================================
```

### ETL

```text
=== DEFINICIÓN FORMAL 7-TUPLA: ETL ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23}

2. Alfabeto de entrada (Σ):
   Σ = { , A, C, D, E, F, L, M, N, O, R, S, T, X, a, c, d, e, f, l, m, n, o, r, s, t, x}

3. Alfabeto de salida (Γ):
   Γ = {E, L, T}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, e) = q2,  ω(q0, e) = E
  δ(q0, E) = q2,  ω(q0, E) = E
  δ(q2, t) = q3,  ω(q2, t) = T
  δ(q2, T) = q3,  ω(q2, T) = T
  δ(q2, x) = q4,  ω(q2, x) = T
  δ(q2, X) = q4,  ω(q2, X) = T
  δ(q3, l) = q1,  ω(q3, l) = L
  δ(q3, L) = q1,  ω(q3, L) = L
  δ(q4, t) = q5,  ω(q4, t) = L
  δ(q4, T) = q5,  ω(q4, T) = L
  δ(q5, r) = q6,  ω(q5, r) = ε
  δ(q5, R) = q6,  ω(q5, R) = ε
  δ(q6, a) = q7,  ω(q6, a) = ε
  δ(q6, A) = q7,  ω(q6, A) = ε
  δ(q7, c) = q8,  ω(q7, c) = ε
  δ(q7, C) = q8,  ω(q7, C) = ε
  δ(q8, t) = q9,  ω(q8, t) = ε
  δ(q8, T) = q9,  ω(q8, T) = ε
  δ(q9,  ) = q10,  ω(q9,  ) = ε
  δ(q10, t) = q11,  ω(q10, t) = ε
  δ(q10, T) = q11,  ω(q10, T) = ε
  δ(q11, r) = q12,  ω(q11, r) = ε
  δ(q11, R) = q12,  ω(q11, R) = ε
  δ(q12, a) = q13,  ω(q12, a) = ε
  δ(q12, A) = q13,  ω(q12, A) = ε
  δ(q13, n) = q14,  ω(q13, n) = ε
  δ(q13, N) = q14,  ω(q13, N) = ε
  δ(q14, s) = q15,  ω(q14, s) = ε
  δ(q14, S) = q15,  ω(q14, S) = ε
  δ(q15, f) = q16,  ω(q15, f) = ε
  δ(q15, F) = q16,  ω(q15, F) = ε
  δ(q16, o) = q17,  ω(q16, o) = ε
  δ(q16, O) = q17,  ω(q16, O) = ε
  δ(q17, r) = q18,  ω(q17, r) = ε
  δ(q17, R) = q18,  ω(q17, R) = ε
  δ(q18, m) = q19,  ω(q18, m) = ε
  δ(q18, M) = q19,  ω(q18, M) = ε
  δ(q19,  ) = q20,  ω(q19,  ) = ε
  δ(q20, l) = q21,  ω(q20, l) = ε
  δ(q20, L) = q21,  ω(q20, L) = ε
  δ(q21, o) = q22,  ω(q21, o) = ε
  δ(q21, O) = q22,  ω(q21, O) = ε
  δ(q22, a) = q23,  ω(q22, a) = ε
  δ(q22, A) = q23,  ω(q22, A) = ε
  δ(q23, d) = q1,  ω(q23, d) = ε
  δ(q23, D) = q1,  ω(q23, D) = ε
====================================================
```

### KAFKA

```text
=== DEFINICIÓN FORMAL 7-TUPLA: KAFKA ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16}

2. Alfabeto de entrada (Σ):
   Σ = { , A, C, E, F, H, K, P, a, c, e, f, h, k, p}

3. Alfabeto de salida (Γ):
   Γ = {A, F, K}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, k) = q2,  ω(q0, k) = K
  δ(q0, K) = q2,  ω(q0, K) = K
  δ(q0, a) = q6,  ω(q0, a) = K
  δ(q0, A) = q6,  ω(q0, A) = K
  δ(q2, a) = q3,  ω(q2, a) = A
  δ(q2, A) = q3,  ω(q2, A) = A
  δ(q3, f) = q4,  ω(q3, f) = F
  δ(q3, F) = q4,  ω(q3, F) = F
  δ(q4, k) = q5,  ω(q4, k) = K
  δ(q4, K) = q5,  ω(q4, K) = K
  δ(q5, a) = q1,  ω(q5, a) = A
  δ(q5, A) = q1,  ω(q5, A) = A
  δ(q6, p) = q7,  ω(q6, p) = A
  δ(q6, P) = q7,  ω(q6, P) = A
  δ(q7, a) = q8,  ω(q7, a) = F
  δ(q7, A) = q8,  ω(q7, A) = F
  δ(q8, c) = q9,  ω(q8, c) = K
  δ(q8, C) = q9,  ω(q8, C) = K
  δ(q9, h) = q10,  ω(q9, h) = A
  δ(q9, H) = q10,  ω(q9, H) = A
  δ(q10, e) = q11,  ω(q10, e) = ε
  δ(q10, E) = q11,  ω(q10, E) = ε
  δ(q11,  ) = q12,  ω(q11,  ) = ε
  δ(q12, k) = q13,  ω(q12, k) = ε
  δ(q12, K) = q13,  ω(q12, K) = ε
  δ(q13, a) = q14,  ω(q13, a) = ε
  δ(q13, A) = q14,  ω(q13, A) = ε
  δ(q14, f) = q15,  ω(q14, f) = ε
  δ(q14, F) = q15,  ω(q14, F) = ε
  δ(q15, k) = q16,  ω(q15, k) = ε
  δ(q15, K) = q16,  ω(q15, K) = ε
  δ(q16, a) = q1,  ω(q16, a) = ε
  δ(q16, A) = q1,  ω(q16, A) = ε
====================================================
```

### DATA_WAREHOUSE

```text
=== DEFINICIÓN FORMAL 7-TUPLA: DATA_WAREHOUSE ===
M = (Q, Σ, Γ, δ, ω, q0, F)

1. Conjunto de estados (Q):
   Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37}

2. Alfabeto de entrada (Σ):
   Σ = { , A, D, E, H, O, R, S, T, U, W, a, d, e, h, o, r, s, t, u, w}

3. Alfabeto de salida (Γ):
   Γ = {A, D, E, H, O, R, S, T, U, W, _}

4. Estado inicial (q0):
   q0 = q0

5. Estados de aceptación (F):
   F = {q1}

6 & 7. Funciones de transición (δ) y salida (ω):
  δ(q0, d) = q2,  ω(q0, d) = D
  δ(q0, D) = q2,  ω(q0, D) = D
  δ(q2, a) = q3,  ω(q2, a) = A
  δ(q2, A) = q3,  ω(q2, A) = A
  δ(q2, w) = q15,  ω(q2, w) = A
  δ(q2, W) = q15,  ω(q2, W) = A
  δ(q3, t) = q4,  ω(q3, t) = T
  δ(q3, T) = q4,  ω(q3, T) = T
  δ(q4, a) = q5,  ω(q4, a) = A
  δ(q4, A) = q5,  ω(q4, A) = A
  δ(q5,  ) = q6,  ω(q5,  ) = _
  δ(q6, w) = q7,  ω(q6, w) = W
  δ(q6, W) = q7,  ω(q6, W) = W
  δ(q7, a) = q8,  ω(q7, a) = A
  δ(q7, A) = q8,  ω(q7, A) = A
  δ(q8, r) = q9,  ω(q8, r) = R
  δ(q8, R) = q9,  ω(q8, R) = R
  δ(q9, e) = q10,  ω(q9, e) = E
  δ(q9, E) = q10,  ω(q9, E) = E
  δ(q10, h) = q11,  ω(q10, h) = H
  δ(q10, H) = q11,  ω(q10, H) = H
  δ(q11, o) = q12,  ω(q11, o) = O
  δ(q11, O) = q12,  ω(q11, O) = O
  δ(q12, u) = q13,  ω(q12, u) = U
  δ(q12, U) = q13,  ω(q12, U) = U
  δ(q13, s) = q14,  ω(q13, s) = S
  δ(q13, S) = q14,  ω(q13, S) = S
  δ(q14, e) = q1,  ω(q14, e) = E
  δ(q14, E) = q1,  ω(q14, E) = E
  δ(q15, ε) = q16,  ω(q15, ε) = T
  δ(q15, h) = q27,  ω(q15, h) = T
  δ(q15, H) = q27,  ω(q15, H) = T
  δ(q16, ε) = q17,  ω(q16, ε) = A
  δ(q17, ε) = q18,  ω(q17, ε) = _
  δ(q18, ε) = q19,  ω(q18, ε) = W
  δ(q19, ε) = q20,  ω(q19, ε) = A
  δ(q20, ε) = q21,  ω(q20, ε) = R
  δ(q21, ε) = q22,  ω(q21, ε) = E
  δ(q22, ε) = q23,  ω(q22, ε) = H
  δ(q23, ε) = q24,  ω(q23, ε) = O
  δ(q24, ε) = q25,  ω(q24, ε) = U
  δ(q25, ε) = q26,  ω(q25, ε) = S
  δ(q26, ε) = q1,  ω(q26, ε) = E
  δ(q27, ε) = q28,  ω(q27, ε) = A
  δ(q28, ε) = q29,  ω(q28, ε) = _
  δ(q29, ε) = q30,  ω(q29, ε) = W
  δ(q30, ε) = q31,  ω(q30, ε) = A
  δ(q31, ε) = q32,  ω(q31, ε) = R
  δ(q32, ε) = q33,  ω(q32, ε) = E
  δ(q33, ε) = q34,  ω(q33, ε) = H
  δ(q34, ε) = q35,  ω(q34, ε) = O
  δ(q35, ε) = q36,  ω(q35, ε) = U
  δ(q36, ε) = q37,  ω(q36, ε) = S
  δ(q37, ε) = q1,  ω(q37, ε) = E
====================================================
```
