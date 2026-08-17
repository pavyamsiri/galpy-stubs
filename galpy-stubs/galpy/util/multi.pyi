from collections.abc import Callable, Sequence

def parallel_map[T, U](
    function: Callable[[T], U],
    sequence: Sequence[T],
    numcores: int | None = None,
    progressbar: bool = False,
) -> map[U] | list[U]: ...
