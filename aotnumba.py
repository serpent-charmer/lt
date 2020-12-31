from numba.pycc import CC
cc = CC('aot_compiled')
# Uncomment the following line to print out the compilation steps
#cc.verbose = True

@cc.export('cross_pr_aout', 'void(f8[:], f8[:])')
def cross_pr(a, b):
   
    for i in range(len(a)):
        a[i] = a[i] * b[i]

if __name__ == "__main__":
    cc.compile()