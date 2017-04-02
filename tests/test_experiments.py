from context import researcher

class TestExperiment(researcher.experiment.Experiment):

	def __init__(self):
		# Should only be called once
		print("constructing experiment")

	def setup(self, *args):
		self._input = args[0]
		print("setting up experiment with input " + str(self._input))

	def _execute(self):
		print("executing experiment with input " + str(self._input))

	def _analyze(self):
		print("analyzing experiment results")
		self._result = float(self._input)**2 

	def run(self, *args):
		print("received input of length " + str(len(args)))
		print("running experiment")
		self._input = args[0]
		self._execute()
		self._analyze()

		# Package and return results
		return (self._input, self._result)
