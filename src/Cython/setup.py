from distutils.core import setup

from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["c_calculate_distance.pyx",
                           "c_cooling.pyx",
                           "c_initialization.pyx",
                           "c_metropolis_transition.pyx",
                           "c_replica_transition.pyx"])
)
