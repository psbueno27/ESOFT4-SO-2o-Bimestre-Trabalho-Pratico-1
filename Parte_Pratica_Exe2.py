
# Simulador de Fragmentacao de Memoria
# Algoritmo First-Fit

# Criacao das cinco particoes fixas
particoes = [
    {"tamanho": 100, "processo": None},
    {"tamanho": 150, "processo": None},
    {"tamanho": 200, "processo": None},
    {"tamanho": 250, "processo": None},
    {"tamanho": 300, "processo": None}
]


# Funcao para alocar um processo na primeira particao disponivel
def alocar_processo(nome, tamanho):

    if tamanho <= 0:
        print("Erro: tamanho invalido.")
        return

    # Percorre as particoes utilizando First-Fit
    for i, particao in enumerate(particoes):

        # Verifica se a particao esta livre e possui espaco suficiente
        if particao["processo"] is None and particao["tamanho"] >= tamanho:

            # Armazena as informacoes do processo
            particao["processo"] = {
                "nome": nome,
                "tamanho": tamanho
            }

            # Calcula a fragmentacao interna
            desperdicio = particao["tamanho"] - tamanho

            print("\nProcesso", nome, "alocado com sucesso!")
            print("Particao utilizada:", i + 1)
            print("Tamanho do processo:", tamanho, "unidades")
            print("Fragmentacao interna:", desperdicio, "unidades")

            return

    # Caso nao exista uma particao disponivel
    print("\nFalha ao alocar", nome, ": nao ha particao disponivel.")


# Funcao para liberar a memoria ocupada por um processo
def liberar_processo(nome):

    for particao in particoes:

        if particao["processo"] is not None:

            if particao["processo"]["nome"] == nome:

                particao["processo"] = None
                print("\nProcesso", nome, "liberado com sucesso!")
                return

    print("\nProcesso", nome, "nao encontrado.")


# Funcao para exibir o estado atual da memoria
def exibir_memoria():

    print("\n========== ESTADO DA MEMORIA ==========")

    for i, particao in enumerate(particoes):

        processo = particao["processo"]

        if processo is None:
            print("Particao", i + 1, ":", particao["tamanho"], "unidades - LIVRE")

        else:
            print(
                "Particao", i + 1, ":", particao["tamanho"],
                "unidades -", processo["nome"],
                "(", processo["tamanho"], "unidades)"
            )

    print("=======================================")


# Funcao para calcular a fragmentacao interna total
def fragmentacao_total():

    total = 0

    for particao in particoes:

        processo = particao["processo"]

        if processo is not None:
            total += particao["tamanho"] - processo["tamanho"]

    print("\nFragmentacao interna total:", total, "unidades")


# Execucao da sequencia de testes solicitada

print("INICIANDO SIMULACAO DE MEMORIA")

alocar_processo("P1", 90)
alocar_processo("P2", 140)
alocar_processo("P3", 180)

exibir_memoria()

liberar_processo("P2")

alocar_processo("P4", 100)

alocar_processo("P5", 350)

exibir_memoria()

fragmentacao_total()
