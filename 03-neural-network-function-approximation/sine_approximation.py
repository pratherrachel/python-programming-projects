"""Approximate sin(x) on [0, pi] with dense neural networks.

The test points are held out from the training points but occupy the same
interval; this demonstrates interpolation, not extrapolation.
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


def build_model(dropout_rate: float) -> tf.keras.Model:
    layers = [tf.keras.layers.Input(shape=(1,))]
    for _ in range(3):
        layers.append(tf.keras.layers.Dense(16, activation="relu"))
        if dropout_rate:
            layers.append(tf.keras.layers.Dropout(dropout_rate))
    layers.append(tf.keras.layers.Dense(1))
    model = tf.keras.Sequential(layers)
    model.compile(optimizer="adam", loss="mse")
    return model


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--output", default="outputs")
    args = parser.parse_args()
    if args.epochs < 1:
        parser.error("--epochs must be at least 1")
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    tf.keras.utils.set_random_seed(42)
    rng = np.random.default_rng(42)
    x = rng.uniform(0, np.pi, size=(1200, 1)).astype("float32")
    x_train, x_test = x[:1000], x[1000:]
    y_train, y_test = np.sin(x_train), np.sin(x_test)
    grid = np.linspace(0, np.pi, 300, dtype="float32").reshape(-1, 1)

    fig, ax = plt.subplots()
    ax.plot(grid, np.sin(grid), color="black", label="Actual sin(x)")
    for label, rate in (("No dropout", 0.0), ("Dropout 5%", 0.05)):
        tf.keras.utils.set_random_seed(42)
        model = build_model(rate)
        model.fit(x_train, y_train, epochs=args.epochs, batch_size=32, verbose=0, validation_split=0.1)
        test_mse = model.evaluate(x_test, y_test, verbose=0)
        print(f"{label}: held-out MSE = {test_mse:.6f}")
        predictions = model.predict(grid, verbose=0)
        ax.plot(grid, predictions, label=f"{label} (MSE {test_mse:.4f})")
    ax.set(xlabel="x (radians)", ylabel="Function value", title="Neural-network approximation of sin(x)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output / "sine_approximation.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
