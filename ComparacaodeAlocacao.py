# -*- coding: utf-8 -*-
"""Questão 5 - Comparação de desempenho: alocação na pilha x heap.
Uso: python3 questao5.py [operacoes] [repeticoes]   (padrão: 1.000.000 e 5)"""
import gc
import statistics
import sys
import time


class Objeto:
    """Objeto alocado dinamicamente no heap (__slots__ deixa o objeto menor)."""
    __slots__ = ("a", "b", "c")

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c


def funcao_com_variaveis_locais():
    """Variáveis locais: quadro criado e descartado na pilha em cada chamada."""
    a = 1
    b = 2
    c = a + b
    return c


def funcao_com_alocacao_heap():
    """Cria um objeto no heap; ao sair da função ele é destruído e liberado."""
    obj = Objeto(1, 2, 3)
    return None


def medir_tempo(funcao, quantidade):
    """Executa 'funcao' 'quantidade' vezes e devolve o tempo em segundos."""
    inicio = time.perf_counter()
    for _ in range(quantidade):
        funcao()
    return time.perf_counter() - inicio


def ler_parametros(args):
    """Lê operações e repetições da linha de comando, validando as entradas."""
    try:
        quantidade = int(args[1]) if len(args) > 1 else 1_000_000
        repeticoes = int(args[2]) if len(args) > 2 else 5
    except ValueError:
        raise ValueError("os parâmetros devem ser números inteiros.")
    if quantidade <= 0 or repeticoes <= 0:
        raise ValueError("os parâmetros devem ser maiores que zero.")
    return quantidade, repeticoes


def main():
    try:
        quantidade, repeticoes = ler_parametros(sys.argv)
    except ValueError as erro:
        print(f"Erro: {erro}")
        print("Uso: python3 questao5.py [operacoes] [repeticoes]")
        return 1

    print("=" * 60)
    print(" COMPARAÇÃO DE DESEMPENHO: ALOCAÇÃO NA PILHA x HEAP")
    print("=" * 60)
    print(f"Operações por teste : {quantidade:,}".replace(",", "."))
    print(f"Repetições          : {repeticoes}")
    print("-" * 60)
    print(" Execução |  Pilha (s)   |   Heap (s)")
    print("-" * 60)

    # Aquecimento e coletor de lixo desligado, para não distorcer a medição
    medir_tempo(funcao_com_variaveis_locais, 10_000)
    medir_tempo(funcao_com_alocacao_heap, 10_000)
    pilha, heap = [], []
    gc.disable()
    try:
        for i in range(1, repeticoes + 1):
            pilha.append(medir_tempo(funcao_com_variaveis_locais, quantidade))
            heap.append(medir_tempo(funcao_com_alocacao_heap, quantidade))
            print(f"{i:>9} | {pilha[-1]:>12.4f} | {heap[-1]:>12.4f}")
    finally:
        gc.enable()

    m_pilha, m_heap = statistics.mean(pilha), statistics.mean(heap)
    d_pilha, d_heap = statistics.pstdev(pilha), statistics.pstdev(heap)
    ns_pilha = m_pilha / quantidade * 1e9
    ns_heap = m_heap / quantidade * 1e9
    print("-" * 60)
    print(f"Média    | {m_pilha:>12.4f} | {m_heap:>12.4f}")
    print(f"Desvio   | {d_pilha:>12.4f} | {d_heap:>12.4f}")
    print(f"Por op.  | {ns_pilha:>9.1f} ns | {ns_heap:>9.1f} ns")
    print("=" * 60)

    if m_pilha == 0:
        print("Tempo da pilha muito pequeno para calcular a diferença.")
        return 1

    # Diferença percentual (pilha como referência): (heap - pilha) / pilha * 100
    dif = (m_heap - m_pilha) / m_pilha * 100
    comparacao = "lenta" if dif >= 0 else "rápida"
    print("RESULTADO")
    print(f"A alocação no heap foi {abs(dif):.1f}% mais {comparacao} "
          f"que a da pilha ({m_heap / m_pilha:.2f}x o tempo).")
    print("=" * 60)
    return 0


# Análise: a pilha só move um ponteiro (alocar e liberar custam poucas instruções);
# no heap o alocador procura e gerencia blocos, por isso o heap costuma ser mais lento.
# Os tempos variam com a carga do sistema, a CPU e a versão do Python; por isso há
# várias repetições e se usa a média. Em Python todo objeto fica no heap, então o
# teste compara variáveis locais com a criação de objetos.

if __name__ == "__main__":
    sys.exit(main())