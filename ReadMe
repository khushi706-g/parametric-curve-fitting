# Parametric Curve Fitting

Research and Development / AI Assignment — Parametric Curve Parameter Estimation

## Problem Statement

The objective of this assignment is to find the unknown parameters of a given parametric curve using a set of points that lie on the curve.

The given parametric equations are:

$$
x(t)=t\cos(\theta)-e^{M|t|}\sin(0.3t)\sin(\theta)+X
$$

$$
y(t)=42+t\sin(\theta)+e^{M|t|}\sin(0.3t)\cos(\theta)
$$

The unknown parameters are:

$$
\theta,\ M,\ X
$$

The assignment provides a set of `(x,y)` points in `xy_data.csv`, and the task is to determine the values of the unknown parameters that produce the given curve.

---

## Parameter Constraints

The parameters must satisfy the following constraints:

| Parameter | Range                         |
| :-------: | :---------------------------- |
|  $\theta$ | $0^\circ < \theta < 50^\circ$ |
|    $M$    | $-0.05 < M < 0.05$            |
|    $X$    | $0 < X < 100$                 |
|    $t$    | $6 < t < 60$                  |

These ranges are specified in the assignment.

---

## Dataset

The dataset provided with the assignment contains points lying on the parametric curve.

The dataset used in this repository is:

```text
data/xy_data.csv
```

It contains two columns:

```text
x
y
```

The dataset contains **1500 `(x,y)` points**.

Each row represents one observed point:

$$
(x_i,y_i)
$$

---

## Objective

The objective is to estimate $\theta$, $M$, and $X$ such that the generated curve closely matches the given data.

The assignment evaluates the solution using:

> The L1 distance between uniformly sampled points between the expected and predicted curve.

The assignment also evaluates:

* Explanation of the complete process and steps followed
* Submitted code / GitHub repository

Therefore, the primary objective is to minimize the distance between the expected curve and the predicted curve.

---

# Approach

The complete solution follows these steps:

```text
             Given XY Data
                   |
                   v
          Data Preprocessing
                   |
                   v
          Visualize the Data
                   |
                   v
       Define Parametric Equation
                   |
                   v
       Mathematical Transformation
                   |
                   v
           Define L1 Loss
                   |
                   v
       Optimize θ, M and X
                   |
                   v
         Generate Final Curve
                   |
                   v
       Compare with Given Data
```

---

## 1. Load the Dataset

The dataset is loaded using Pandas.

```python
import pandas as pd

df = pd.read_csv("data/xy_data.csv")

x_data = df["x"].values
y_data = df["y"].values
```

The data is then inspected to verify its dimensions and check for missing values.

---

## 2. Visualize the Given Data

The `(x,y)` points are plotted using Matplotlib.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.scatter(
    x_data,
    y_data,
    s=8
)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Given XY Data")

plt.show()
```

This visualization provides an initial understanding of the shape of the curve.

---

# Mathematical Formulation

The original equations are:

$$
x(t)=t\cos(\theta)-e^{M|t|}\sin(0.3t)\sin(\theta)+X
$$

$$
y(t)=42+t\sin(\theta)+e^{M|t|}\sin(0.3t)\cos(\theta)
$$

Since the assignment specifies:

$$
6<t<60
$$

we have:

$$
|t|=t
$$

Define:

$$
A=e^{Mt}\sin(0.3t)
$$

The equations then become:

$$
x-X=t\cos(\theta)-A\sin(\theta)
$$

$$
y-42=t\sin(\theta)+A\cos(\theta)
$$

These equations can be interpreted as a rotation of the quantities $t$ and $A$.

---

## Recovering `t`

Multiplying the first equation by $\cos(\theta)$ and the second equation by $\sin(\theta)$ and adding them:

$$
(x-X)\cos(\theta)+(y-42)\sin(\theta)=t
$$

Therefore:

$$
\boxed{
t=(x-X)\cos(\theta)+(y-42)\sin(\theta)
}
$$

This gives the value of `t` corresponding to an observed `(x,y)` point for a candidate $\theta$ and $X$.

---

## Recovering the Oscillatory Component

The perpendicular transformation gives:

$$
A=-(x-X)\sin(\theta)+(y-42)\cos(\theta)
$$

Since:

$$
A=e^{Mt}\sin(0.3t)
$$

we obtain:

$$
-(x-X)\sin(\theta)+(y-42)\cos(\theta)
=====================================

e^{Mt}\sin(0.3t)
$$

This relationship is used during parameter estimation.

---

# Parametric Curve Implementation

The mathematical model is implemented in Python as:

```python
import numpy as np

