import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

# ------------------------------------------------------------
# 1. Load data
# ------------------------------------------------------------
data = pd.read_csv("data/xy_data.csv")
x_data = data["x"].values
y_data = data["y"].values

# ------------------------------------------------------------
# 2. Parametric curve from the assignment
# ------------------------------------------------------------
def parametric_curve(t, theta_deg, M, X):
    theta = np.deg2rad(theta_deg)

    amplitude = np.exp(M * np.abs(t)) * np.sin(0.3 * t)

    x = (
        t * np.cos(theta)
        - amplitude * np.sin(theta)
        + X
    )

    y = (
        42
        + t * np.sin(theta)
        + amplitude * np.cos(theta)
    )

    return x, y


# ------------------------------------------------------------
# 3. Infer t for a candidate theta and X
# ------------------------------------------------------------
def calculate_t(x, y, theta_deg, X):
    theta = np.deg2rad(theta_deg)

    return (
        (x - X) * np.cos(theta)
        + (y - 42) * np.sin(theta)
    )


# ------------------------------------------------------------
# 4. L1 loss
#
# For a candidate theta, M, X:
#   - infer t for every observed point
#   - generate the corresponding point on the model
#   - calculate |dx| + |dy|
# ------------------------------------------------------------
def l1_loss(params):
    theta_deg, M, X = params

    t = calculate_t(x_data, y_data, theta_deg, X)

    # Assignment constraint: 6 < t < 60
    if np.any(t <= 6) or np.any(t >= 60):
        return 1e6 + np.sum(np.maximum(6 - t, 0))
        + np.sum(np.maximum(t - 60, 0))

    x_pred, y_pred = parametric_curve(t, theta_deg, M, X)

    error = np.abs(x_data - x_pred) + np.abs(y_data - y_pred)

    return np.mean(error)


# ------------------------------------------------------------
# 5. Optimize theta, M and X
# ------------------------------------------------------------
bounds = [
    (0.000001, 49.999999),       # theta
    (-0.049999, 0.049999),       # M
    (0.000001, 99.999999)        # X
]

result = differential_evolution(
    l1_loss,
    bounds,
    seed=42,
    popsize=20,
    maxiter=1000,
    tol=1e-10,
    polish=True
)

theta, M, X = result.x

print("\nFinal Parameters")
print("----------------")
print(f"theta = {theta:.8f} degrees")
print(f"M     = {M:.8f}")
print(f"X     = {X:.8f}")

print("\nL1 Loss")
print("-------")
print(f"{result.fun:.12f}")


# ------------------------------------------------------------
# 6. Plot observed points and fitted curve
# ------------------------------------------------------------
t_plot = np.linspace(6, 60, 5000)

x_curve, y_curve = parametric_curve(
    t_plot,
    theta,
    M,
    X
)

plt.figure(figsize=(10, 6))

plt.scatter(
    x_data,
    y_data,
    s=8,
    label="Given data"
)

plt.plot(
    x_curve,
    y_curve,
    linewidth=2,
    label="Fitted curve"
)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Parametric Curve Parameter Estimation")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("plots/fitted_curve.png", dpi=200)
plt.show()


# ------------------------------------------------------------
# 7. Save final answer
# ------------------------------------------------------------
with open("results/final_parameters.txt", "w") as f:
    f.write("Parametric Curve Parameter Estimation\n")
    f.write("-------------------------------------\n")
    f.write(f"theta = {theta:.10f} degrees\n")
    f.write(f"M     = {M:.10f}\n")
    f.write(f"X     = {X:.10f}\n")
    f.write(f"L1    = {result.fun:.12f}\n")
