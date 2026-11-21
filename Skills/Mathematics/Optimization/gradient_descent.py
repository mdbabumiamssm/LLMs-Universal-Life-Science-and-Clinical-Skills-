# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA


def function_to_optimize(x):
    """
    f(x) = x^2 + 4x + 4
    Minimum is at x = -2 (Value 0)
    """
    return x**2 + 4*x + 4

def gradient(x):
    """
    Derivative f'(x) = 2x + 4
    """
    return 2*x + 4

def gradient_descent(start_x, learning_rate, epochs):
    x = start_x
    history = []
    
    print(f"Starting Gradient Descent at x={x}")
    print(f"Learning Rate: {learning_rate}, Epochs: {epochs}")
    print("-" * 30)
    
    for i in range(epochs):
        grad = gradient(x)
        step = learning_rate * grad
        
        # Store history for visualization
        history.append((x, function_to_optimize(x)))
        
        print(f"Epoch {i+1}: x = {x:.4f}, Grad = {grad:.4f}, f(x) = {function_to_optimize(x):.4f}")
        
        # Update rule: x = x - alpha * gradient
        x = x - step
        
    print("-" * 30)
    print(f"Global Minimum found at: x = {x:.4f}")
    return x, history

if __name__ == "__main__":
    # Start at random point x = 5
    final_x, hist = gradient_descent(start_x=5, learning_rate=0.1, epochs=20)
    
    # Simple ASCII plot of the descent
    print("\nDescent Path (Value of f(x)):")
    for val in hist:
        # Simple bar chart
        bar = "#" * int(val[1])
        print(f"{val[1]:.2f} | {bar}")

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
