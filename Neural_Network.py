import numpy as np


class Neural_Network:
    #
    def __init__(self, size):
        self.layer_size = size
        self.layer_count = len(self.layer_size) - 1

        self.original_inputs = []
        self.z_inputs_list = []
        # self.output_list = []
        self.activity = []
        self.weights = []

        self.final_output = []
        self.final_output_derivative = []

        self.train_data = []

        '''Takes layer size (2, 3, 1) and creates weight matrices by grouping them in twos. Since weights go from 2 to 3
        then 3 to 1.
        Randomizes them with normal distribution '''

        for (i, j) in zip(self.layer_size[:-1], self.layer_size[1:]):
            self.weights.append(np.random.normal(scale=.1, size=(i,j)))



    def forward(self, inputs):

        # Takes inputs and creates numpy array. so
        self.z_inputs_list = []
        self.activity = []
        self.original_inputs = np.array(inputs)

        for i in range(self.layer_count):
            print("initial input:", self.original_inputs)
            # if first layer:
            if i == 0:
                # dot product of weights x initial inputs added to z_input list
                self.z_inputs_list.append(self.original_inputs.dot(self.weights[i]))
                # pass inputs to sigmoid and add to activity list
                self.activity.append(self.sigmoid(self.z_inputs_list[i]))
                print("Original inputs", self.original_inputs)
                print("activity Layer 1 = ", self.activity[0])
            else:
                # dot product previous outputs with next layer weights
                self.z_inputs_list.append(self.activity[i-1].dot(self.weights[i]))
                self.activity.append(self.sigmoid(self.z_inputs_list[i]))
                print("output Activity:", self.activity[i])


    def train_network(self, train_data):
        # convert training data into proper sized array
        self.train_data = train_data
        self.train_data = np.array(train_data)
        self.train_data.reshape(3,1)

        # reshape final output activity into 3x1 matrix to subtract elementwise from y for error
        yhat = self.activity[-1]
        yhat = np.array(yhat)
        yhat = yhat.reshape(3,1)
        error = self.cost(train_data, yhat)

        '''calculate f'(z) for final layer. This is the derivative of our sigmoid
        function to calculate Backpropgation Delta'''

        for i in range(len(self.z_inputs_list[-1])):
            self.final_output_derivative.append(self.sigmoid(self.z_inputs_list[1][i], derivative=True))
        print("derivative", self.final_output_derivative)

        final_delta = (error)*self.final_output_derivative
        part_deriviative = np.dot(self.activity[0], final_delta)



    def cost(self, y, yhat):
        error = np.subtract(y, yhat)
        print(error)
        return error

    def sigmoid(self, z, derivative=False):
        if not derivative:
            return 1 / (1 - np.exp(-z))
        else:
            return self.sigmoid(z) * (1 - self.sigmoid(z))


shape = [2, 3, 1]
x = [[3, 5], [5, 1], [7,9]]
y = [75, 90, 82]
print(y)
network = Neural_Network(shape)
network.forward(x)
network.train_network(y)

