# Group Resources
This repository contains helpful tutorials on things that will help people get caught up to speed in Edaurdo Rozo's research group.

## Contents
Each directory contains the following:
* ```C_integrands``` - how to make your Python integrals go faster by writing the integrands in C
* ```Debugging``` - how to interpret error messages from C or Python
* ```Fitting Models``` - solutions to many of the problems in David Hogg's "Fitting a Model to Data" paper
* ```GP_examples``` - some examples of how Gaussian Processes work
* ```Making Figures``` - instructions on how to make presentable plots for group meetings and papers
* ```Numerical Exercises``` - some problems in computational cosmology that are good to have done yourself at least once
* ```Using Class``` - examples of how to use the Boltzmann code CLASS. Boltzmann codes are necessary to do cosmology that involves large scale structure

## To be added
You can contribute as well. Here are some topics that could be expanded on.
* ```Splines and interpolation``` - a breakdown of how to interpolate data. Sometimes a linear interpolator is good, other times a spline is good. Explain what these technical terms are and show the difference between these choices.
* ```Basic parallelism``` - some programs are super slow but can be run on many cores or CPUs at the same time. Show examples of using Pthon's ```multiprocess``` package, using OpenMP in C, and also OpenMPI in C
* ```Cosmology homeworks``` - a collection of exercises that everyone in the group should do at least once. E.g. correlation function definition, differences between halo-halo halo-matter and matter-matter correlation functions, transforming between power spectrum and correlation functions, basic gravitational lensing, pair counting, understanding what a mass function is, opening a data catalog, etc.
* ```MCMC tips and tricks``` - We end up running MCMC codes like emcee all the time. This details some good things to know such as: how to find the max likelihood point before setting up walkers, setting up walkers to match the likelihood, how long should burn-in be, when is your chain converged/finding the autocorrelation time, down sampling a chain to remove correlations, re-initializing a chain to add on to the end.
* ```Emcee alternatives``` - our go to sampler is emcee but there are other options. This shows how to use Multinest and HMC samplers. Stretch goals would include showing how to use variational inference, or Gaussian Process sampling.
* ```Terminology cheat sheet``` - What's the difference between DES and DESC? What about SLAC and slack? What *is* large scale structure, weak vs strong lensing, correlation functions, etc.?