对于有非 $y^{(n)}$ 项的高阶常系数非齐次线性微分方程

$$
y^{( n)} +a_{1} y^{( n-1)} +...+a_{n-1} y^{( 1)} +a_{n} y=f(x)
$$

我们推导其通解。

## 线性空间法

### 特征方程无重根

可参照上一节，将高阶方程转化为一阶方程组

$$
\mathbf{y} '=\mathbf{Ay} +\mathbf{f}(x)
$$


其中

$$
\mathbf{f}(x) =( 0,0,...,0,f( x))^{T}
$$


可将常系数矩阵 $\boldsymbol{A}$ 对角化，

$$
\mathbf{A} = \mathbf{P}^{-1}\mathbf{\Lambda P}
$$


则原方程组为

$$
\mathbf{Py} '=\Lambda \mathbf{Py} +\mathbf{Pf}(x)
$$


即求一阶常系数非齐次线性微分方程组

$$
\mathbf{z} '=\mathbf{\Lambda z} +\mathbf{b}( x)
$$


其中

$$
\mathbf{z} =\mathbf{Py} ,\mathbf{b}( x) =\mathbf{Pf}( x)
$$


其中第 i 项有

$$
z_{i} '=\lambda _{i} z_{i} +b_{i}( x)
$$


其通解为

$$
z_{i} =e^{\int \lambda _{i} dx}\left(\int b_{i}( x) e^{-\int \lambda _{i} dx} dx+C_{i}\right)
$$


求出 $\mathbf{z}$ 之后，再通过线性变换得到

$$
\mathbf{y} =\mathbf{P}^{-1}\mathbf{z} 
$$


### 特征方程有重根与非重根

还是拿上一节4阶齐次线性微分方程举例。但是这次交换换元顺序，得到

$$
\displaystyle \zeta _{1} =y' -\lambda y
$$


$$
\displaystyle \zeta _{2} =\zeta _{1} ' -\lambda \zeta _{1}
$$


$$
\displaystyle z_{1} =\zeta _{2} ' -\lambda _{1} \zeta _{2}
$$


$$
\displaystyle z_{1} ' -\lambda _{2} z_{1} =f(x)
$$


$$
\displaystyle \begin{pmatrix}
y'\\
\zeta _{1} '\\
\zeta _{2} '\\
z_{1} '
\end{pmatrix} =\begin{pmatrix}
\lambda  & 1 &  & \\
 & \lambda  & 1 & \\
 &  & \lambda _{1} & 1\\
 &  &  & \lambda _{2}
\end{pmatrix}\begin{pmatrix}
y\\
\zeta _{1}\\
\zeta _{2}\\
z_{1}
\end{pmatrix}
$$


分解成上下两块

$$
\displaystyle \begin{pmatrix}
y'\\
z'
\end{pmatrix} =\begin{pmatrix}
\mathbf{B} & \mathbf{C}\\
0 & \mathbf{D}
\end{pmatrix}\begin{pmatrix}
y\\
z
\end{pmatrix} +\begin{pmatrix}
\mathbf{0}\\
\mathbf{f}( x)
\end{pmatrix}
$$


即

$$
\displaystyle \mathbf{y} '=\mathbf{By} +\mathbf{Cz}
$$


$$
\mathbf{z} '=\mathbf{Dz} +\mathbf{f}( x)
$$


其中， $\mathbf{B}$ 不可对角化的上三角矩阵， $\mathbf{D}$ 可对角化。

根据 "**特征方程无重根** " 中介绍的方法，可求得通解 $\mathbf{z}( x)$


进而求解

$$
\displaystyle \mathbf{y} '=\mathbf{By} +\mathbf{g}(x)
$$


其中 

$$
\mathbf{g}(x)=\mathbf{Cz}(x)
$$


因为 $\mathbf{B}$ 不可对角化的上三角矩阵，所以可以展开成为标量形式，从下到上依次求解一阶常系数非齐次线性微分方程，得到通解 $\mathbf{y}(x)$。

## 线性算子法

线性算子法可以避免重根和非重根的讨论

已知常系数线性微分方程的特征方程有特征根系 

$\lambda _{i} ,i=1,2,...,n$

，则可进行因式分解

$\left[\prod _{i=1}^{n}\left(\frac{d}{dx} -\lambda _{i}\right)\right] y=b( x)$

出于简化书写的目的，定义微分算子 $D=\frac{d}{dx}$，则上式可重写为

$\left[\prod _{i=1}^{n}( D-\lambda _{i})\right] y=b( x)$

每次释放出一个括号，即

$\left[\prod _{i=1}^{n-1}( D-\lambda _{i})\right]( D-\lambda _{n}) y=b( x)$

若定义 $y_{1} =( D-\lambda _{n}) y$，则

$\left[\prod _{i=1}^{n-1}( D-\lambda _{i})\right] y_{1} =b( x)$

释放到最后一个括号之后

$( D-\lambda _{1}) y_{n-1} =b( x)$

这个时候需要求解的是一个一阶常系数非齐次线形微分方程。其有通解

$y_{n-1} =y_{n-1}( x)$

将其代回定义

$y_{n-1}( x) =( D-\lambda _{2}) y_{n-2}$

，则变成求解 $y_{n-2}$ 的另一个 一阶常系数非齐次线形微分方程，有通解

$y_{n-2} =y_{n-2}( x)$

逐次求解，则可得到 $y( x)$ 的通解表达式。

这是编程中常用的递归方法。虽然没有线性空间法书写起来简洁，但是适用于单线程编程。

### 代码编程

以下是SymPy 迭代算法的实现

```python
# dsolve is capable of solving high-order linear ODE
# I rewrite the algorithm, simply for demonstration
# lambdas are the coefficients
# bx is the non-homogeneous part as a function of x
def dsolve_nth_linear_ode(lambdas, bx):
  yx = bx
  for lambda_ in lambdas:
    x = Symbol('x')
    y = Function('y')(x)
    lhs = y.diff(x) - lambda_ * y - yx
    # I used the built-in dsolve to solve the first order ODE
    sol = dsolve(Eq(lhs, yx), y, hint='1st_linear')
    yx = sol.rhs
  return yx
```

> 读者们可能有注意到，ipynb 文件中，用 $f(x)$ 作为待求方程。这是因为在 多变量微积分中，$y,z$ 常被用作自变量。所以 就只能用 $f,g,h$ 这些字母表示方程了

### 微分算子的适用范围

需要说明的是，微分算子法不适用于非常系数微分方程。

微分算子满足 结合律，分配律，但是不满足交换律。比如说

$\displaystyle D\lambda ( x) \neq \lambda ( x) D$

证明：

$\displaystyle ( D\lambda ( x)) y( x) =\frac{d}{dx}( \lambda ( x) y( x)) =\left(\frac{d}{dx} \lambda ( x)\right) y( x) +\lambda ( x)\left(\frac{d}{dx} y( x)\right) \neq \lambda ( x)\left(\frac{d}{dx} y( x)\right)$

只有当 $\lambda(x)=\lambda$  为常系数的时候，$\frac{d}{dx} \lambda ( x) = 0 $，等号才成立。

这也就是为什么微分算子法 只适用于常系数微分方程，不适用于非常系数微分方程。
