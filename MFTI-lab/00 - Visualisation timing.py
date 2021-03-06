import time
from matplotlib import pyplot as plt

def GCD(a, b):
    '''
    Наибольший общий делитель a, b
    '''
    while b:
        a, b = b, a%b
    return a

def GCD1(a, b):
    '''
    Наибольший общий делитель a, b
    '''
    while a > 0 and b > 0:
        a, b = b, a%b
    return a if a else b



# минимальное из вызовов
def timed(f, args, n_iter=10):
    acc = float("inf")
    print(*args)
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        acc = min(acc, time.perf_counter() - t0)
    return acc

# общее за все вызовы время
def timed_CountedAllCycles(f, args, n_iter=10):
    acc = 0
    t0 = time.perf_counter()
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
    acc = time.perf_counter()
    return acc



def compare(fs, args):
    xs = list(range(len(args)))
    for f in fs:
        plt.plot(xs, [timed(f, chunk) for chunk in args],
                 label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()

def compareAll(fs, args):
    xs = list(range(len(args)))
    for f in fs:
        plt.plot(xs, [timed_CountedAllCycles(f, chunk) for chunk in args],
                 label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()



compare([GCD, GCD1], [(x, 17) for x in range(100, 10000, 100)])
compareAll([GCD, GCD1], [(x, 17) for x in range(100, 10000, 100)])