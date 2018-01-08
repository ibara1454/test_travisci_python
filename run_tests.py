#!/usr/bin/env python
# -*- coding:utf-8

# Run this test with
# `mpiexec -n 1 python run_tests.py`
#

from unittest import TestLoader, TextTestRunner

if __name__ == '__main__':
    path = 'test'
    loader = TestLoader()
    test = loader.discover(path)
    runner = TextTestRunner(verbosity=2)
    runner.run(test)
