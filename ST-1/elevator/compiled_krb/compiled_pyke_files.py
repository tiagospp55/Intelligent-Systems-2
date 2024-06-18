# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'floors.kfb'):
           [1710097450.5797598, 'floors.fbc'],
         ('', '', 'elevator_control.krb'):
           [1710097450.591412, 'elevator_control_plans.py', 'elevator_control_bc.py'],
        },
        compiler_version)

