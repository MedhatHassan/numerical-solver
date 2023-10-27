import sympy as sp
import argparse

def parse_args(): 
    print("""
            ███╗   ██╗ ██╗   ██╗ ███╗   ███╗ ███████╗ ██████╗  ██╗  ██████╗  █████╗  ██╗          ███████╗  ██████╗  ██╗      ██╗   ██╗ ███████╗ ██████╗  
            ████╗  ██║ ██║   ██║ ████╗ ████║ ██╔════╝ ██╔══██╗ ██║ ██╔════╝ ██╔══██╗ ██║          ██╔════╝ ██╔═══██╗ ██║      ██║   ██║ ██╔════╝ ██╔══██╗ 
            ██╔██╗ ██║ ██║   ██║ ██╔████╔██║ █████╗   ██████╔╝ ██║ ██║      ███████║ ██║          ███████╗ ██║   ██║ ██║      ██║   ██║ █████╗   ██████╔╝ 
            ██║╚██╗██║ ██║   ██║ ██║╚██╔╝██║ ██╔══╝   ██╔══██╗ ██║ ██║      ██╔══██║ ██║          ╚════██║ ██║   ██║ ██║      ╚██╗ ██╔╝ ██╔══╝   ██╔══██╗ 
            ██║ ╚████║ ╚██████╔╝ ██║ ╚═╝ ██║ ███████╗ ██║  ██║ ██║ ╚██████╗ ██║  ██║ ███████╗     ███████║ ╚██████╔╝ ███████╗  ╚████╔╝  ███████╗ ██║  ██║ 
            ╚═╝  ╚═══╝  ╚═════╝  ╚═╝     ╚═╝ ╚══════╝ ╚═╝  ╚═╝ ╚═╝  ╚═════╝ ╚═╝  ╚═╝ ╚══════╝     ╚══════╝  ╚═════╝  ╚══════╝   ╚═══╝   ╚══════╝ ╚═╝  ╚═╝ 
                                                                                                                    By Medhat hassan ~~ @MedhatHassan
    """)
    parser = argparse.ArgumentParser(description="Numerical Solver")

    # Required argument: Function
    parser.add_argument("-f", "--function", type=str, required=True, help="Math function to solve")

    # Optional argument: Error tolerance
    parser.add_argument("-e", "--error", type=float, default=1e-5, help="Error tolerance (default: 1e-5)")

    # Optional argument: Number of iterations
    parser.add_argument("-i", "--iterations", type=int, default=50, help="Maximum number of iterations (default: 50)")

    # Optional argument: Verbose mode
    parser.add_argument("-v", "--verbose", action="store_true" , default=False, help="To show all iterations of numerical methods")

    # Optional arguments for Numerical methods
    parser.add_argument("-b", "--bisection", action="store_true", help="Use the Bisection Method")
    parser.add_argument("-fp", "--false_position", action="store_true", help="Use the False Position Method")
    parser.add_argument("-n", "--newton_raphson", action="store_true", help="Use the newton raphson Method")
    parser.add_argument("-s", "--secant", action="store_true", help="Use the secant Method")
    parser.add_argument("-all", "--all_methods", action="store_true", help="Use all Method and compare")
    parser.add_argument("-xl", "--lower_value", type=float, help="Lower value for bisection or false position")
    parser.add_argument("-xu", "--upper_value", type=float, help="Upper value for bisection or false position")
    parser.add_argument("-x0", "--intial_value0", type=float, help="Intial value for newton raphson or secant")
    parser.add_argument("-x1", "--intial_value1", type=float, help="Intial value for secant")


    args = parser.parse_args()
    return args

def exactSolutions(equation):
    try:
        # Parse the equation
        equation = sp.Eq(equation, 0)
        x = sp.symbols('x')
        symbol = x
        # Solve for the symbol
        solutions = sp.solve(equation, symbol)

        return solutions
    except:
        print("[-]No exact solutions found for the given equation.")


def f(x, equation):
    return equation.subs('x', x)

def bisectionMethod(equation, xl, xu, es, imax, verbose):
    iter = 0
    xm = (xl + xu) / 2
    ea = es + 1  # Initialize error to 0 in the first iteration

    if verbose:
        print(f'iterations \t xl \t  xm \t    xu \t      f(xl) \tf(xm) \t f(xu) \t    e_a')
        print('------------------------------------------------------------------------------------')

    while (ea != 0) and (iter < imax - 1):
        if iter == 0:
            xmold = xm
            xm = (xl + xu) / 2
            ea = abs(xm - xmold)
            fxl = f(xl, equation)
            fxm = f(xm, equation)
            fxu = f(xu, equation)
            if verbose:
                print(f'iteration {iter} {xl:9.4f} {xm:9.4f} {xu:9.4f} {fxl:9.4f} {fxm:9.4f} {fxu:9.4f} {ea:9.4f}\n')

        iter += 1

        test = fxl * fxm  # Modify this line

        if test < 0: 
            xu = xm
            fxu = fxm
        elif test > 0:
            xl = xm
            fxl = fxm
        else:
            ea = 0

        xmold = xm
        xm = (xl + xu)/2
        fxm = f(xm, equation)
        ea = abs(xm - xmold)
        
        if verbose:
            print(f'iteration {iter} {xl:9.4f} {xm:9.4f} {xu:9.4f} {fxl:9.4f} {fxm:9.4f} {fxu:9.4f} {ea:9.4f}\n')

    return xm ,ea

