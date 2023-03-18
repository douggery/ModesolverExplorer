import modesolverpy.mode_solver as ms
import modesolverpy.structure as st
import numpy as np
import time

import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from lmfit.models import Model

def exp_decay(xdata,offset,decay_length,amplitude):
      f=[amplitude*(np.e**(decay_length*val))+offset for val in xdata]
      return f

def second_order_poly(xdata,offset,c1,c2):
      f=[offset+c1*val+c2*val**2 for val in xdata]
      return f

Step_sizes=[2.5,5,7.5,10,12.5,15,17.5,20,22.5,25,30,40,50]
Times_to_simulate=[14325,609,201,30,7.88,5.5,3.4,3.88,3,2.4,1.66,1.4,1.3]
neff_Ex=[1.596,1.598,1.604,1.602,1.604,1.610,1.615,1.602,1.620,1.614,1.631,1.658,1.629]
neff_Ey=[1.579,1.580,1.587,1.583,1.585,1.591,1.599,1.590,1.607,1.592,1.614,1.637,1.603]

# plt.plot(Step_sizes,Times_to_simulate,label='Simulation Time')
# plt.plot(Step_sizes,neff_Ex,'o',color='b',label='n$_{eff}$ E$_x$')
# plt.plot(Step_sizes,neff_Ey,'o',color='g',label='n$_{eff}$ E$_y$')
plt.plot(Step_sizes,neff_Ex,color='b')
plt.plot(Step_sizes,neff_Ey,color='g')

# exp_model=Model(exp_decay)

# params=exp_model.make_params()

# params.add('offset',min=1,max=3)
# params.add('decay_length',min=0.001,max=10)
# params.add('amplitude',min=0.1,max=10)

# result=exp_model.fit(neff_Ey,params,xdata=Step_sizes,offset=1.58,decay_length=0.005,amplitude=1,fit_kws={'maxfev':1000})

# plt.plot(Step_sizes,result.best_fit,'r:')

depth=5

second_model=Model(second_order_poly)

params=second_model.make_params()

params.add('offset',min=1,max=3)
params.add('c1',min=0.000001,max=10)
params.add('c2',min=0.000001,max=10)

result=second_model.fit(neff_Ex[depth:-1],params,xdata=Step_sizes[depth:-1],offset=2,c1=0.001,c2=0.001,fit_kws={'maxfev':1000})
coeff=result.params
# print(coeff)

plt.plot(Step_sizes,neff_Ex,'o',color='b',label='Simulated n$_{eff}$ Ex')
plt.plot(Step_sizes,neff_Ex,color='b')
plt.plot(Step_sizes[depth:-1],neff_Ex[depth:-1],'o',color='r',label='Data selected for E$_x$ fit')

plt.plot(Step_sizes,second_order_poly(Step_sizes,offset=coeff['offset'],c1=coeff['c1'],c2=coeff['c2']),'--',color='r',label='Best Fit Extrapolation E$_x$')
#
second_model=Model(second_order_poly)

params=second_model.make_params()

params.add('offset',min=1,max=3)
params.add('c1',min=0.000001,max=10)
params.add('c2',min=0.000001,max=10)

result=second_model.fit(neff_Ey[depth:-1],params,xdata=Step_sizes[depth:-1],offset=2,c1=0.001,c2=0.001,fit_kws={'maxfev':1000})
coeff=result.params
# print(coeff)

plt.plot(Step_sizes,neff_Ey,'o',color='g',label='Simulated n$_{eff}$ Ey')
plt.plot(Step_sizes,neff_Ey,color='g')
plt.plot(Step_sizes[depth:-1],neff_Ey[depth:-1],'o',color='r',label='Data selected for E$_y$ fit')

plt.plot(Step_sizes,second_order_poly(Step_sizes,offset=coeff['offset'],c1=coeff['c1'],c2=coeff['c2']),'--',color='r',label='Best Fit Extrapolation E$_y$')

plt.legend()
plt.title('Step Size Vs Simulated n$_{effective}$')

plt.xlabel('Step Size (nm)')
plt.ylabel('Simulated n$_{effective}$ Value')

plt.show()

n_eff_predicted=second_order_poly([2.5],offset=coeff['offset'],c1=coeff['c1'],c2=coeff['c2'])[0]
n_eff_predicted_at_zero=second_order_poly([0],offset=coeff['offset'],c1=coeff['c1'],c2=coeff['c2'])[0]
print('predicted value at 2.5 nm step size: '+str(np.round(n_eff_predicted,3)))
diff_from_actual=n_eff_predicted-neff_Ey[0]
print('difference from value at 2.5 nm step size is ' +str(np.round(diff_from_actual,3)))
print('the percent error is '+str(np.round(100*diff_from_actual/n_eff_predicted,3))+'%')
print('the predicted value at 0 nm step size is '+str(np.round(n_eff_predicted_at_zero,3)))

predicted_improvement=neff_Ey[depth]-n_eff_predicted
print('the predicted improvement over the last used data point is '+str(np.round(predicted_improvement,2)))

print('with a percent error improvement of '+str(np.round(100*predicted_improvement/n_eff_predicted,2))+'%')

plt.semilogy(Step_sizes,Times_to_simulate,color='g')
plt.title('Step size vs Simulation Time')
plt.xlabel('Step Size (nm)')
plt.ylabel('Simulation Time (s)')

plt.show()