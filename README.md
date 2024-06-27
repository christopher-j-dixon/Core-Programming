# Introduction to Core Programming

## Course Overview

This repository contains my coursework solutions for the Core Programming course. The course covers numerical methods and their implementation in Python, including root-finding, solving linear systems, polynomial interpolation, numerical calculus, and solving ODEs.

## Directory Structure

### Calculation (CAL)
1. **CAL1.py**: 
   - Implements Bernoulli numbers and their applications in mathematical functions.
   - Includes the `bernoulli` function to compute Bernoulli numbers.
   - Includes the `pn` function to compute values using Bernoulli numbers.

2. **CAL2.py**: 
   - Implements numerical differentiation using forward, backward, and central difference formulas.
   - Includes visualisation of the numerical differentiation results.

3. **CAL3.py**: 
   - Implements numerical integration using trapezoidal, Simpson's, and midpoint rules.
   - Includes visualisation of the numerical integration results.

### Linear Systems (LIN)
1. **LIN1.py**: 
   - Implements Gaussian elimination for solving linear systems.
   - Includes operation count and pivoting strategies.

2. **LIN2.py**: 
   - Implements Jacobi and Gauss-Seidel methods for solving linear systems iteratively.
   - Includes matrix norms and convergence analysis.

3. **LIN3.py**: 
   - Implements matrix factorisation techniques.
   - Includes special matrices like diagonally dominant and symmetric positive definite matrices.

### Analysis of Functions (ACF)
1. **ACF1.py**: 
   - Implements root-finding methods: Bisection method, fixed-point iteration, and Newton’s method.
   - Includes convergence analysis of these methods.

2. **ACF2.py**: 
   - Implements polynomial interpolation using Lagrange polynomials.
   - Includes error analysis of the interpolation.

3. **ACF3.py**: 
   - Implements numerical solutions for ordinary differential equations (ODEs) using Euler’s method and higher-order Runge-Kutta methods.
   - Includes local truncation error analysis and visualisation.

## Learning Outcomes

Upon successful completion of this course, students will be able to:

- Solve nonlinear equations using root-finding methods, and analyse their convergence.
- Solve linear systems of equations using direct methods, and analyse their computational complexity.
- Solve linear systems of equations using iterative techniques, and analyse their convergence.
- Approximate functions by polynomial interpolants, and analyse their accuracy.
- Approximate derivatives and definite integrals using numerical differentiation and integration, and analyse their convergence.
- Approximate ODEs using numerical methods, and analyse their convergence.
- Implement reusable codes in Python.
