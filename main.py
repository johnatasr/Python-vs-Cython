import run_python
import run_cython
import time

if __name__ == "__main__":
    number = 999999999999999999999999999999999999 * 999999999999999999999999999999

    start = time.time()
    print(start)
    num = run_cython.fibonacci(number)
    end = time.time()
    print(end)

    cy_time = end - start
    print("Cython time = {}".format(cy_time))

    start = time.time()
    print(start)
    run_python.fibonacci(number)
    end = time.time()
    print(end)

    py_time = end - start
    print("Python time = {}".format(py_time))

    print("Speedup = {}".format(py_time / cy_time))
