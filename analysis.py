import pandas as pd
from factor_analyzer import FactorAnalyzer
import numpy as np

def run_unit_5_analysis(file_path):
    # Cargar datos
    df = pd.read_csv(file_path)
    
    # Limpiar nombres de columnas si es necesario
    df.columns = [c.strip().replace('"', '') for c in df.columns]

    print("--- Unit 5: Factorial Structure Analysis ---")

    # 1. Configurar el Análisis Factorial
    # Usamos 2 factores y rotación Oblimin según la práctica
    fa = FactorAnalyzer(n_factors=2, rotation='oblimin', method='principal')
    fa.fit(df)

    # 2. Obtener la Matriz de Cargas (Factor Loadings)
    loadings = pd.DataFrame(
        fa.loadings_, 
        index=df.columns, 
        columns=['Factor 1', 'Factor 2']
    )

    print("\n[Factor Loadings Matrix]")
    print(loadings.round(3))

    # 3. Identificar Ítems Inversos (Cargas negativas significativas)
    print("\n[Detection of Reverse Items]")
    for factor in loadings.columns:
        reverse_items = loadings[loadings[factor] < -0.4].index.tolist()
        if reverse_items:
            print(f"Potential reverse items in {factor}: {reverse_items}")

    # 4. Varianza Explicada
    ev, v = fa.get_factor_variance()
    print(f"\nCumulative Variance Explained: {v[2]*100:.2f}%")

if __name__ == "__main__":
    # Asegúrate de que el nombre coincida con tu archivo subido
    run_unit_5_analysis('BASE DE DATOS 5 (1).csv')
