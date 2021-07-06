import re
from os import environ
from pathlib import Path
from .fake_data import generate
from .io import (
    epochs_from_hdf,
    epochs_from_dataframe,
    load_grid,
    epochs_from_feather,
)
from .models import run_model, lm, lmer
from . import utils, defaults

__version__ = "0.5.1.dev5"

# for use by pytests and docs
DATA_DIR = Path(__file__).parent / "data"


def get_ver():
    """return version string"""
    pf_ver = re.search(r"(?P<ver_str>\d+\.\d+\.\d+\S*)", __version__)

    if pf_ver is None:
        msg = f"""Illegal fitgrid __version__: {__version__}
        fitgrid __init__.py must have an X.Y.Z semantic version, e.g.,

        __version__ = '0.0.0'
        __version__ = '0.0.0.dev0'
        __version__ = '0.0.0rc1'

        """
        raise Exception(msg)
    else:
        return pf_ver["ver_str"]