def parametric_curve(t, theta_deg, M, X):

    theta = np.deg2rad(theta_deg)

    amplitude = (
        np.exp(M * np.abs(t))
        * np.sin(0.3 * t)
    )

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
```

The angle $\theta$ is specified in degrees in the assignment, while NumPy's trigonometric functions operate in radians. Therefore, $\theta$ is converted using:

```python
theta = np.deg2rad(theta_deg)
```

---

# L1 Loss Function

For a candidate parameter set:

$$
(\theta,M,X)
$$

the corresponding `t` values are calculated and the predicted coordinates are generated.

For every data point, the L1 distance is calculated as:

$$
L_i=
|x_i-x_{pred,i}|
+
|y_i-y_{pred,i}|
$$

The mean L1 loss is:

$$
L=
\frac{1}{N}
\sum_{i=1}^{N}
\left(
|x_i-x_{pred,i}|
+
|y_i-y_{pred,i}|
\right)
$$

The optimization process attempts to minimize this loss.

A smaller value of $L$ indicates a closer match between the generated curve and the supplied data.

---

# Parameter Optimization

The unknown parameters are optimized subject to the assignment constraints.

The search space is:

$$
0<\theta<50^\circ
$$

$$
-0.05<M<0.05
$$

$$
0<X<100
$$

The implementation uses **Differential Evolution** from SciPy:

```python
from scipy.optimize import differential_evolution
```

Differential Evolution performs a global search over the parameter space and is suitable for this nonlinear curve-fitting problem.

The optimization objective is the L1 loss defined above.

---

# Results

The parameters estimated from the supplied dataset are:

| Parameter | Estimated Value |
| :-------: | --------------: |
|  $\theta$ |         **30°** |
|    $M$    |        **0.03** |
|    $X$    |          **55** |

Therefore:

$$
\boxed{\theta=30^\circ}
$$

$$
\boxed{M=0.03}
$$

$$
\boxed{X=55}
$$

---

# Final Parametric Equation

After substituting the estimated parameters:

$$
x(t)=t\cos(30^\circ)
-e^{0.03|t|}
\sin(0.3t)\sin(30^\circ)
+55
$$

$$
y(t)=42+t\sin(30^\circ)
+e^{0.03|t|}
\sin(0.3t)\cos(30^\circ)
$$

with:

$$
6<t<60
$$

---

# Visualization

The recovered parameters are used to generate a uniformly sampled curve over the range:

$$
6\leq t\leq60
$$

The predicted curve is plotted together with the supplied `(x,y)` points.

The resulting visualization is available at:

```text
plots/fitted_curve.png
```

---

# Project Structure

```text
parametric-curve-fitting/
│
├── data/
│   └── xy_data.csv
│
├── plots/
│   └── fitted_curve.png
│
├── results/
│   └── final_parameters.txt
│
├── main.py
├── solution.ipynb
├── requirements.txt
├── .gitignore
└── ReadMe.md
```

---

# Requirements

The project requires Python 3 and the following libraries:

```text
numpy
pandas
matplotlib
scipy
jupyter
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# How to Run

## Using Jupyter Notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
solution.ipynb
```

Run the notebook cells sequentially.

## Using Python

Run:

```bash
python main.py
```

The program will:

1. Load the dataset.
2. Define the parametric curve.
3. Estimate $\theta$, $M$, and $X$.
4. Calculate the L1 loss.
5. Generate the fitted curve.
6. Display the result.
7. Save the estimated parameters.

---

# Final Answer

The unknown parameters obtained from the supplied dataset are:

$$
\boxed{
\theta=30^\circ,\quad
M=0.03,\quad
X=55
}
$$

---

# Assignment Reference

This project is based on the **Research and Development / AI Assignment**.

The assignment specifies:

* The parametric curve
* Unknown parameters $\theta$, $M$, and $X$
* Parameter ranges
* The supplied `xy_data.csv`
* L1-distance-based evaluation
* Explanation of the complete solution
* Code / GitHub submission

The assignment also states that the required final result is the values of the unknown variables, while additional mathematical and coding work used to estimate them is an advantage.