def falsePositionMethod(equation, xl, xu, es, imax, verbose):
    iter = 0
    ea = es + 1  # Initialize ea to a value greater than es

    if f(xl, equation) * f(xu, equation) >= 0:
        print("The function values at xl and xu should have opposite signs for a root to exist in the interval.")
        return None
    else:
        if verbose:
            print(f'iterations \t xl \t  xr \t    xu \t      f(xl) \tf(xr) \t f(xu) \t    e_a')
            print('------------------------------------------------------------------------------------')
        
        while (ea > es) and (iter < imax):
            xrold = xl
            fl = f(xl, equation)
            fu = f(xu, equation)
            xr = xu - fu * (xl - xu) / (fl - fu)
            fr = f(xr, equation)
            iter += 1

            if xr != 0:
                ea = abs((xr - xrold) / xr) * 100

            test = fl * fr

            if test < 0:
                xu = xr
            elif test > 0:
                xl = xr
            else:
                ea = 0

            if verbose:
                print(f'iteration {iter} {xl:9.4f} {xr:9.4f} {xu:9.4f} {fl:9.4f} {fr:9.4f} {fu:9.4f} {ea:9.4f}\n')

        return xr , ea

def newtonRaphsonMethod(equation, x0, tol, max_iter, verbose):
    x = sp.symbols('x')
    f = sp.sympify(equation)
    df = sp.diff(f, x)

    x_val = x0
    ea = tol + 1  # Initialize error to a value greater than tol
    iter = 0

    if verbose:
        print(f'iterations \tx \tf(x) \te_a')
        print('---------------------------------------')

    while (ea > tol) and (iter < max_iter):
        fx = f.subs(x, x_val)
        if abs(fx) < tol:
            if verbose:
                print(f'iteration {iter} \t{x_val:.4f} \t{fx:.4f} \t{ea:.4f}')
            return x_val , ea # Converged

        dfx = df.subs(x, x_val)
        if dfx == 0:
            if verbose:
                print("[-] Derivative is zero may lead to division by zero")
            return None

        xrold = x_val
        x_val = x_val - fx / dfx
        ea = abs((x_val - xrold) / x_val) * 100

        if verbose:
            print(f'iteration {iter} \t{x_val:.4f} \t{fx:.4f} \t{ea:.4f}')
        
        iter += 1

    if verbose:
        print("[-] Did not converge within the maximum number of iterations for this X0")

    return None

def secantMethod(equation, x0, x1, tol, max_iter, verbose):
    x = sp.symbols('x')
    f = sp.sympify(equation)

    x0_val, x1_val = x0, x1
    iter = 0

    if verbose:
        print(f'iterations \tx1 \tx2 \tf(x1)\tf(x2)\te_a')
        print('---------------------------------------------------------')

    for i in range(max_iter):
        f0 = f.subs(x, x0_val)
        f1 = f.subs(x, x1_val)

        if abs(f1 - f0) < tol:
            if verbose:
                print(f'iteration {iter} \t{x1_val:.4f} \t{x1_val:.4f} \t{f1:.4f} \t{f1:.4f} \t{0.0000}')
            return x1_val , tol  # Converged

        dfdx = (f1 - f0) / (x1_val - x0_val)

        if dfdx == 0:
            if verbose:
                print("[-] Derivative is zero may lead to division by zero")
            return None 

        x2_val = x1_val - f1 / dfdx
        ea = abs((x2_val - x1_val) / x2_val) * 100

        if verbose:
            print(f'iteration {iter} \t{x1_val:.4f} \t{x2_val:.4f} \t{f1:.4f} \t{f.subs(x, x2_val):.4f} \t{ea:.4f}')

        x0_val, x1_val = x1_val, x2_val
        iter += 1

    if verbose:
        print("[-] Did not converge within the maximum number of iterations for this interval")

    return None

