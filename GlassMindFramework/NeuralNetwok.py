from GlassMindFramework.Neuron import Neuron
class NeuralNetwork:
    """
    layers - (2, 4, 6, 8, 1) e.t.c.
    """
    def __init__(self, layers):
        self.neurons = [[Neuron() for i in range(layers)] for layer in layers]
        last_layer = layers[0]  # Firstly, it will be
        self.weights = []
        for layer in layers:


        # self.weights = [[None for i in range(layer)] for layer in layers[1:]]

