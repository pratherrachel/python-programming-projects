# Neural-Network Approximation of the Sine Function

Train dense neural networks to approximate `sin(x)` on the interval [0, π], comparing a baseline model against one with 5% dropout.

## Method

- Generate synthetic x values on [0, π] and compute exact sine targets.
- Hold out 200 independent points from training for test evaluation.
- Train three 16-unit ReLU hidden layers with Adam optimization and mean squared error loss.
- Report the held-out mean squared error and save a plot comparing predictions with the analytical function.

## Run

From the repository root, after `pip install -r requirements.txt`:

```bash
python 03-neural-network-function-approximation/sine_approximation.py --epochs 100
```

Plot output is written to `outputs/sine_approximation.png`.

**Limitations:** this tests interpolation within the training domain, not extrapolation; results can vary across runs and platforms.
