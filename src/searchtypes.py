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
