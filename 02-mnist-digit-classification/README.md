# MNIST Digit Classification

Compare fully connected neural networks trained on the MNIST handwritten-digit dataset using TensorFlow/Keras: a baseline with no dropout and an otherwise similar model with 25% dropout after each hidden layer.

## Method

- Normalize pixels to the range [0, 1] and flatten each 28×28 image to 784 features.
- Use hidden layers of 200, 100, 60 and 30 ReLU units, with 10-class softmax output.
- Use 10% of the *training* data for validation; reserve the official test data for final evaluation.
- Print held-out test accuracy and loss and save training/validation plots.

## Run

From the repository root, after `pip install -r requirements.txt`:

```bash
python 02-mnist-digit-classification/mnist_compare.py --epochs 5
```

Use `--epochs 32` to reproduce the original coursework training length. The dataset is downloaded by Keras when it is not already cached. Plot files are written to `outputs/`.

**Limitations:** no repeated-seed uncertainty analysis; uses dense rather than convolutional networks; benchmark results should be reported only after actually running the code.
