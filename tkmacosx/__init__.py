import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from basewidget import *
from variables import *
from widget import *
from colors import *

if __name__ == "__main__":
    demo_sframe()
    demo_button()
    demo_colorvar()
