import cvxpy
from cvxpy.atoms.affine.binary_operators import matmul
from cvxpy.atoms.affine.sum import sum
import numpy as np
import os


def max_slices(m,l):
    x = cvxpy.Variable(len(l),boolean=True)
    const1 = sum(matmul(x,l))  <=m
    obj = cvxpy.Maximize(sum(matmul(x, l)))
    prob = cvxpy.Problem(obj,[const1])
    prob.solve(solver=cvxpy.CBC)
    print("optimization result :",prob.status)
    return x.value

def read_file(file_path):
    file = open(file_path)
    lines = file.readlines()
    m, n = list(map(int, lines[0].strip().split()))
    l =  list(map(int, lines[1].strip().split()))
    return m, n, l

if __name__=="__main__":
    root_dir = input().strip()
    files = os.listdir(root_dir)
    for file in files:
        print("Solving file :",file)
        m, n, l = read_file(os.path.join(root_dir, file))
        #print(m,n)
        s = max_slices(m,l)
        with open(os.path.join(root_dir,"..","result", file+".sol"),"w") as solution:
            s = [int(round(i)) for i in s]
            ind = [i for i in range(len(s)) if s[i]!=0]
            solution.write(str(len(ind))+"\n")

            solution.write(" ".join([str(i) for i in ind]))
