from abc import ABCMeta, abstractmethod

class Experiment(metaclass=ABCMeta):

	@abstractmethod
	def setup(self, *args):
		""" Called once on the main experiment instance to initialize things

		"""
		raise NotImplementedError()

	@abstractmethod
	def _execute(self):
		""" Executes defined task in experiment

		"""
		raise NotImplementedError()

	@abstractmethod
	def _analyze(self):
		""" Processes results of execution
		
		"""
		raise NotImplementedError()

	@abstractmethod
	def run(self, *args):
		""" Externally visible method that can be called by processes in pool

		"""
		raise NotImplementedError()