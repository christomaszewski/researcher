from abc import ABCMeta, abstractmethod

from multiprocess import Pool

class Executor(metaclass=ABCMeta):

	@abstractmethod
	def setup(self, *args):
		raise NotImplementedError()

	@abstractmethod
	def start(self):
		raise NotImplementedError()

class LoopedExecutor(Executor):

	def __init__(self, experiment):
		self._expr = experiment

	def setup(self, *args):
		self._inputArgs = args

	def start(self):
		self._results = []
		for arg in self._inputArgs:
			self._results.append(self._expr.run(arg))

		return self._results

class MultiProcessExecutor(Executor):

	def __init__(self, experiment, numProcesses=None):
		self._expr = experiment

		if (numProcesses is None):
			self._numProcesses = multiprocess.cpu_count() - 1
		else:
			self._numProcesses = numProcesses

	def setup(self, *args):
		self._inputArgs  = args
		self._workerPool = Pool(processes = self._numProcesses)

	def start(self):
		chunks = max(int(len(*self._inputArgs)/self._numProcesses), 1)
		print(chunks)
		self._results = self._workerPool.map_async(self._expr.run, *self._inputArgs, chunksize=chunks)

		return self._results