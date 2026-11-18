
import gc
import sys


# 1. CRIAR A CLASSE OBJETO

class Objeto:
    def __init__(self, nome):
        self.nome = nome

        # Cria uma lista grande para simular o uso de memoria
        self.dados = [0] * 1000000

        print(f"Objeto {self.nome} foi criado.")

    def __del__(self):
        print(f"Objeto {self.nome} foi destruído.")


# 2. CRIAR VÁRIAS INSTÂNCIAS DA CLASSE OBJETO

obj1 = Objeto("A")
obj2 = Objeto("B")
obj3 = Objeto("C")
obj4 = Objeto("D")
obj5 = Objeto("E")


# 3. DEMONSTRAR O FUNCIONAMENTO DO GARBAGE COLLECTOR

# Destruição automática por contagem de referências

print("\n Contagem de referências ")

print("Referências ao objeto A:", sys.getrefcount(obj1)) 

# Cria uma segunda referência para o mesmo objeto
referencia = obj1

print("Referências após criar outra variável:", sys.getrefcount(obj1))

# Remove as referências ao objeto A
del obj1
del referencia

print("As referências ao objeto A foram removidas.")

# Remove a referência ao objeto B
del obj2


#Referência circular em um objeto
print("\n Referência circular ")

# O objeto C passa a referenciar a si mesmo
obj3.referencia = obj3

# Remove a referencia externa
del obj3

print("Referência externa removida, mas existe um ciclo.")

# Forca a execucao do Garbage Collector
coletados = gc.collect()

print("Objetos coletados pelo GC:", coletados)

#Ciclo entre dois objetos
print("\n Ciclo entre dois objetos ")

# Os objetos D e E passam a referenciar um ao outro
obj4.outro = obj5
obj5.outro = obj4

# Remove as referências externas
del obj4
del obj5

print("Referências externas removidas.")

# Força a coleta dos objetos que ficaram no ciclo
coletados = gc.collect()

print("Objetos coletados pelo GC:", coletados)


# 4. EXIBIR ESTATÍSTICAS DO COLETOR DE LIXO
print("\n Coleta geracional ")

# Cria novos objetos para demonstrar a coleta geracional
objetos = []

for i in range(5):
    objetos.append(Objeto(f"F{i}"))

# Exibe as estatisticas antes da coleta
print("\nEstatísticas antes da coleta:")
print(gc.get_stats())

# Remove as referencias aos objetos
objetos.clear()

# Forca uma coleta em todas as geracoes
gc.collect()

# Exibe as estatisticas depois da coleta
print("\nEstatisticas depois da coleta:")
print(gc.get_stats())

# Exibe informacoes adicionais do coletor
print("\nLimites das gerações:", gc.get_threshold())
print("Contadores atuais:", gc.get_count())


print("\nPrograma finalizado.")
