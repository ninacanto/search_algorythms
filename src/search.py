import time
# Use importação relativa quando usado como módulo, ou absoluta quando executado como script
try:
    from .searchtypes import SearchResult
except ImportError:
    # Quando executado diretamente como script
    from types import SearchResult


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
