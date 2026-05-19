
import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset de temperaturas globales mensuales
df = pd.read_csv('datos/monthly.csv')

# Filtramos solo la fuente GCAG para mantener consistencia
df = df[df['Source'] == 'GCAG'].copy()

# Extraemos el año desde la columna Year (formato YYYY-MM)
df['Anio'] = df['Year'].str[:4].astype(int)

# Calculamos indicadores por año
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

# Guardamos el resumen en /resultados
resumen.to_csv('resultados/resumen_indicadores.csv', index=False)
print("\nResumen guardado en /resultados/resumen_indicadores.csv")

# Generamos gráfico de evolución de temperatura promedio anual
plt.figure(figsize=(12, 5))
plt.plot(resumen['Anio'], resumen['temp_promedio'], color='steelblue', linewidth=1.5)
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.title('Evolución de la Temperatura Promedio Global (1850 - actualidad)')
plt.xlabel('Año')
plt.ylabel('Anomalía de temperatura (°C)')
plt.tight_layout()
plt.savefig('resultados/grafico_temperatura.png', dpi=150)
plt.show()
print("Gráfico guardado en /resultados/grafico_temperatura.png")
