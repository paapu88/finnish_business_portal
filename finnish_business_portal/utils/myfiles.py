from typing import Union
from pathlib import Path
def add_home(filepath: Union[str, Path]):
    """
    Add home directory to filename
    Parameters
    ----------
    filepath :  filepath without home

    Returns
    -------
    filepath with $HOME at the beginning

    """
    if str(filepath).startswith("~"):
        filepath = Path(str(filepath).replace("~/", "").replace("~", ""))
        # print(f"home {type(Path.home())}")
        # print(f"filepath {type(filepath)}")
        # print(f"replaced {Path.home().joinpath(str(filepath))}")
        return Path.home().joinpath(filepath)
    elif str(filepath).startswith("$HOME"):
        filepath = filepath.replace("$HOME/", "").replace("$HOME", "")
        return Path.home().joinpath(filepath)
    return Path(filepath)