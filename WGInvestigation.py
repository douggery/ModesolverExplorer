import modesolverpy.mode_solver as ms
import modesolverpy.structure as st
import numpy as np
import time

start_time=time.time()

# All units are relative.  [um] were chosen in this case.
scale_factor=1.0
x_step = 0.020
y_step = 0.020
wg_height = 0.25*scale_factor
wg_width = 0.3*scale_factor
sub_height = (2-wg_height)/2
sub_width = 2.
clad_height = sub_height
n_sub = 1.45
n_wg = 2.01
n_clad = 1.45
film_thickness = wg_height
wavelength = 0.780*scale_factor
angle = 90.

structure = st.RidgeWaveguide(wavelength,
                              x_step,
                              y_step,
                              wg_height,
                              wg_width,
                              sub_height,
                              sub_width,
                              clad_height,
                              n_sub,
                              n_wg,
                              angle,
                              n_clad,
                              film_thickness)

structure.write_to_file('WG Structure, dim=' + str(wg_height) +' by ' + str(wg_width)+'.dat')

mode_solver = ms.ModeSolverSemiVectorial(2, semi_vectorial_method='Ey')
mode_solver.solve(structure)
mode_solver.write_modes_to_file('Mode Structure, dim=' + str(wg_height) + ' by ' + str(wg_width) + 'step size= '+str(x_step)+'.dat')
mode_solver = ms.ModeSolverSemiVectorial(2, semi_vectorial_method='Ex')
mode_solver.solve(structure)
mode_solver.write_modes_to_file('Mode Structure, dim=' + str(wg_height) + ' by ' + str(wg_width) + 'step size= '+str(x_step)+'.dat')

print("----- %s seconds -----" % (time.time()-start_time))