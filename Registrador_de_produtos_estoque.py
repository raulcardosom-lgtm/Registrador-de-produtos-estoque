estoque = {}  # Lista do estoque pra registrar os produtos


# função para registrar produtos na lista estoque
def registrar_produto(dados_estoque):
    nome = input("Nome do produto: ").strip().lower()

    if nome in dados_estoque:
        print("Produto já cadastrado!")
        return

    quantidade = int(input("Qual a quantidade?: "))
    Preco = float(input("Qual é o preço unitário?: R$"))

    dados_estoque[nome] = {"quantidade": quantidade, "preco": Preco}
    print("Produto cadastrado com sucesso!")
    return


# função para buscar os produtos na lista estoque
def buscar_produto(nome, dados_estoque):
    if nome in dados_estoque:
        return dados_estoque[nome]
    return None


while True:  # Loop do menu principal
    print("\n" + "=" * 35)
    print("      SISTEMA DE ESTOQUE ATIVO     ")
    print("=" * 35)
    print("[1] Consultar Produto")
    print("[2] Registrar produto")
    print("[3] Sair do sistema")
    if not estoque:  # aviso caso o estoque esteja vazio
        print("-" * 35)
        print("O estoque está vazio!")
    print("-" * 35)

    opcao = input("O que deseja fazer? ").strip()

    if opcao == "1":  # caminho para consultar produtos
        if not estoque:
            print("-" * 35)
            print("O estoque está vazio!")
            input("Precione [ENTER] para continuar...")
            continue
        nome_produto = input("Qual produto deseja consultar? ").strip().lower()
        info = buscar_produto(nome_produto, estoque)
        if info is not None:
            print(f"\nProduto: {nome_produto.title()}")
            print(f"Estoque atual: {info['quantidade']} unidades")
            print(f"Preço unitário: R${info['preco']:.2f}")
        else:
            print("Produto não encontrado!")
        input("\nPressione [Enter] para continuar...")

    elif opcao == "2":  # caminho para registrar produtos
        registrar_produto(estoque)
        input("\nPressione [Enter] para continuar...")

    elif opcao == "3":  # caminho para sair do sistema
        print("\nEncerrando terminal. Até mais!")
        break
    else:  # else para caso o usuário digite uma opção inválida
        print("\nOpção inválida! Escolha apenas 1, 2 e 3.")
        input("Pressione [Enter] para tentar novamente...")
