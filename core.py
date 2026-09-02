import time
from functools import lru_cache
from typing import List, Dict, Any

class CoreEngine:
    """Core processing engine optimized for performance."""

    def __init__(self, cache_size: int = 256):
        self.cache_size = cache_size
        self._cache: Dict[str, Any] = {}

    @lru_cache(maxsize=256)
    def _compute_heavy(self, key: str) -> float:
        """Simulate heavy computation. Caching avoids recomputation."""
        time.sleep(0.01)
        return hash(key) % 1000 / 100.0

    def process_data(self, data_items: List[Dict[str, Any]]) -> List[float]:
        """Process items using cached heavy computation."""
        results = []
        for item in data_items:
            key = str(sorted(item.items()))
            result = self._compute_heavy(key)
            results.append(result)
        return results

    def batch_process(self, all_data: List[List[Dict[str, Any]]]) -> List[List[float]]:
        """Batch processing to minimize function call overhead."""
        batch_results = []
        for batch in all_data:
            batch_results.append(self.process_data(batch))
        return batch_results


def optimize_list(items: List[int]) -> List[int]:
    """Optimized list processing using comprehension."""
    return [x * 2 + 1 for x in items if x % 2 == 0]


if __name__ == "__main__":
    engine = CoreEngine()
    sample = [{"id": i, "val": i**2} for i in range(50)]
    start_time = time.time()
    res = engine.process_data(sample)
    elapsed = time.time() - start_time
    print(f"Processed {len(sample)} items in {elapsed:.4f}s")
    opt = optimize_list(list(range(100)))
    print(f"Optimized list length: {len(opt)}")