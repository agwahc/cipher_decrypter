import os
import dir


def reset():
    path = dir.rand_tmp()
    path2 = dir.fill_tmp()
    os.remove(path)
    os.remove(path2)
