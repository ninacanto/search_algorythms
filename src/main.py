#!/usr/bin/env python3
"""
Benchmark de algoritmos de busca - Versão Python
Executa comparação entre busca sequencial e busca binária.
"""

import random
import time
import csv
import math


class SearchResult:
    def __init__(self, positions_visited, execution_time_ns):
        self.positions_visited = positions_visited
        self.execution_time_ns = execution_time_ns
    
    def __repr__(self):
        return f"SearchResult(positions_visited={self.positions_visited}, execution_time_ns={self.execution_time_ns})"


class BenchmarkResults:
    def __init__(self, size, sequential_avg_case, sequential_worst_case, binary_avg_case, binary_worst_case):
        self.size = size
        self.sequential_avg_case = sequential_avg_case
        self.sequential_worst_case = sequential_worst_case
        self.binary_avg_case = binary_avg_case
        self.binary_worst_case = binary_worst_case
    
    def __repr__(self):
        return f"BenchmarkResults(size={self.size})"


def sequential_search(arr, target):
    """
    Implementação da busca sequencial.
    
    Args:
        arr: Lista de valores inteiros
        target: Valor a ser encontrado
    
    Returns:
        SearchResult com informações sobre a busca
    """
    start = time.time_ns()
    positions_visited = 0
    
    for value in arr:
        positions_visited += 1
        if value == target:
            duration = time.time_ns() - start
            return SearchResult(positions_visited, duration)
    
    duration = time.time_ns() - start
    return SearchResult(positions_visited, duration)


def binary_search(arr, target):
    """
    Implementação da busca binária.
    
    Args:
        arr: Lista ordenada de valores inteiros
        target: Valor a ser encontrado
    
    Returns:
        SearchResult com informações sobre a busca
    """
    start = time.time_ns()
    positions_visited = 0
    left = 0
    right = len(arr)
    
    while left < right:
        positions_visited += 1
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            duration = time.time_ns() - start
            return SearchResult(positions_visited, duration)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    duration = time.time_ns() - start
    return SearchResult(positions_visited, duration)


def export_to_csv(results):
    """
    Exporta os resultados do benchmark para um arquivo CSV.
    
    Args:
        results: Lista de objetos BenchmarkResults
    
    Returns:
        None
    """
    with open("benchmark_results.csv", "w", newline='') as file:
        csv_writer = csv.writer(file)
        
        # Cabeçalho com todas as métricas
        csv_writer.writerow([
            "Size", "Seq_Avg_Time_ns", "Seq_Worst_Time_ns", "Bin_Avg_Time_ns", "Bin_Worst_Time_ns",
            "Seq_Avg_Positions", "Seq_Worst_Positions", "Bin_Avg_Positions", "Bin_Worst_Positions",
            "Time_Speedup_Avg", "Time_Speedup_Worst", "Position_Efficiency_Avg", "Position_Efficiency_Worst", "Theoretical_Log2"
        ])
        
        for result in results:
            size = result.size
            
            # Cálculos de speedup e eficiência
            time_speedup_avg = result.sequential_avg_case.execution_time_ns / result.binary_avg_case.execution_time_ns
            time_speedup_worst = result.sequential_worst_case.execution_time_ns / result.binary_worst_case.execution_time_ns
            
            pos_efficiency_avg = result.sequential_avg_case.positions_visited / result.binary_avg_case.positions_visited
            pos_efficiency_worst = result.sequential_worst_case.positions_visited / result.binary_worst_case.positions_visited
            
            theoretical_log2 = math.log2(size)
            
            # Linha com todos os dados
            csv_writer.writerow([
                size,
                result.sequential_avg_case.execution_time_ns,
                result.sequential_worst_case.execution_time_ns,
                result.binary_avg_case.execution_time_ns,
                result.binary_worst_case.execution_time_ns,
                result.sequential_avg_case.positions_visited,
                result.sequential_worst_case.positions_visited,
                result.binary_avg_case.positions_visited,
                result.binary_worst_case.positions_visited,
                f"{time_speedup_avg:.2f}",
                f"{time_speedup_worst:.2f}",
                f"{pos_efficiency_avg:.2f}",
                f"{pos_efficiency_worst:.2f}",
                f"{theoretical_log2:.2f}"
            ])
    
    print("✅ Dados exportados para: benchmark_results.csv")
    print("📊 Arquivo único com todas as métricas organizadas")


