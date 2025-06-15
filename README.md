# 🐍 Search Algorithms Benchmark

Comparação de desempenho entre **Busca Sequencial** e **Busca Binária** implementada em Python.

## Especificações do Estudo

### Algoritmos Testados

- **Busca Sequencial** - O(n)
- **Busca Binária** - O(log n)

### Tamanhos de Entrada

- 1.000 elementos ordenados
- 10.000 elementos ordenados
- 100.000 elementos ordenados

### Cenários de Teste

- **Caso Médio**: Elemento em posição aleatória
- **Pior Caso**: Elemento não presente na estrutura

### Métricas Coletadas

- **Tempo de execução** (nanossegundos)
- **Quantidade de posições visitadas**

## Como Executar

```bash
# Clonar o repositório
git clone <repository-url>
cd search_benchmark

# Executar o benchmark em Python
python main.py
```

## Resultados

O programa gera um arquivo `benchmark_results.csv` com todas as métricas coletadas, incluindo:

- Tempos de execução para cada algoritmo e cenário
- Número de posições visitadas
- Speedup e eficiência comparativa
- Valores teóricos vs observados

## Dependências

- Python 3.6+
- Módulos da biblioteca padrão (random, time, csv, math)

## Saída

- `benchmark_results.csv` - Dados completos para análise
- Relatório no console com métricas principais
