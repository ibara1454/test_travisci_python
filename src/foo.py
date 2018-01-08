#!usr/bin/env python

import numpy as np
from mpi4py import MPI


def bar():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    return rank
