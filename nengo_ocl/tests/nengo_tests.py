"""
Black-box testing of the sim_ocl Simulator.
"""
import sys

import pyopencl as cl
import pytest

import nengo
import nengo.tests.test_synapses
from nengo.utils.testing import allclose

from nengo_ocl import sim_ocl

ctx = cl.create_some_context()


class OclSimulator(sim_ocl.Simulator):
    def __init__(self, *args, **kwargs):
        super(OclSimulator, self).__init__(*args, context=ctx, **kwargs)


def allclose_tol(*args, **kwargs):
    """Use looser tolerance"""
    kwargs.setdefault('atol', 1e-7)
    return allclose(*args, **kwargs)


nengo.tests.test_synapses.allclose = allclose_tol  # looser tolerances


if __name__ == '__main__':
    # To profile, run `python -m cProfile -o test_sim_ocl.log test_sim_ocl.py`.
    # Appending the argument `-k <filter>` allows you to control which tests
    # are run (e.g. `-k "test_ensemble."` runs all tests in test_ensemble.py).
    pytest.main(sys.argv)