def generate_analysis_summary(results):
    """
    Gera um resumo de análise para os resultados do benchmark.
    
    Args:
        results: Lista de objetos BenchmarkResults
    
    Returns:
        None
    """
    print("\n=== ANÁLISE PARA GRÁFICOS ===")
    
    print("\n📊 COMPLEXIDADE OBSERVADA:")
    for result in results:
        theoretical_log = math.log2(result.size)
        observed_avg = result.binary_avg_case.positions_visited
        observed_worst = result.binary_worst_case.positions_visited
        
        print(f"Tamanho {result.size}: Log₂({result.size}) = {theoretical_log:.1f} | Observado: {observed_avg:.1f} (avg), {observed_worst:.1f} (worst)")
    
    print("\n📈 CRESCIMENTO RELATIVO:")
    if len(results) >= 2:
        for i in range(1, len(results)):
            prev = results[i-1]
            curr = results[i]
            
            size_growth = curr.size / prev.size
            seq_time_growth = curr.sequential_worst_case.execution_time_ns / prev.sequential_worst_case.execution_time_ns
            bin_time_growth = curr.binary_worst_case.execution_time_ns / prev.binary_worst_case.execution_time_ns
            seq_pos_growth = curr.sequential_worst_case.positions_visited / prev.sequential_worst_case.positions_visited
            bin_pos_growth = curr.binary_worst_case.positions_visited / prev.binary_worst_case.positions_visited
            
            print(f"{prev.size}x → {curr.size}x elementos:")
            print(f"  Crescimento: {size_growth:.1f}x | Seq tempo: {seq_time_growth:.1f}x | Bin tempo: {bin_time_growth:.1f}x")
            print(f"  Seq posições: {seq_pos_growth:.1f}x | Bin posições: {bin_pos_growth:.1f}x")


def generate_sorted_array(size):
    """
    Gera uma lista ordenada de inteiros de 1 até size.
    
    Args:
        size: Tamanho da lista a ser gerada
    
    Returns:
        Lista ordenada de inteiros
    """
    return list(range(1, size + 1))


def run_benchmark(size):
    """
    Executa os testes de benchmark para um tamanho específico.
    
    Args:
        size: Tamanho da lista para testes
    
    Returns:
        Objeto BenchmarkResults com os resultados
    """
    arr = generate_sorted_array(size)
    
    random_index = random.randrange(0, size)
    avg_case_target = arr[random_index]
    worst_case_target = size + 1000
    
    print(f"Testando {size} elementos...")
    
    iterations = 1000
    
    # Busca Sequencial - Caso Médio
    seq_avg_time = 0
    seq_avg_positions = 0
    for _ in range(iterations):
        result = sequential_search(arr, avg_case_target)
        seq_avg_time += result.execution_time_ns
        seq_avg_positions += result.positions_visited
    
    sequential_avg_case = SearchResult(
        positions_visited=seq_avg_positions // iterations,
        execution_time_ns=seq_avg_time // iterations
    )
    
    # Busca Sequencial - Pior Caso
    seq_worst_time = 0
    seq_worst_positions = 0
    for _ in range(iterations):
        result = sequential_search(arr, worst_case_target)
        seq_worst_time += result.execution_time_ns
        seq_worst_positions += result.positions_visited
    
    sequential_worst_case = SearchResult(
        positions_visited=seq_worst_positions // iterations,
        execution_time_ns=seq_worst_time // iterations
    )
    
    # Busca Binária - Caso Médio
    bin_avg_time = 0
    bin_avg_positions = 0
    for _ in range(iterations):
        result = binary_search(arr, avg_case_target)
        bin_avg_time += result.execution_time_ns
        bin_avg_positions += result.positions_visited
    
    binary_avg_case = SearchResult(
        positions_visited=bin_avg_positions // iterations,
        execution_time_ns=bin_avg_time // iterations
    )
    
    # Busca Binária - Pior Caso
    bin_worst_time = 0
    bin_worst_positions = 0
    for _ in range(iterations):
        result = binary_search(arr, worst_case_target)
        bin_worst_time += result.execution_time_ns
        bin_worst_positions += result.positions_visited
    
    binary_worst_case = SearchResult(
        positions_visited=bin_worst_positions // iterations,
        execution_time_ns=bin_worst_time // iterations
    )
    
    return BenchmarkResults(
        size=size,
        sequential_avg_case=sequential_avg_case,
        sequential_worst_case=sequential_worst_case,
        binary_avg_case=binary_avg_case,
        binary_worst_case=binary_worst_case
    )


