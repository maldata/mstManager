"""
This file is intended to make it easier to run tests.
All test scripts should start with:

from context import *

And this will pull in the top-level packages.

In order to explain briefly, consider this:
http://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time/14132912#14132912

The short story is that when running a top-level script, its name will be
interpreted as __main__. However, when you import a module, its name will be
package.subpackage.subpackage.module. A module can therefore use relative
imports because the full absolute path is in its name.
Top-level scripts cannot.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mstmanager

