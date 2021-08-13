import pdb
def factoryal(n):
    # pdb.set_trace()
    try:
        if (isinstance(n, int))==True:
            fact = 1
            sum = 1
            while True:
                sum *= fact
                fact += 1
                if fact > n:
                    break
            return  sum
        else:
            print("the number must be decimal")
    except Exception  as e:
        print("the error is",e.args)
    # if isinstance(n,int):
    if __name__=='__main__':
        print(factoryal(3))



