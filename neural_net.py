import numpy as np
import torch
import torchvision
import tqdm
import sys


# define our neural network
def neural_net (x, weight_1, weight_2):
    # matrix multiplication
    layer_1 = x @ weight_1
    # non-linear activation function
    layer_1 = torch.relu(layer_1)
    layer_2 = layer_1 @ weight_2
    return layer_2

# weight (parameter) matrix with gradients tracked
weight_1 = torch.randn(784,200,requires_grad=True)
weight_2 = torch.randn(200,10,requires_grad=True)

# download and load MNIST data
mnist_data = torchvision.datasets.MNIST("MNIST", train=True, download=False)
learning_rate   = 0.001
epochs          = 2000
batch_size      = 100
# setup a loss function
loss_function   = torch.nn.CrossEntropyLoss()

for i in tqdm.tqdm(range(epochs)):
    # get a set of random index value
    random_index        = np.random.randint(0, mnist_data.data.shape[0], size=batch_size)
    # subset the data and flatten the 28 x 28 image to 784 vectors
    x                   = mnist_data.data[random_index].float().flatten(start_dim=1)
    # normalize the vector to be between 0 and 1
    x                  /= x.max()
    # makes prediction using neural network
    predict_y_using_nn  = neural_net(x, weight_1, weight_2)
    # gets ground-truth image labels
    ground_truth        = mnist_data.targets[random_index]
    # computes the loss
    loss                = loss_function(predict_y_using_nn, ground_truth)
    # back propagation
    loss.backward()
    # don't compute gradient in this block
    with torch.no_grad():
        # gradient descent over parameter matrices
        weight_1 -= learning_rate * weight_1.grad
        weight_2 -= learning_rate * weight_2.grad

print ('finished training.')
sys.exit(0)
