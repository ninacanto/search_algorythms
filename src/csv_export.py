import csv
import math


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
