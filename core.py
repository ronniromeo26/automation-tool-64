import concurrent.futures
from functools import lru_cache
from typing import Any, Callable, Dict, List, Generator


class CorePipeline:
    """High-performance batch processing pipeline with cached routing and worker thread pooling."""

    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self._executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

    @staticmethod
    @lru_cache(maxsize=1024)
    def _fast_transform_key(key: str) -> str:
        """Cache key normalization to avoid redundant string processing overhead."""
        return key.strip().lower().replace(" ", "_")

    def _chunk_items(self, items: List[Any], chunk_size: int) -> Generator[List[Any], None, None]:
        """Yield memory-efficient chunks from the input collection."""
        for i in range(0, len(items), chunk_size):
            yield items[i : i + chunk_size]

    def execute_batch(self, items: List[Dict[str, Any]], handler: Callable[[Dict[str, Any]], Any], chunk_size: int = 50) -> List[Any]:
        """Executes worker operations concurrently across optimized dataset chunks."""
        results: List[Any] = []
        chunks = list(self._chunk_items(items, chunk_size))

        futures = [
            self._executor.submit(self._process_chunk, chunk, handler)
            for chunk in chunks
        ]

        for future in concurrent.futures.as_completed(futures):
            results.extend(future.result())

        return results

    def _process_chunk(self, chunk: List[Dict[str, Any]], handler: Callable[[Dict[str, Any]], Any]) -> List[Any]:
        """Processes an individual chunk using cached transformations."""
        chunk_results = []
        for item in chunk:
            normalized_item = {
                self._fast_transform_key(k): v
                for k, v in item.items()
            }
            chunk_results.append(handler(normalized_item))
        return chunk_results

    def shutdown(self) -> None:
        """Cleanly release background thread pool allocation."""
        self._executor.shutdown(wait=True)
