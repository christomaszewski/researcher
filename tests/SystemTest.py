from context import researcher

from test_experiments import TestExperiment
from researcher import executor
from multiprocessing import Pool

if __name__ == '__main__':

	expr = TestExperiment()
	expr.setup(-1)

	multiExec = executor.MultiProcessExecutor(expr, numProcesses=4)


	multiExec.setup(range(10))


	results = multiExec.start()


	print(results)
