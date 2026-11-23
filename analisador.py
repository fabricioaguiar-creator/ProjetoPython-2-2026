import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AnalisadorDados:
    def __init__(self, caminho_csv):
        # Lê o arquivo CSV e remove linhas com dados vazios
        self.df = pd.read_csv(caminho_csv)
        total_antes = len(self.df)
        self.df = self.df.dropna()
        self.df["Year"] = self.df["Year"].astype(int)
        total_depois = len(self.df)

        print(f"Base carregada com sucesso! ({total_depois} registros válidos de {total_antes})")

    def mostrar_resumo(self):
        print("\n--- Resumo Estatístico das Vendas (em milhões) ---")
        print(f"Total de jogos analisados: {len(self.df)}")
        print(f"Média de Vendas Globais: {self.df['Global_Sales'].mean():.2f}")
        print(f"Média América do Norte:  {self.df['NA_Sales'].mean():.2f}")
        print(f"Média Europa:            {self.df['EU_Sales'].mean():.2f}")
        print(f"Média Japão:             {self.df['JP_Sales'].mean():.2f}")

    def agrupar_por_genero(self):
        print("\nVendas Globais por Gênero")
        resumo = self.df.groupby("Genre")["Global_Sales"].agg(["count", "sum", "mean"])
        resumo.columns = ["Qtd Jogos", "Total Vendas", "Média Vendas"]
        resumo = resumo.sort_values(by="Total Vendas", ascending=False)
        print(resumo.round(2))

    def filtrar_plataforma(self, plataforma):
        filtrado = self.df[self.df["Platform"].str.upper() == plataforma.upper()]

        if filtrado.empty:
            print(f"\nNenhum jogo encontrado para a plataforma '{plataforma}'.")
            plataformas_disp = ", ".join(self.df["Platform"].unique())
            print(f"Plataformas disponíveis na base: {plataformas_disp}")
            return

        print(f"\nJogos da Plataforma: {plataforma.upper()}")
        print(f"Quantidade de jogos: {len(filtrado)}")
        print(f"Média de vendas globais: {filtrado['Global_Sales'].mean():.2f} milhões")
        print("\nTop 5 jogos mais vendidos:")
        top5 = filtrado[["Name", "Year", "Genre", "Global_Sales"]].head(5)
        print(top5.to_string(index=False))

    def grafico_barras_genero(self):
        dados = self.df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False).reset_index()

        plt.figure(figsize=(10, 5))
        sns.barplot(data=dados, x="Genre", y="Global_Sales")
        plt.title("Total de Vendas Globais por Gênero de Jogo")
        plt.xlabel("Gênero")
        plt.ylabel("Vendas Globais (em milhões)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def grafico_linha_anos(self):
        dados = self.df.groupby("Year")["Global_Sales"].sum()

        plt.figure(figsize=(10, 5))
        plt.plot(dados.index, dados.values, marker="o", color="royalblue", linewidth=2)
        plt.title("Evolução das Vendas Globais de Jogos por Ano")
        plt.xlabel("Ano de Lançamento")
        plt.ylabel("Vendas Globais (em milhões)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def grafico_histograma_vendas(self):
        plt.figure(figsize=(10, 5))
        sns.histplot(self.df["Global_Sales"], bins=15, kde=True, color="teal")
        plt.title("Distribuição das Vendas Globais por Jogo")
        plt.xlabel("Vendas Globais (em milhões)")
        plt.ylabel("Quantidade de Jogos")
        plt.tight_layout()
        plt.show()