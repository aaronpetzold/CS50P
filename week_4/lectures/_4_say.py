"""
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

# Website: https://pypi.org/
# pip install ...
"""

import sys

from _6_sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])