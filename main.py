from src.analisador import AnalisadorDados


def menu():
    print("SISTEMA DE ANÁLISE DE DADOS (KAGGLE)")

    try:
        analisador = AnalisadorDados("data/vgsales.csv")
    except FileNotFoundError:
        print("Erro: Arquivo 'data/vgsales.csv' não encontrado!")
        print("Baixe o dataset no Kaggle e salve dentro da pasta 'data/'.")
        return

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("[1] Resumo geral e médias de vendas")
        print("[2] Agrupar vendas por gênero (GroupBy)")
        print("[3] Filtrar jogos por plataforma")
        print("[4] Gráfico de Barras: Vendas por Gênero")
        print("[5] Gráfico de Linha: Vendas por Ano")
        print("[6] Gráfico Histograma: Distribuição das Vendas")
        print("[0] Sair")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                analisador.mostrar_resumo()
            elif opcao == 2:
                analisador.agrupar_por_genero()
            elif opcao == 3:
                plat = input("Digite a sigla da plataforma (ex: Wii, DS, PS2, X360): ").strip()
                analisador.filtrar_plataforma(plat)
            elif opcao == 4:
                print("Gerando gráfico de barras...")
                analisador.grafico_barras_genero()
            elif opcao == 5:
                print("Gerando gráfico de linha...")
                analisador.grafico_linha_anos()
            elif opcao == 6:
                print("Gerando histograma...")
                analisador.grafico_histograma_vendas()
            elif opcao == 0:
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida! Digite um número entre 0 e 6.")
        except ValueError:
            print("Erro: digite apenas números!")


if __name__ == "__main__":
    menu()