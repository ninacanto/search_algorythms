# 🐍 Search Algorithms Benchmark

Comparação de desempenho entre **Busca Sequencial** e **Busca Binária** implementada em Python.

> Nota: Este projeto também possui uma implementação em Rust disponível na pasta `rust_version/`.

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

## Análise Gráfica

Os dados coletados foram analisados e visualizados em gráficos interativos:

**[Gráficos e Análise Completa](https://colab.research.google.com/drive/1X3MSX1ADwnVWsTnTZruGSonPsenqh43v?usp=sharing)**

### Principais Conclusões

- A busca binária mantém performance quase constante independente do tamanho
- A busca sequencial cresce linearmente com o tamanho da entrada
- Speedup varia de **111x** (1K elementos) até **6.250x** (100K elementos)
- O comportamento prático confirma a análise assintótica teórica

## Estrutura do Projeto

```
├── main.py         # Script principal com todo o código integrado
└── python_version/ # Versão modularizada (alternativa)
    ├── __init__.py
    ├── main.py
    ├── types.py
    ├── search.py
    └── csv_export.py
```

## Dependências

- Python 3.6+
- Módulos da biblioteca padrão (random, time, csv, math)

## Saída

- `benchmark_results.csv` - Dados completos para análise
- Relatório no console com métricas principais
