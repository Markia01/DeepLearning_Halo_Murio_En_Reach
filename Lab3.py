# perceptron used for binary classification for NAND logic gates

input_data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]


def not_heaviside(x): return 1 if x <= 0 else 0


expected_output = [1, 1, 1, 0]  # AND logic gate
weights = [1, 1]
bias = -1.5
for x in input_data:
    linear_combination = sum(w*i for w, i in zip(weights, x)) + bias
    prediction = not_heaviside(linear_combination)
    print(f"Input: {x}, Prediction: {prediction}")
