# Numerical Solver

![Numerical Solver Logo](https://www.example.com/path/to/your/logo.png)

## Table of Contents
- [Introduction](#introduction)
- [Description](#description)
- [Supported Methods](#supported-methods)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [all function](#all-function)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

Welcome to the Numerical Solver repository! This Python script provides a versatile tool for solving mathematical equations using various numerical methods. Whether you're a student, researcher, or developer, this tool can help you find approximate solutions to equations efficiently.

## Description
Numerical Solver is a Python script designed to help you find numerical solutions to mathematical equations. It supports multiple numerical methods, including the Bisection Method, False Position Method, Newton-Raphson Method, and the Secant Method. You can use it to approximate roots of equations with different levels of accuracy and precision.

## installation
Clone this repository to your local machine:
```git clone https://github.com/MedhatHassan/numericalsolver.git```
Install the required dependencies using pip:
```pip install sympy```

## Supported Methods
Numerical Solver supports the following numerical methods:

- Bisection Method: Approximates roots using the bisection method within a specified interval.
- False Position Method: Uses the false position method to find root estimates.
- Newton-Raphson Method: Applies the Newton-Raphson method for root approximation.
- Secant Method: Utilizes the secant method to find root approximations.
You can choose any of these methods according to your needs and preferences Or choose all to compare them all to get the right answer.

## Prerequisites

Before using Numerical Solver, make sure you have the following prerequisites in place:
- Python (version 3.6 or higher)
- SymPy library (for symbolic mathematics)

## Usage
Run `python Numerical Solver.py --help` to get help
```

            ███╗   ██╗ ██╗   ██╗ ███╗   ███╗ ███████╗ ██████╗  ██╗  ██████╗  █████╗  ██╗          ███████╗  ██████╗  ██╗      ██╗   ██╗ ███████╗ ██████╗  
            ████╗  ██║ ██║   ██║ ████╗ ████║ ██╔════╝ ██╔══██╗ ██║ ██╔════╝ ██╔══██╗ ██║          ██╔════╝ ██╔═══██╗ ██║      ██║   ██║ ██╔════╝ ██╔══██╗ 
            ██╔██╗ ██║ ██║   ██║ ██╔████╔██║ █████╗   ██████╔╝ ██║ ██║      ███████║ ██║          ███████╗ ██║   ██║ ██║      ██║   ██║ █████╗   ██████╔╝ 
            ██║╚██╗██║ ██║   ██║ ██║╚██╔╝██║ ██╔══╝   ██╔══██╗ ██║ ██║      ██╔══██║ ██║          ╚════██║ ██║   ██║ ██║      ╚██╗ ██╔╝ ██╔══╝   ██╔══██╗ 
            ██║ ╚████║ ╚██████╔╝ ██║ ╚═╝ ██║ ███████╗ ██║  ██║ ██║ ╚██████╗ ██║  ██║ ███████╗     ███████║ ╚██████╔╝ ███████╗  ╚████╔╝  ███████╗ ██║  ██║ 
            ╚═╝  ╚═══╝  ╚═════╝  ╚═╝     ╚═╝ ╚══════╝ ╚═╝  ╚═╝ ╚═╝  ╚═════╝ ╚═╝  ╚═╝ ╚══════╝     ╚══════╝  ╚═════╝  ╚══════╝   ╚═══╝   ╚══════╝ ╚═╝  ╚═╝ 
                                                                                                                    By Medhat hassan ~~ @MedhatHassan     
    
usage: Numerical Solver.py [-h] -f FUNCTION [-e ERROR] [-i ITERATIONS] [-v] [-b] [-fp] [-n] [-s] [-all] [-xl LOWER_VALUE] [-xu UPPER_VALUE] [-x0 INTIAL_VALUE0] [-x1 INTIAL_VALUE1]

Numerical Solver

options:
  -h, --help            show this help message and exit
  -f FUNCTION, --function FUNCTION
                        Math function to solve
  -e ERROR, --error ERROR
                        Error tolerance (default: 1e-5)
  -i ITERATIONS, --iterations ITERATIONS
                        Maximum number of iterations (default: 50)
  -v, --verbose         To show all iterations of numerical methods
  -b, --bisection       Use the Bisection Method
  -fp, --false_position
                        Use the False Position Method
  -n, --newton_raphson  Use the newton raphson Method
  -s, --secant          Use the secant Method
  -all, --all_methods   Use all Method and compare
  -xl LOWER_VALUE, --lower_value LOWER_VALUE
                        Lower value for bisection or false position
  -xu UPPER_VALUE, --upper_value UPPER_VALUE
                        Upper value for bisection or false position
  -x0 INTIAL_VALUE0, --intial_value0 INTIAL_VALUE0
                        Intial value for newton raphson or secant
  -x1 INTIAL_VALUE1, --intial_value1 INTIAL_VALUE1
                        Intial value for secant
```
## all function
The all function is designed to provide a comparison of different numerical methods and find the best method for approximating the root of a mathematical equation.
It allows users to apply multiple numerical methods and select the one that produces the closest result to the exact solution.
This function is particularly useful when you want to assess the accuracy of different methods for a given equation and determine which method performs best.
The all function uses the following numerical methods: Bisection, False Position, Newton-Raphson, and Secant.
It also considers the exact solutions, if available, as a reference point for comparison.
### Usage
To use the all function effectively, follow these steps:
- Provide the mathematical equation you want to solve using the -f or --function command-line argument.
- provide the lower and upper interval limits (-xl and -xu).
- provide two initial guesses (-x0 and -x1).

Run the script, and it will execute all the methods and provide the approximate roots and error values for each method.

The script will also identify the method that produces the result closest to the exact solution **(if available)** and report it as the best method.

The best method and its corresponding root value will be displayed as the final output.
### examble 
```
python Numerical Solver.py -f "x - cos(x)" -all -xl 0.9 -xu 0.4 -x0 0.9 -x1 1 -i 10
```

## Contributing
We welcome contributions to improve Numerical Solver! If you have any ideas for enhancements, bug fixes, or new features, please feel free to submit a pull request. Make sure to follow the contribution guidelines provided in the repository.

## License
Numerical Solver is licensed under the MIT License. You are free to use, modify, and distribute this script as long as you include the appropriate attribution.

## Acknowledgements
We would like to express our gratitude to the open-source community for their support and contributions that make projects like Numerical Solver possible.

Happy solving!
