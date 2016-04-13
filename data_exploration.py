# -*- coding: utf-8 -*-

import os
from matplotlib import pylab as plt
import pandas as pd
import numpy as np

if __name__ == "__main__":
    
    data = pd.read_csv(os.path.join("jla_cosmo_v2",
                                    "data",
                                    "jla_lcparams.txt"),
                                    delimiter = " ")
    print data.head()