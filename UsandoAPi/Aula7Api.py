import requests
import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt

username = "YanGabrielton"

# Requisição para pegar os repositórios do usuário
repos_url = f"https://api.github.com/users/{username}/repos"
repos_response = requests.get(repos_url)

if repos_response.status_code == 200:
    repos_data = repos_response.json()
    language_totals = defaultdict(int)

    for repo in repos_data:
        repo_name = repo['name']
        languages_url = f"https://api.github.com/repos/{username}/{repo_name}/languages"
        lang_response = requests.get(languages_url)

        if lang_response.status_code == 200:
            languages = lang_response.json()
            for lang, bytes_count in languages.items():
                language_totals[lang] += bytes_count

    # Criando DataFrame
    df_languages = pd.DataFrame(list(language_totals.items()), columns=["Linguagem", "Bytes"])
    df_languages = df_languages.sort_values(by="Bytes", ascending=True)  # ordem crescente para barra horizontal
    total_bytes = df_languages["Bytes"].sum()
    df_languages["Porcentagem"] = (df_languages["Bytes"] / total_bytes) * 100

    print("\nLinguagens mais usadas pelo usuário:")
    print(df_languages)

    # Gráfico de barras horizontais
    plt.figure(figsize=(10, 6))
    bars = plt.barh(df_languages["Linguagem"], df_languages["Bytes"], color='skyblue')
    plt.xlabel("Bytes de Código")
    plt.title(f"Linguagens mais usadas por {username}")

    # Adicionando os valores nas barras
    for bar, percent in zip(bars, df_languages["Porcentagem"]):
        width = bar.get_width()
        plt.text(width + 500, bar.get_y() + bar.get_height()/2, f"{percent:.1f}%", va='center')

    plt.tight_layout()
    plt.savefig("grafico_barras_linguagens.png", dpi=300)
    plt.show()

else:
    print("Erro ao buscar repositórios do usuário.")