def print_results(results):
    """
    Imprime os resultados do benchmark para um tamanho específico.
    
    Args:
        results: Objeto BenchmarkResults com os resultados
    
    Returns:
        None
    """
    print(f"\n=== RESULTADOS PARA {results.size} ELEMENTOS ===")
    
    print(f"\n{'':<20} {'POS MÉDIA':>12} {'POS PIOR':>12} {'TEMPO MÉD':>12} {'TEMPO PIOR':>12}")
    print(f"{'-' * 72}")
    
    print(f"{'Busca Sequencial':<20} {results.sequential_avg_case.positions_visited:>12} "
          f"{results.sequential_worst_case.positions_visited:>12} "
          f"{f'{results.sequential_avg_case.execution_time_ns}ns':>12} "
          f"{f'{results.sequential_worst_case.execution_time_ns}ns':>12}")
    
    print(f"{'Busca Binária':<20} {results.binary_avg_case.positions_visited:>12} "
          f"{results.binary_worst_case.positions_visited:>12} "
          f"{f'{results.binary_avg_case.execution_time_ns}ns':>12} "
          f"{f'{results.binary_worst_case.execution_time_ns}ns':>12}")
    
    speedup_avg = results.sequential_avg_case.execution_time_ns / results.binary_avg_case.execution_time_ns
    speedup_worst = results.sequential_worst_case.execution_time_ns / results.binary_worst_case.execution_time_ns
    
    print(f"\nSpeedup: {speedup_avg:.1f}x (médio) | {speedup_worst:.1f}x (pior)")


def main():
    """
    Função principal que executa o benchmark completo.
    """
    print("🐍 BENCHMARK: Busca Sequencial vs Busca Binária")
    print("Testando com 1.000 iterações por cenário\n")
    
    sizes = [1_000, 10_000, 100_000]
    all_results = []
    
    for size in sizes:
        results = run_benchmark(size)
        print_results(results)
        all_results.append(results)
        print()
    
    # Exportar dados para CSV
    try:
        export_to_csv(all_results)
    except Exception as e:
        print(f"❌ Erro ao exportar CSV: {e}")
    
    # Análise para criação de gráficos
    generate_analysis_summary(all_results)
    
    print("\n=== RESUMO FINAL ===")
    print("Complexidade: Sequencial O(n) | Binária O(log n)")
    for result in all_results:
        ratio = result.sequential_worst_case.positions_visited / result.binary_worst_case.positions_visited
        print(f"{result.size:>6} elementos: Binária {ratio:.1f}x mais eficiente")
    
    print("\n📋 ARQUIVO GERADO:")
    print("   • benchmark_results.csv (com todas as métricas)")
    print("\n💡 Use esse CSV para criar gráficos no Excel, Python, R, etc.")


if __name__ == "__main__":
    main()
