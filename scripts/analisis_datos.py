
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================
# ANÁLISIS DE ANOMALÍAS DE TEMPERATURA GLOBAL - DATASET GISTEMP
# Fuente: datahub.io/core/global-temp
# Descripción: Las anomalías representan la diferencia respecto
# al promedio base del período 1951-1980
# =============================================================

# Cargamos el dataset de temperaturas globales mensuales
df = pd.read_csv('datos/monthly.csv')

# Filtramos solo la fuente GCAG para mantener consistencia
# GCAG = Global Change Attribution Group (datos más completos)
df = df[df['Source'] == 'GCAG'].copy()

# Extraemos el año desde la columna Year (formato YYYY-MM)
# Usamos str[:4] porque el formato es 'AAAA-MM'
df['Anio'] = df['Year'].str[:4].astype(int)

# Agrupamos por año y calculamos estadísticas anuales
# Esto reduce el ruido mensual y facilita la visualización
resumen = df.groupby('Anio')['Mean'].agg(
    temp_promedio='mean',
    temp_maxima='max',
    temp_minima='min'
).reset_index()

# Mostramos los indicadores en consola
print("=== INDICADORES CLIMÁTICOS ===")
print(f"Temperatura promedio global: {resumen['temp_promedio'].mean():.4f} °C")
print(f"Temperatura máxima registrada: {resumen['temp_maxima'].max():.4f} °C")
print(f"Temperatura mínima registrada: {resumen['temp_minima'].min():.4f} °C")

# Exportamos el resumen anual a CSV para análisis posteriores
resumen.to_csv('resultados/resumen_indicadores.csv', index=False)
print("\nResumen guardado en /resultados/resumen_indicadores.csv")

# Generamos gráfico de evolución de temperatura promedio anual
# La línea punteada en 0 representa el valor base (promedio 1951-1980)
plt.figure(figsize=(12, 5))
plt.plot(resumen['Anio'], resumen['temp_promedio'], color='steelblue', linewidth=1.5)
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8, label='Valor base (1951-1980)')
plt.title('Evolución de la Temperatura Promedio Global (1850 - actualidad)')
plt.xlabel('Año')
plt.ylabel('Anomalía de temperatura (°C)')
plt.legend()
plt.tight_layout()
plt.savefig('resultados/grafico_temperatura.png', dpi=150)
plt.show()
print("Gráfico guardado en /resultados/grafico_temperatura.png")
