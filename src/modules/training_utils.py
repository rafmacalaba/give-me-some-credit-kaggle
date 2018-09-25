import numpy as np
import pandas as pd
from contextlib import contextmanager
import time
import logging


@contextmanager
def timing(name):
    t0 = time.time()
    yield
    
    log_out = 'Fragment [{}] done in {:.2f} s\n'.format(name, time.time() - t0)
    print(log_out)
    logging.info(log_out)


def round_float_to(number, round_to=0.05):
    return round(number / round_to) * round_to


def get_round_num(num, round_num):
    return int((round_num * (num // round_num)) + round_num)


def get_opt_val_seeds(size, seed=1030):
    np.random.seed(seed)
    opt_val_seeds = np.random.choice([42, 1029, 610, 514], size=size, replace=True)
    
    return opt_val_seeds


def make_sub(preds, test_feat):
    sub = pd.DataFrame(
        data=preds,
        columns=['Probability'],
        index=test_feat.index
    )
    
    ids = np.arange(1,101504)
    sub["Id"] = ids
    return sub[['Id', 'Probability']]
