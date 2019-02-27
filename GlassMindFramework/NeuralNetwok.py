from GlassMindFramework.Neuron import Neuron


class NeuralNetwork:
    """
    layers - (2, 4, 6, 8, 1) e.t.c.
    """
    def __init__(self, layers):
        # self.activate_fnc = activate_fnc
        # self.derivative = derivative

        self.neurons = [[Neuron() for i in range(layer)] for layer in layers]

        last_layer = layers[0]  # Firstly, it will be
        self.weights = []
        for layer in layers[1:]:
            self.weights.append([])
            for i in range(layer):
                self.weights[-1].append([])
                for ii in range(last_layer):
                    self.weights[-1][-1].append(0)
            last_layer = layer

        # self.weights = [[None for i in range(layer)] for layer in layers[1:]]

    def write(self):
        pass

    def test(self):
        pass

    def pack_propogation(self):
        pass
