## 二阶常系数齐次线性微分方程

### 特征方程法

先从求解二阶方程入手

$y''+py'+qy=0$

我们来猜测解的形式。因为指数函数 $e^{rx}$ 有比较好的性质，即各阶导数只相差一个常数比例，所以用待定系数法，猜测解的形式。代入后，得到

$\displaystyle \left( e^{rx}\right) ''+p\left( e^{rx}\right) '+q\left( e^{rx}\right) =0$

$\displaystyle \left( r^{2} +pr+q\right) e^{rx} =0$

$\displaystyle r^{2} +pr+q=0$

关于r的特征方程。可知r 有两个解

| 条件       | 特征方程解                         | 方程通解                                |
| ---------- | ---------------------------------- | --------------------------------------- |
| $p^2-4q>0$ | $\frac{-p\pm \sqrt{p^{2} -4q}}{2}$ | $C_{1} e^{r_{1} x} +C_{2} e^{r_{2} x}$  |
| $p^2-4q=0$ | $-p/2$                             | $C_{1} e^{r_{1} x} +C_{2} xe^{r_{1} x}$ |
| $p^2-4q<0$ | $\frac{-p\pm i\sqrt{4q-p^{2}}}{2}$ | $C_{1} e^{r_{1} x} +C_{2} e^{r_{2} x}$  |

### 线性空间法

特征方程法非常便捷。但是有没有可能遗漏任何解呢？我们用更严格的线性空间法，再推导一遍通解。

定义 $z=y'$，则原方程可以写成一阶线性方程组的形式

$z'+pz+qy=0$

写成矩阵形式

$\displaystyle \begin{pmatrix}
y'\\
z'
\end{pmatrix} =\begin{pmatrix}
0 & 1\\
-q & -p
\end{pmatrix}\begin{pmatrix}
y\\
z
\end{pmatrix}$

$\boldsymbol{y} '=\boldsymbol{Ay}$

若

$p^2-4q\neq 0$

可将常系数矩阵 $\boldsymbol{A}$ 对角化，

$\mathbf{A} = \mathbf{P}^{-1}\mathbf{\Lambda P}$

得到

$\boldsymbol{P}\boldsymbol{y} '=\boldsymbol{\Lambda Py}$

对角化之后，各行线性无关

$(\mathbf{Py})_{i} '=\lambda _{i}(\mathbf{Py})_{i}$

易得到一阶微分方程的通解是

$(\mathbf{Py})_{i} =C_{i} e^{\lambda _{i} x}$

$\mathbf{y} =\mathbf{P}^{-1}\left( C_{i} e^{\lambda _{i} x}\right)=\mathbf{P}^{-1}\mathbf{C}\left( e^{\lambda _{i} x}\right)$

其中 $\mathbf{C}$  是对角阵。

因为 $\mathbf{P}$ 是线性变换，我们只需要改变一下系数的形式。定义

$\mathbf{D} =\mathbf{P}^{-1}\mathbf{C}$

即得到

$y_{i} =\sum _{j} D_{j} e^{\lambda _{j} x}$



对于 $p^2-4q = 0$， 导致 $\mathbf{A}$ 不可对角化的情况，请读者尝试证明。

