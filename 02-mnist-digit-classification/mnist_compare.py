"""Compare fully connected MNIST classifiers with and without dropout.

Training/validation data come exclusively from the original training set.
The test set is reserved for final evaluation.
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


def create_model(dropout_rate: float) -> tf.keras.Model:
    layers = [tf.keras.layers.Input(shape=(784,))]
    for units in (200, 100, 60, 30):
        layers.append(tf.keras.layers.Dense(units, activation="relu"))
        if dropout_rate > 0:
            layers.append(tf.keras.layers.Dropout(dropout_rate))
    layers.append(tf.keras.layers.Dense(10, activation="softmax"))
    model = tf.keras.Sequential(layers)
    model.compile(optimizer="sgd", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--output", default="outputs")
    args = parser.parse_args()
    if args.epochs < 1:
        parser.error("--epochs must be at least 1")
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    tf.keras.utils.set_random_seed(42)
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train.reshape(-1, 784).astype("float32") / 255.0
    x_test = x_test.reshape(-1, 784).astype("float32") / 255.0

    results = {}
    for name, rate in (("no_dropout", 0.0), ("dropout_25pct", 0.25)):
        tf.keras.utils.set_random_seed(42)
        model = create_model(rate)
        history = model.fit(
            x_train, y_train,
            batch_size=160, epochs=args.epochs,
            validation_split=0.1, verbose=1,
        )
        test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
        results[name] = (history.history, test_loss, test_accuracy)
        print(f"{name}: test loss={test_loss:.4f}, test accuracy={test_accuracy:.4f}")

    for metric in ("accuracy", "loss"):
        fig, ax = plt.subplots()
        for name, (history, _, _) in results.items():
            ax.plot(history[metric], label=f"{name} training")
            ax.plot(history[f"val_{metric}"], linestyle="--", label=f"{name} validation")
        ax.set(xlabel="Epoch", ylabel=metric.capitalize(), title=f"MNIST {metric}: dropout comparison")
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(output / f"mnist_{metric}.png", dpi=150)
        plt.close(fig)


if __name__ == "__main__":
    main()
