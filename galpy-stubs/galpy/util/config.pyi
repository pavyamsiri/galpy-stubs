from configparser import ConfigParser
from os import PathLike

type QuantityLike = object

default_configuration: dict[str, dict[str, str]]
default_filename: str
__config__: ConfigParser
__orig__config__: ConfigParser
cfilename: list[str]
configfilename: str

def check_config(configuration: ConfigParser) -> bool: ...
def fix_config(configuration: ConfigParser | None = None) -> ConfigParser: ...
def write_config(
    filename: str | PathLike[str], configuration: ConfigParser
) -> None: ...
def set_ro(ro: QuantityLike) -> None: ...
def set_vo(vo: QuantityLike) -> None: ...
