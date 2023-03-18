# ModesolverExplorer
Modefield Solver with Richardson Extrapolation

WGInvestigation
This code uses a modesolver (modesolverpy) to estimate the mode field profile of an electromagnetic wave in a dielectric waveguide

Dielectric waveguides are used in nanophotonic circuits and are a common physics problem in electrodynamics courses 
and this modesolver makes it easy to numerically evaluate. 

Important outputs are the mode field diameter as a function of wavelength, polarization, and waveguide geometry

A modern topic in applied physics is the control of the dispersion (the refractive index ~speed of light vs wavelength) in a medium.
This exploration first shows the effect of geometric dispersion. Due to the nanoscopic size of the waveguide, light at different wavelengths
has different relative fractions leaking out of the high-index core. This equates to an effective refractive index that is roughly proportional
to the overalp area of the mode in the core vs the cladding. Longer wavelengths thus have lower effective refractive indices than shorter wavelengths
which equates to 'waveguide dispersion.' This effect is in contrast to material dispersion which has the opposite character for
common nanophotonic materials. Control of the dispersion enables waveguide mixing, nonlinear phase matching, and diffractive structure design

WGInvestigation can be run multiple times with different parameters and should have been turned into a function. 

Anyways, the Step Size vs Beta bit of code outputs a more practical and applied result. Decreasing the step size of the model increases the accuracy
at a cost of increased time. However, the changes in accuracy should monotonically decrease to the true result as the step size --> 0. 
Taking this (physical) assumption, we can perform a series of fast, large-step-size computation and fit a low-order polynomial to extract the 
zero-step-size value. Oscillations can be seen about this curve due to the finite truncation of the physics so large step sizes are not physical.

Taking a subset of the simulations (red dots) and extrapolating to zero (dotted curve) approximates the minimum-step-size simulation
while taking several orders of magnitude less time to compute. 

This was a one day demo program developed at the end of my phd to discuss waveguide dispersion visually

![Simulation Time Vs Step Size](https://user-images.githubusercontent.com/30641156/226084832-62fd76f9-32be-408d-88f7-af21724e1edd.png)

![Step Size vs neffective](https://user-images.githubusercontent.com/30641156/226084833-ec625d6a-f348-4005-b27e-fe6926e757f6.png)
