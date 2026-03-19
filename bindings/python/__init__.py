import os
from pathlib import Path

try:
    from ._build_config import GNC_PY_WHEEL_MODE
except Exception:
    GNC_PY_WHEEL_MODE = False

if GNC_PY_WHEEL_MODE and "GNC_BUILDDIR" not in os.environ:
    site_root = Path(__file__).resolve().parent.parent
    os.environ.setdefault("GNC_UNINSTALLED", "1")
    os.environ["GNC_BUILDDIR"] = str(site_root)
    os.environ.setdefault("GNC_WHEEL_MODE", "1")
    os.environ.setdefault("GNC_SUPPRESS_PREFS_WARNINGS", "1")

# import all the symbols from gnucash_core, so basic gnucash stuff can be
# loaded with:
# >>> from gnucash import thingy
# instead of
# >>> from gnucash.gnucash_core import thingy
from gnucash.gnucash_core import *
from . import app_utils
from . import deprecation
##  @file
#   @brief helper file for the importing of gnucash
#   @author Mark Jenkins, ParIT Worker Co-operative <mark@parit.ca>
#   @author Jeff Green,   ParIT Worker Co-operative <jeff@parit.ca>
#   @ingroup python_bindings
