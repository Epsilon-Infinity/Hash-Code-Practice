import cvxpy
from cvxpy.atoms.affine.binary_operators import matmul
from cvxpy.atoms.affine.sum import sum
import numpy as np
import os
import util


def max_slices(m,l):
    x = cvxpy.Variable(len(l),boolean=True)
    const1 = sum(matmul(x,l))  <=m
    obj = cvxpy.Maximize(sum(matmul(x, l)))
    prob = cvxpy.Problem(obj,[const1])
    prob.solve(solver=cvxpy.CBC)
    print("optimization result :",prob.status)
    s = [int(round(i)) for i in x.value]
    return [i for i in range(len(s)) if s[i]!=0]



if __name__=="__main__":
    root_dir = input().strip()
    util.solve_files(root_dir, max_slices)
