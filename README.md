# Python Programming Projects

A growing collection of introductory Python programming and neural-network exercises. These projects document my development in Python alongside my [MATLAB computational mathematics work](https://github.com/pratherrachel/computational-mathematics-matlab).

## Projects

| Project | Topics | Script |
| --- | --- | --- |
| [Cafe Order Calculator](01-cafe-order-calculator/) | Python fundamentals, dictionaries, input validation, arithmetic | `cafe_order.py` |
| [MNIST Digit Classification](02-mnist-digit-classification/) | Image classification, data preprocessing, dense neural networks, dropout | `mnist_compare.py` |
| [Sine Function Approximation](03-neural-network-function-approximation/) | Numerical approximation, neural-network regression, MSE, visualization | `sine_approximation.py` |
| [SmartFit Fitness Eligibility](04-smartfit-fitness-eligibility/) | Nested conditionals, logical operators, membership choices | `smartfit.py` |

## Getting started

- Install a modern Python version compatible with the dependencies.
- For the cafe project, no third-party packages are required: `python 01-cafe-order-calculator/cafe_order.py`.
- For the neural-network projects, create and activate a Python virtual environment, then run `python -m pip install -r requirements.txt`.
- Run `python 02-mnist-digit-classification/mnist_compare.py --epochs 5` or `python 03-neural-network-function-approximation/sine_approximation.py`.
- The machine-learning scripts download MNIST through the official Keras loader (first run only) or generate synthetic data, respectively. They save output figures under an `outputs/` directory relative to the working directory.

## Notes on methodology

- The MNIST project compares fully connected models with and without 25% dropout. Training-set validation is separate from the final test-set evaluation.
- The sine project compares a regression network with and without 5% dropout. The held-out points test interpolation on the same domain, not extrapolation.
- Results vary with hardware, library versions, and stochastic training. No performance metrics are claimed here before actual runs.
- These scripts are educational examples, not production-ready systems.

## Next steps

Improve unit tests, compare results across different random seeds, add a confusion matrix for MNIST, and document plots from actual runs.

## SmartFit original coursework

The [SmartFit project](04-smartfit-fitness-eligibility/) contains my original introductory Python assignment, unchanged. The folder README documents the intended behavior and limitations without claiming additional validation, price calculations, or automated tests.
