#!/usr/bin/env python
# -*- coding:utf-8

import unittest
from mpi4py import MPI
from sample import foo


class TestSample(unittest.TestCase):
    def test_foo(self):
        comm = MPI.COMM_WORLD
        rank = comm.Get_rank()
        self.assertEqual(rank, foo.bar())