def compareRoots(bisection_result, false_position_result, newton_raphson_result, secant_result, exact_solutions):
    methods = ["Bisection", "False Position", "Newton-Raphson", "Secant", "Exact Solutions"]
    roots = [bisection_result, false_position_result, newton_raphson_result, secant_result, exact_solutions]

    # Find the method with the closest root to the exact solution
    best_method_index = min(range(len(roots)), key=lambda i: abs(roots[i] - exact_solutions))

    best_method = methods[best_method_index]
    best_root = roots[best_method_index]

    return best_method, best_root

import sympy as sp

def compareRootsError(bisection_error, false_position_error, newton_raphson_error, secant_error):
    methods = ["Bisection", "False Position", "Newton-Raphson", "Secant"]
    errors = [bisection_error, false_position_error, newton_raphson_error, secant_error]

    # Find the method with the lowest error
    best_method_index = errors.index(min(errors))
    best_method = methods[best_method_index]
    best_error = errors[best_method_index]

    return best_method, best_error


if __name__ == "__main__":
    args = parse_args()
    function = args.function
    error = args.error
    verbose = args.verbose
    iterations = args.iterations
    bisection = args.bisection
    falsePostion = args.false_position
    newton = args.newton_raphson
    secant = args.secant
    x0 = args.intial_value0
    x1 = args.intial_value1
    xu = args.upper_value
    xl = args.lower_value
    all = args.all_methods
    x = sp.symbols('x')
    equation = sp.sympify(function)
    if function and not all:
        solutions = exactSolutions(equation)
        iter = 0
        if solutions:
            print("[+]Exact solutions: ",end="")
            for sol in solutions:
                if iter == 0:
                    print(sol,end="")
                else:
                    print(' OR',sol,end="")
                iter +=1
            print('\n')
    if bisection:
        if xu and xl:
            bisectionMethod_result = bisectionMethod(equation,xl, xu, error, iterations,verbose)
            print("[+]Bisection Method - Approximate root:", bisectionMethod_result)
        else:
            print("[-]You must specify an interval for bisection method")
    if falsePostion:
        if xu and xl:
            falsePositionMethod_result = falsePositionMethod(equation,xl, xu, error, iterations,verbose)
            print("[+]False Position Method - Approximate root:", falsePositionMethod_result)
        else:
            print("[-]You must specify an interval [xl & xu] for False Position method")
    if newton:
        if x0:
            newtonRaphsonMethod_result = newtonRaphsonMethod(equation,x0,error,iterations,verbose)
            print("[+]Newton Raphson Method - Approximate root:", newtonRaphsonMethod_result)
        else:
            print("[-]You must specify an intial value [x0] for Newton Raphson Method")
    if secant:
        if x0 and x1:
            secantMethod_result = secantMethod(equation,x0,x1,error,iterations,verbose)
            print("[+]secant Method - Approximate root:", secantMethod_result)
        else:
            print("[-]You must specify an intial value [x0] for Newton Raphson Method")
    if all:
        exact_solutions = exactSolutions(equation)
        if xu and xl and x0 and x1 and exact_solutions:
            # the equation has exact value 
            bisectionMethod_result,error = bisectionMethod(equation,xl, xu, error, iterations,verbose=False)
            falsePositionMethod_result,error = falsePositionMethod(equation,xl, xu, error, iterations,verbose=False)
            newtonRaphsonMethod_result,error = newtonRaphsonMethod(equation,x0,error,iterations,verbose=False)
            secantMethod_result,error = secantMethod(equation,x0,x1,error,iterations,verbose=False)
            best_method, best_root = compareRoots(bisectionMethod_result, falsePositionMethod_result, newtonRaphsonMethod_result, secantMethod_result, exact_solutions)
            print("[+]Bisection Method - Approximate root:", bisectionMethod_result)
            print("[+]False Position Method - Approximate root:", falsePositionMethod_result)
            print("[+]Newton Raphson Method - Approximate root:", newtonRaphsonMethod_result)
            print("[+]secant Method - Approximate root:", secantMethod_result)
            print(f"The best method is {best_method} with a root value of {best_root:.10f}")
        else:
            res,bisection_error = bisectionMethod(equation,xl, xu, error, iterations,verbose=False)
            res,falsePosition_error = falsePositionMethod(equation,xl, xu, error, iterations,verbose=False)
            res,newtonRaphson_error = newtonRaphsonMethod(equation,x0,error,iterations,verbose=False)
            res,secant_error = secantMethod(equation,x0,x1,error,iterations,verbose=False)
            print("[+]Bisection Method - Approximate root:", res)
            print("[+]False Position Method - Approximate root:", res)
            print("[+]Newton Raphson Method - Approximate root:", res)
            print("[+]secant Method - Approximate root:", res)
            best_method, best_error = compareRootsError(bisection_error, falsePosition_error, newtonRaphson_error, secant_error)
            print(f"The best method is {best_method} with an error of {best_error:.10f}")
