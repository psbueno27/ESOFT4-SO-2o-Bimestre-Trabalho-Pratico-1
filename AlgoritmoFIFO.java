import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class AlgoritmoFIFO {

    public static void main(String[] args) {
        // Sequência de exemplo fornecida no enunciado
        int[] referencias = {7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2};
        int numFrames = 3; // Número de quadros disponíveis

        System.out.println("Iniciando simulação FIFO com " + numFrames + " frames...\n");
        simularFIFO(numFrames, referencias);
    }

    public static void simularFIFO(int numFrames, int[] referencias) {
        // Utilizamos ArrayList para atuar como uma Fila (Queue) e facilitar a impressão do estado
        List<Integer> frames = new ArrayList<>();
        int totalFaults = 0;
        int totalHits = 0;

        for (int ref : referencias) {
            String acao;
            
            // Verifica se a página já está na memória (Page Hit)
            if (frames.contains(ref)) {
                acao = "Page Hit";
                totalHits++;
            } 
            // Caso a página não esteja na memória (Page Fault)
            else {
                totalFaults++;
                
                // Se ainda há espaço nos frames
                if (frames.size() < numFrames) {
                    frames.add(ref);
                    acao = "Page Fault";
                } 
                // Se não há espaço, remove o mais antigo (índice 0) e adiciona o novo no final
                else {
                    int substituido = frames.remove(0);
                    frames.add(ref);
                    acao = "Page Fault (substituiu " + substituido + ")";
                }
            }

            // Exibe o estado da memória após cada referência
            System.out.printf("Referência: %d | Frames: %s | %s | Total Faults: %d%n", 
                              ref, frames.toString(), acao, totalFaults);
        }

        // Cálculo de estatísticas
        double taxaFaltas = ((double) totalFaults / referencias.length) * 100;
        double taxaAcertos = ((double) totalHits / referencias.length) * 100;

        System.out.println("\n--- Estatísticas Finais ---");
        System.out.println("Total de referências analisadas: " + referencias.length);
        System.out.println("Total de Faltas de Página (Page Faults): " + totalFaults);
        System.out.println("Total de Acertos (Page Hits): " + totalHits);
        System.out.printf("Taxa de Faltas de Página (Fault Rate): %.2f%%%n", taxaFaltas);
        System.out.printf("Taxa de Acertos (Hit Rate): %.2f%%%n", taxaAcertos);
    }
}
