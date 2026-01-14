# copa-upsets-albacete-real-madrid
Probability of upsets: Real Madrid eliminated by 2nd tier or lower teams (Copa del Rey)
# Copa del Rey Upsets: Real Madrid eliminado por equipos de 2ª o inferior (1940–actualidad)

Este repositorio analiza, desde un enfoque de Data Analytics, la frecuencia con la que el Real Madrid ha sido eliminado en la Copa del Rey (incluida la Copa del Generalísimo) por equipos de Segunda División o categorías inferiores.

## Objetivo
Estimar la probabilidad histórica de un "upset" definido como:

> Real Madrid eliminado en Copa por un rival de tier >= 2  
(tier 2 = Segunda División, tier 3+ = categorías inferiores)

## Alcance temporal
- Temporadas incluidas: 1940–41 a 2024–25 (inclusive)
- Competición: Copa del Rey + Copa del Generalísimo (misma continuidad histórica)

## KPI principal (resultado)
- Upsets (tier >= 2): 7
- Temporadas analizadas: 85
- p(upset): 8.2%
- Equivalencia: 1 de cada 12 Copas (aprox.)

## Datasets
### `data/processed/rm_copa_eliminations_low_tier.csv`
Lista de temporadas (en el rango) donde el Real Madrid fue eliminado por equipos de 2ª o inferior.

### `data/raw/seed_cases.csv`
Dataset semilla con rondas/formato/resultado cuando se dispone en fuentes.

## Notebook reproducible
- `notebooks/01_analysis.py` calcula:
  - p(upset)
  - 1 de cada N
  - distribución por tier

## Metodología
1. Definir evento de upset: eliminación por rival tier >= 2.
2. Construir dataset de casos (numerador).
3. Definir universo temporal (denominador): temporadas 1940–41 a 2024–25 inclusive.
4. Calcular:
   - p = upsets / temporadas
   - N = 1 / p

## Limitaciones
- Este repo modela probabilidad por edición/temporada (unidad = año), no por partido.
- Los tiers se basan en categoría del rival en esa temporada.

## Fuentes
Ver `data/raw/sources.md`.
