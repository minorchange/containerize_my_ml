import os
import sys


def test_find_and_load_model():
    # Make sure it also works when called from parent repo
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(current_dir_path)

    from find_model import find_and_load_model

    mc = find_and_load_model()
    m = mc()
