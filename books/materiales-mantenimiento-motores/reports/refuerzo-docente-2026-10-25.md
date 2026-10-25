# Refuerzo dirigido a Materiales — 25/10/2026

## Alcance y estado

Contraste de los materiales **facilitados en esta conversación**: 6 presentaciones del docente (Introducción: 34 pp.; Mecánica de fractura: 46; Fatiga: 37; Fluencia: 27; Degradación: 32; END y SHM: 37), formulario 2025V1 (1 p.) y Problemas 1 (3 pp., 8 ejercicios). Esta comparación complementa auditorías anteriores, pero no prueba que se hayan recibido todas las diapositivas del curso. La presentación completa de fractura se aportó después del primer contraste, y ahora está analizada específicamente en `reports/fractura-docente-2026-10-25.md`. Tampoco se ha recibido un examen futuro ni se garantiza un 10. Los ejemplos son originales y emplean datos académicos inventados.

## Archivos y cobertura

- Manual: `content/refuerzo-docente-materiales.tex` y `content/fractura-docente-complemento.tex`, integrados desde `main.tex`.
- Cuaderno: `content/problemas-puente-profesor.tex` y `content/fractura-problemas-docentes.tex`, integrados desde `problemas.tex` y persistidos en `scripts/build_companions.py`.
- Pruebas de regresión numérica: `tests/test_matmo_teaching_bridge.py` y `tests/test_matmo_fracture_slides.py`.

| Fuente del profesor | Aspectos reforzados | Problemas nuevos |
|---|---|---|
| Introducción, pp. 2–34 | Aerostatos/aerodinos, estructuras, propulsores, selección por misión y fallo | Preguntas conceptuales en manual |
| Fractura, pp. 4–43 | Clivaje, dúctil-frágil, Inglis, Griffith, campos de punta, geometrías y cribado de validez | PF01–PF07, autocorrección |
| Fatiga, pp. 18–28 | Estimación en aceros, **contradicción detectada** para aluminio, S–N, correctores (k_a,k_t,k_d,k_u,k_c), tensiones medias, flexión | PM02, PM03, simulacro |
| Fluencia, pp. 4–24 | Norton, temperatura, tensión centrífuga en álabe, deformación elástica y acumulada | PM05, simulacro |
| Degradación, pp. 12–29 | Series galvánicas dependientes de medio, intergranularidad, radiación, desgaste y prevención | PM08 |
| END y SHM, pp. 27–34 | Tap-test, C-scan, tomografía; SHM activo/pasivo y local/global; FBG, CVM, piezoeléctricos | PM07, simulacro |
| Formulario 2025V1, p. 1 | (K_t), tres familias de curvas geométricas, Goodman, Basquin, Paris, fluencia; usos y límites | PM01–PM06 |
| Problemas 1, C1.1–C1.3 | (a_c), (K_{IC}), semilongitud, cribado del espesor | PM06 + P07–P10 existentes |
| Problemas 1, C1.4 | Lectura inversa de curva (K_t), radio y tensión | PM01 |
| Problemas 1, C2.1 | Curva S–N, amplitud y número de ciclos | PM02 |
| Problemas 1, C2.2 | Fuerza axial/flexión, factores ambientales, Goodman | PM03 |
| Problemas 1, C2.3 | Paris, comparación de (R) y carga compresiva/cierre | PM04 |
| Problemas 1, C3.1 | Álabe rotatorio, fluencia y variación de temperatura | PM05 |

## Convenciones y conflictos que deben conservarse

1. **Aluminio, fatiga, p. 19.** Las condiciones `σR ≤ 350 MPa` y `σR < 280 MPa` se solapan con factores distintos. No se ha inventado la desigualdad correcta: se documenta como **pendiente de aclaración docente**.
2. **Factores de fatiga, pp. 24–27.** En la convención docente son penalizadores (producto en denominador). Otras convenciones emplean factores reductores; no se mezclan ni se duplica (K_t) ya contabilizado.
3. **Compresión y Paris.** Se distingue `ΔK` nominal del rango efectivo con cierre. El valor de compresión no se sustituye mecánicamente por una intensidad de apertura negativa con interpretación física universal.
4. **Fluencia.** El modelo de álabe emplea tensión uniforme equivalente para reproducir la idealización de ejercicio, declarando que la tensión real varía a lo largo del radio. La unidad de tiempo del prefactor de Norton se conserva explícitamente.
5. **SHM.** No se generalizan frases de las diapositivas según las cuales todo SHM graba en caja negra, detecta todos los eventos o permite rebajar factores de seguridad.
6. **Datos no certificados.** Ningún número de los ejercicios nuevos es una propiedad experimental del material comercial indicado ni instrucción de mantenimiento.

## Controles recomendados antes de cerrar

```sh
python -m unittest tests.test_matmo_teaching_bridge
python3 scripts/build-studium-books.py materiales-mantenimiento-motores --check
python3 scripts/build-studium-books.py materiales-mantenimiento-motores
# Revisar manual y problemas PDF, referencias cruzadas, desbordamientos y ecuaciones.
```

Hasta ejecutar estas comprobaciones y revisar los PDF compilados **no se puede afirmar CI verde, maquetación revisada ni validación matemática independiente**. El estado del libro permanece **EN REVISIÓN** y no se crea automáticamente ninguna release.
