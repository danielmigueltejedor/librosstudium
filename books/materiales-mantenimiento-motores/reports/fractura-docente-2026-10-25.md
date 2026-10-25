# Auditoría docente de fractura — 25/10/2026

## Fuente recibida

Presentación *Mecánica de la fractura*, Pablo Rodríguez González (ULE), **46 páginas**. Se ha leído y contrastado con el capítulo 3 del manual, el refuerzo previo, el formulario y la hoja Problemas 1. Se han distinguido afirmaciones de las diapositivas de aclaraciones matemáticas externas y de ejemplos originales. El material se utiliza solo como fuente de estudio: no se redistribuyen las diapositivas.

## Matriz de cobertura y cambios

| Páginas de la presentación | Contenido | Estado tras ampliación |
|---|---|---|
| 4–6 | Fallos históricos Liberty/Challenger | Incluido con reserva sobre causalidad histórica |
| 7–11 | Fractura dúctil, microcavidades, clivaje e intergranularidad | Incluido |
| 12–14 | Charpy/Izod y transición térmica | Incluido; no se generaliza universalidad BCC/FCC |
| 15–19 | Diseño por defectos y tensión de cohesión | Incluido y distinguido del dato certificado |
| 20–23 | Inglis y curvas de concentradores | Incluido; alerta de convención del semieje |
| 24–25 | Griffith y energía de dos caras | Derivación nueva, unidades y estado plano |
| 27–29 | Modos y campo singular elástico de modo I | Incluidas componentes y convención de ejes |
| 30–32 | Irwin, relación energía-intensidad, espesor | Incluido con comprobación completa de dimensiones |
| 33–34 | Placa central, borde, doble borde, grieta circular y elíptica | Familias diferenciadas y dos fórmulas explícitas |
| 35–36 | Probetas CT, SENB y DCB | Identificación y CT calculada; otros métodos requieren geometría definida |
| 37–39 | Tablas comparativas de tenacidad | Se explica uso no certificable de tablas ilustrativas |
| 40–41 | Dimensionado y carga admisible | Ecuaciones, unidades corregidas y limitaciones |
| 42–43 | Componentes críticos e inspecciones periódicas | Integrado con daño tolerable y POD |

## Advertencias fundamentales

1. **Inglis (página 20).** En la diapositiva el radical se escribe usando `2a` mientras el dibujo también denomina `2a` a la longitud total de grieta. Para una elipse con semieje mayor `a_e` y radio `rho=b_e²/a_e`, el modelo clásico es `Kt=1+2 sqrt(a_e/rho)`. El libro expone las dos convenciones y no atribuye al docente una errata confirmada.
2. **Campo de grieta (página 29).** Las etiquetas y signos dependen de orientación de ejes; la ampliación declara su propia convención, presenta el campo angular coherente y su validez asintótica.
3. **Griffith (página 25).** Derivación energética completa con `sigma_c=sqrt(2 E' gamma_s/(pi a))`, más definición del estado plano. Se distingue energía superficial de resistencia con disipación adicional.
4. **Tenacidad y energía (páginas 30–31).** La condición de espesor `B>=2.5(KIC/sigmay)²` es necesaria como cribado, pero no sustituye restricciones sobre grieta, ligamento ni validación del ensayo.
5. **Unidades (página 40).** La diapositiva rotula `KIC` como `MPa m^-2` y `Gc` como `MPa m`. Se explicitan `KIC: MPa sqrt(m)` y `Gc: J/m²` para evitar errores dimensionales.
6. **Geometrías (páginas 33–36).** Factores `Y` en `K=Y sigma sqrt(pi a)` no deben reemplazar funciones `f(a/W)` de CT, SENB o DCB sin la normalización de la carga correcta. Se declara el dominio de la aproximación de borde.

## Ejercicios y pruebas de regresión

- En el cuaderno de problemas se añaden **PF01–PF07**: Griffith, energía, placa de ancho finito con raíz implícita, borde con polinomio, CT, validez de deformación plana y razonamiento corto. Incluye autocorrección.
- Los números han sido calculados de forma independiente de los enunciados docentes para evitar copiar la hoja oficial y para asegurar coherencia dimensional.
- Test incorporado: `tests/test_matmo_fracture_slides.py`, además de los tests de Matemática existentes.

## Limitaciones y validación

El objetivo es estudiar solo con los dos libros sin tener que reconstruir las diapositivas, pero **no hay base para prometer una nota de 10, equivalencia literal de cada pregunta de un examen futuro, ni revisión científica independiente**. Los PDFs permanecen rotulados EN REVISIÓN por los bloqueos académicos previos; una release editorial no equivale a certificación. Los checks de compilación y CI deben completarse antes de fusionar o publicar una nueva edición.
