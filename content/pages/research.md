Title: Research
Tags: research
Author: Jed Brown
Summary: Research topics

[TOC]

My research interests include scalable solvers for implicit multiphysics, high order PDE discretization in complex geometry, compatible discretizations for heterogeneous flows, and PDE-constrained optimization. My work emphasizes robust and high performance parallel software, often relating to [PETSc](http://mcs.anl.gov/petsc).

# Active Topics

## CFD for DC motors
Air and oil cooling, turbulence modeling, finite volume and spectral different methods, thermo-elasticity, implicit time integration with high-frequency periodic forcing. With Zoltan Horvath at Széchenyi István University (Győr, Hungary) and [Matt Knepley](http://people.cs.uchicago.edu/~knepley/).

## Interactive in-situ eigen-analysis using PETSc and SLEPc.
This will look somewhat like a "scalable EigTool" with support for 3D visualization and massively parallel solves. Unlike traditional approaches, our approach naturally supports "physics-based preconditioning". When used for solver design, these tools will help identify deficiencies in smoothers and interpolation operators, similar to "bootstrap" algebraic multigrid, but with more involvement of the user. 

## Low-communication multigrid, with applications to time-dependent adjoints, in-situ visualization, and resilience.
The "tau" formulation of FAS multigrid enables communication to be entirely removed from coarse grids. Additionally, coarse state can be checkpointed and then "decompressed" in any part of the subdomain. The basic idea was pointed out as early as 1977 by Achi Brandt, but has been largely overlooked despite becoming more relevant recently due to modern architecture changes. With Mark Adams and the PETSc team. 

## Pipelined Krylov methods
Pipelined Krylov methods such as PGMRES allow overlapping global communication (reductions) with computation and local communication, thus relieving a serious bottleneck on large-systems that do not have specialized hardware for reductions. With Pieter Ghysels. 

## Multilevel solvers for heterogeneous Stokes problems
Stokes problems with highly variable coefficients are ubiquitous in geodynamics applications. The rheology is typically pseudoplastic and temperature-dependent, leading to strong nonlinearities. Solution of these problems represents a critical bottleneck to high-resolution simulation of lithosphere dynamics. We are exploring robust coarsening and highly-parallel smoothers, with attention to fast updating due to evolving nonlinearities. With [Dave May](http://jupiter.ethz.ch/~dmay/), [Matt Knepley](http://people.cs.uchicago.edu/~knepley/), and Mark Adams.

## Time integration in PETSc

Implicit-explicit (IMEX) methods, structure preservation and interaction with multigrid methods, differential algebraic equations. With Emil Constantinescu and Peter Brune. 

# Tutorials

* Jed Brown, PETSc Tutorial at the National Renewable Energy Lab, Golden, CO, 2012-04-27.
* Jed Brown, The Portable Extensible Toolkit for Scientific Computing: Advanced PETSc Tutorial at TACC, Austin, TX, 2012-02-20. video
* Jed Brown, PETSc tutorial at ACTS, NERSC, Berkeley, CA, 2011-08-17.
* Jed Brown, PETSc Tutorial at the Arctic Region Supercomputing Center, Fairbanks, AK, 2010-08-03 to 05.
* Jed Brown, PETSc Tutorial at the Swiss National Supercomputing Center, Manno, Switzerland, 2010-05-10 and 11.
* Jed Brown, Scalable solvers for nonlinear equations: mini-course on Newton-Krylov methods, 3-week mini-course at the University of Alaska Fairbanks, 2009-01-22 to 2009-02-05.
