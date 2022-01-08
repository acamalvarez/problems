from scipy.optimize import linprog


def solve_lin_prog(obj, lhs_ineq, rhs_ineq):
    return linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="simplex")
