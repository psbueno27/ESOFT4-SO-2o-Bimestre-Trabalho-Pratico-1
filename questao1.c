#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
 
int main() {
 
    // 1. Declaração de um array estático com 5 inteiros
    int arrayEstatico[5];
 
    // 2. Preenchimento do array estático com valores de 1 a 5
    for (int i = 0; i < 5; i++) {
        arrayEstatico[i] = i + 1;
    }
 
    // 3. Alocação dinâmica de memória para 10 inteiros
    int *arrayDinamico = malloc(10 * sizeof(int));
 
    // Verifica se a alocação foi realizada corretamente
    if (arrayDinamico == NULL) {
        printf("Erro: não foi possível alocar memória.\n");
        return 1;
    }
 
    // 4. Preenchimento do array dinâmico com valores de 10 a 19
    for (int i = 0; i < 10; i++) {
        arrayDinamico[i] = i + 10;
    }
 
    // 5. Exibição dos valores e endereços do array estático
    printf("=== ARRAY ESTATICO ===\n");
    for (int i = 0; i < 5; i++) {
        printf("Valor: %d | Endereco: %p\n",
               arrayEstatico[i], (void *)&arrayEstatico[i]);
    }
 
    // 6. Exibição dos valores e endereços do array dinâmico
    printf("\n=== ARRAY DINAMICO ===\n");
    for (int i = 0; i < 10; i++) {
        printf("Valor: %d | Endereco: %p\n",
               arrayDinamico[i], (void *)&arrayDinamico[i]);
    }
 
    // 7. Exibição dos endereços iniciais dos dois arrays
    printf("\n=== COMPARACAO DE ENDERECOS ===\n");
    printf("Endereco do array estatico: %p\n", (void *)arrayEstatico);
    printf("Endereco do array dinamico: %p\n", (void *)arrayDinamico);
 
    // Calcula a diferença numérica entre os endereços, em bytes
    uintptr_t enderecoEstatico = (uintptr_t)arrayEstatico;
    uintptr_t enderecoDinamico = (uintptr_t)arrayDinamico;
 
    if (enderecoEstatico > enderecoDinamico) {
        printf("Diferenca entre enderecos: %llu bytes\n",
               (unsigned long long)(enderecoEstatico - enderecoDinamico));
    } else {
        printf("Diferenca entre enderecos: %llu bytes\n",
               (unsigned long long)(enderecoDinamico - enderecoEstatico));
    }
 
    // 8. Liberação da memória alocada dinamicamente
    free(arrayDinamico);
    printf("\nMemoria dinamica liberada com sucesso!\n");
 
    return 0;
}
