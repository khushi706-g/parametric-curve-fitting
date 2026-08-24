# Parametric Curve Fitting

## Research and Development / AI Assignment

This project solves the given **parametric curve parameter estimation** problem. The objective is to determine the unknown parameters $\theta$, $M$, and $X$ from a set of points lying on the curve.

---

## Problem Statement

The given parametric curve is:

$$
x(t)=t\cos(\theta)-e^{M|t|}\sin(0.3t)\sin(\theta)+X
$$

$$
y(t)=42+t\sin(\theta)+e^{M|t|}\sin(0.3t)\cos(\theta)
$$

The unknown parameters are:

$$
\theta,\quad M,\quad X
$$

The dataset `xy_data.csv` contains points that lie on this curve. The task is to estimate the values of the unknown parameters from these points.

---

## Parameter Constraints

The assignment specifies the following ranges:

$$
0^\circ < \theta < 50^\circ
$$

$$
-0.05 < M < 0.05
$$

$$
0 < X < 100
$$

The parameter $t$ lies in the range:

$$
6 < t < 60
$$

These constraints are used during the parameter estimation process.

---

## Dataset

The provided dataset contains the points lying on the curve.

The dataset consists of:

* **1500 data points**
* Two variables: `x` and `y`
* No missing values

Each row represents a point:

$$
(x_i,y_i)
$$

The data is visualized before parameter estimation to understand the shape of the given curve.

---

# Approach

The parameter estimation is performed through the following steps:

1. Load the given dataset.
2. Visualize the `(x,y)` points.
3. Implement the given parametric equations.
4. Transform the equations to obtain the corresponding value of $t$.
5. Define an L1-based error function.
6. Optimize $\theta$, $M$, and $X$ within the given constraints.
7. Generate the predicted curve using the estimated parameters.
8. Compare the predicted curve with the supplied data.

---

## Mathematical Transformation

The original equations are:

$$
x(t)=t\cos(\theta)-e^{M|t|}\sin(0.3t)\sin(\theta)+X
$$

$$
y(t)=42+t\sin(\theta)+e^{M|t|}\sin(0.3t)\cos(\theta)
$$

Since:

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

The equations can then be written as:

$$
x-X=t\cos(\theta)-A\sin(\theta)
$$

$$
y-42=t\sin(\theta)+A\cos(\theta)
$$

These equations represent a rotation of the quantities $t$ and $A$.

### Recovering $t$

Multiplying the first equation by $\cos(\theta)$ and the second equation by $\sin(\theta)$ and adding them gives:

$$
t=(x-X)\cos(\theta)+(y-42)\sin(\theta)
$$

Therefore, for a candidate $\theta$ and $X$, the corresponding value of $t$ can be calculated for every observed point.

### Recovering the Oscillatory Component

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

This relationship is used to estimate the unknown parameters.

---

# L1 Distance

The assignment evaluates the solution using the **L1 distance between uniformly sampled points of the expected and predicted curves**.

For corresponding points, the L1 distance is calculated as:

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

The objective is to find the parameter values that minimize this error.

A smaller L1 distance indicates a closer match between the expected and predicted curves.

---

# Parameter Optimization

The unknown parameters are estimated within the constraints specified in the assignment:

$$
0^\circ < \theta < 50^\circ
$$

$$
-0.05 < M < 0.05
$$

$$
0 < X < 100
$$

A nonlinear optimization approach is used to search for the parameter combination that minimizes the L1 error.

The implementation uses **Differential Evolution** from SciPy for the parameter search.

```python
from scipy.optimize import differential_evolution
```

Differential Evolution performs a global search over the allowed parameter space and is suitable for this nonlinear parametric curve.

---

# Results

The estimated parameters obtained from the supplied dataset are:

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

# Final Parametric Curve

Substituting the estimated parameters into the original equations gives:

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

where:

$$
6<t<60
$$

---

# Visualization

The estimated parameters are used to generate the predicted parametric curve.

The curve is generated using uniformly sampled values of $t$ between 6 and 60 and is compared with the supplied `(x,y)` points.

The resulting plot is included in the repository as:

```text
plots/fitted_curve.png
```

The visualization shows the close agreement between the supplied data points and the estimated parametric curve.

---

## Desmos Visualization

The assignment also provides an interactive **Desmos visualization** of the parametric curve.

### Interactive Graph

[**Open Parametric Curve in Desmos**](https://www.desmos.com/calculator/rfj91yrxob)

The Desmos visualization can be used to:

* View the parametric curve interactively.
* Understand the effect of $\theta$, $M$, and $X$.
* Observe how changing the parameters affects the curve.
* Visually verify the estimated parameters.

Using the estimated parameters:

$$
\theta=30^\circ,\qquad M=0.03,\qquad X=55
$$

the resulting curve is:

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

# Conclusion

The unknown parameters of the given parametric curve were estimated using mathematical transformation and constrained nonlinear optimization.

The final estimated values are:

$$
\boxed{
\theta=30^\circ,\quad
M=0.03,\quad
X=55
}
$$

These values satisfy the parameter constraints specified in the assignment and produce a curve that closely matches the supplied dataset.

---

