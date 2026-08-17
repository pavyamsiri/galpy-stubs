from collections.abc import Sequence

from .Snapshot import Snapshot

def snapshotToMovie(
    snap: Snapshot | Sequence[Snapshot] | object,
    filename: str,
    *args: object,
    **kwargs: object,
) -> None: ...
