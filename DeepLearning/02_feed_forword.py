class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
    
    def feedForward(self, inputs):
        total = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        return total