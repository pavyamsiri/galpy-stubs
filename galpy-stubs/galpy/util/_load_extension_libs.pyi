from ctypes import CDLL

PY3: bool
_ext_suffix: str
_libgalpy: CDLL | None
_libgalpy_loaded: bool
_libgalpy_actionAngleTorus: CDLL | None
_libgalpy_actionAngleTorus_loaded: bool
_checked_openmp_issue: bool

def load_libgalpy(
    check_openmp_issue: bool = True,
) -> tuple[CDLL | None, bool | None]: ...
def load_libgalpy_actionAngleTorus() -> tuple[CDLL | None, bool | None]: ...
