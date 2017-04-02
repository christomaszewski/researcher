from abc import ABCMeta, abstractmethod

from multiprocess import Pool

class Executor(metaclass=ABCMeta):

	@abstractmethod
	def setup(self, *args):
		raise NotImplementedError()

	@abstractmethod
	def start(self):
		raise NotImplementedError()


class MultiProcessExecutor(Executor):

	def __init__(self, experiment, numProcesses):
		self._expr = experiment
		self._numProcesses = numProcesses

	def setup(self, *args):
		self._inputArgs  = args
		self._workerPool = Pool(processes = self._numProcesses)

	def start(self):
		chunks = int(len(*self._inputArgs)/self._numProcesses)
		print(chunks)
		self._results = self._workerPool.map_async(self._expr.run, *self._inputArgs, chunksize=chunks)

		return self._results