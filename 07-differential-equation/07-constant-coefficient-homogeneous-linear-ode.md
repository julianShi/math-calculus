## 二阶常系数齐次线性微分方程

### 特征方程法

先从求解二阶方程入手

$y''+py'+qy=0$

我们来猜测解的形式。因为指数函数 $e^{rx}$ 有比较好的性质，即各阶导数只相差一个常数比例，所以用待定系数法，猜测解的形式。代入后，得到

$\left( e^{rx}\right) ''+p\left( e^{rx}\right) '+q\left( e^{rx}\right) =0$

$\left( r^{2} +pr+q\right) e^{rx} =0$

$r^{2} +pr+q=0$

关于r的特征方程。可知r 有两个解

| 条件       | 特征方程解                         | 方程通解                                |
| ---------- | ---------------------------------- | --------------------------------------- |
| $p^2-4q>0$ | $\frac{-p\pm \sqrt{p^{2} -4q}}{2}$ | $C_{1} e^{r_{1} x} +C_{2} e^{r_{2} x}$  |
| $p^2-4q=0$ | $-p/2$                             | $C_{1} e^{r_{1} x} +C_{2} xe^{r_{1} x}$ |
| $p^2-4q<0$ | $\frac{-p\pm i\sqrt{4q-p^{2}}}{2}$ | $C_{1} e^{r_{1} x} +C_{2} e^{r_{2} x}$  |

**符号计算器**

通解

> 读者可以打开网页https://bubbleuniverse.github.io/symbolic/calculator，
>
> 把下列 LaTeX 源码贴入输入框中
>
> ```latex
> \frac{d}{dx}\frac{d}{dx}f(x)+p\frac{d}{dx}f(x)+qf(x)
> ```
>
> 选择 "求解微分方程 dsolve"，点击 “计算”按钮，就可以求解出
> $$
> f{\left(x \right)} = C_{1} e^{\frac{x \left(- p + \sqrt{p^{2} - 4 q}\right)}{2}} + C_{2} e^{- \frac{x \left(p + \sqrt{p^{2} - 4 q}\right)}{2}}
> $$

当有重根

> 读者可以打开网页https://bubbleuniverse.github.io/symbolic/calculator，
>
> 把下列 LaTeX 源码贴入输入框中
>
> ```latex
> \frac{d}{dx}\frac{d}{dx}f(x)+2p\frac{d}{dx}f(x)+p^2f(x)
> ```
>
> 选择 "求解微分方程 dsolve"，点击 “计算”按钮，就可以求解出
> $$
> f{\left(x \right)} = \left(C_{1} + C_{2} x\right) e^{- p x}
> $$

当有复数根

> 读者可以打开网页https://bubbleuniverse.github.io/symbolic/calculator，
>
> 把下列 LaTeX 源码贴入输入框中
>
> ```latex
> \frac{d}{dx}\frac{d}{dx}f(x)+p\frac{d}{dx}f(x)+p^2f(x)
> ```
>
> 选择 "求解微分方程 dsolve"，点击 “计算”按钮，就可以求解出
> $$
> f{\left(x \right)} = C_{1} e^{\frac{p x \left(-1 + \sqrt{3} i\right)}{2}} + C_{2} e^{- \frac{p x \left(1 + \sqrt{3} i\right)}{2}}
> $$



### 线性空间法

特征方程法非常便捷。但是有没有可能遗漏任何解呢？我们用更严格的线性空间法，再推导一遍通解。

定义 $z=y'$，则原方程可以写成一阶线性方程组的形式

$z'+pz+qy=0$

写成矩阵形式

$$
\begin{pmatrix}
y'\\
z'
\end{pmatrix} =\begin{pmatrix}
0 & 1\\
-q & -p
\end{pmatrix}\begin{pmatrix}
y\\
z
\end{pmatrix}
$$

$$
\mathbf{y} '=\mathbf{Ay}
$$

### 特征方程无重根

若

$p^2-4q\neq 0$

可将常系数矩阵 $\mathbf{A}$ 对角化，

$$
\mathbf{A} = \mathbf{P}^{-1}\mathbf{\Lambda P}
$$

得到

$$
\mathbf{P}\mathbf{y} '=\mathbf{\Lambda Py}
$$

对角化之后，各行线性无关

$$
(\mathbf{Py})_{i} '=\lambda _{i}(\mathbf{Py})_{i}
$$

易得到一阶微分方程的通解是
$$
(\mathbf{Py})_{i} =c_{i} e^{\lambda _{i} x}
$$

$$
\mathbf{y} =\mathbf{P}^{-1}\left( c_{i} e^{\lambda _{i} x}\right)=\mathbf{P}^{-1}\mathbf{C}\left( e^{\lambda _{i} x}\right)
$$
其中 $\mathbf{C}$  是对角阵。

因为 $\mathbf{P}$ 是线性变换，我们只需要改变一下系数的形式。定义
$$
\mathbf{D} =\mathbf{P}^{-1}\mathbf{C}
$$
即得到通解

$y_{i} =\sum _{j} D_{j} e^{\lambda _{j} x}$

### 特征方程有重根

对于 $p^2-4q = 0$， 进而特征根 $\lambda _{1} =\lambda _{2} =\lambda =-p/2$，导致 $\mathbf{A}$ 不可对角化的情况，可以这么处理。

这个时候，方程可以重写为

$y''+py'+\frac{p^2}{4}y=0$

用特征根表示更好

$y''-2\lambda y'+\lambda^2 y=0$

类似于因式分解，我们得到

$\left( y'-\lambda y\right) '-\lambda\left( y' -\lambda y\right) =0$

的美妙形式。这个形式不是简单拼凑出来的，而是重根固有的性质。接下来定义

$z=y'- \lambda y$

那么得到方程

$z' - \lambda z=0$

这是一阶齐次线性方程，有通解

$z=C_1e^{\lambda x}$

代回到z的定义，得到

$y'-\lambda y = C_1e^{\lambda x}$

这是一阶非齐次线性方程，也有通解

$y =  \left(C_{2} + C_{1} x\right) e^{\lambda x} $

这个方法可以推广到高阶，比如说有3重根的情况。读者可以自行尝试。



### 特征方程有重根与非重根

拿4阶齐次线性微分方程举例。例如，假设有四个特征值 $\lambda,\lambda,\lambda_1,\lambda_2$， 其中两个 $\lambda$ 是重根。那么可以作如下变量替换，把原高阶方程变成一阶方程组

$z=y' -\lambda _{1} y$

$z_{1} =z' -\lambda _{2} z$

$\zeta _{1} =( z_{1} ' -\lambda z_{1})$

$\zeta _{1} ' -\lambda \zeta _{1} =0$

其对应的矩阵形式是
$$
\begin{pmatrix}
y'\\
z'\\
z_{1} '\\
\zeta _{1} '
\end{pmatrix} =\begin{pmatrix}
\lambda _{1} & 1 &  & \\
 & \lambda _{2} & 1 & \\
 &  & \lambda  & 1\\
 &  &  & \lambda 
\end{pmatrix}\begin{pmatrix}
y\\
z\\
z_{1}\\
\zeta _{1}
\end{pmatrix}
$$
根据线性代数知识，这是分块上三角矩阵
$$
\mathbf{A} =\begin{pmatrix}
\mathbf{B} & \mathbf{C}\\
\mathbf{0} & \mathbf{D}
\end{pmatrix}
$$
其中，$\mathbf{B}$ 可对角化，$\mathbf{D}$ 不可对角化，$\mathbf{C}$ 可以通过相似变换消去。

可以构造相似变换矩阵 $\mathbf{P}$, 使得
$$
\mathbf{P}^{-1}\mathbf{A}\mathbf{P} =\begin{pmatrix}
\mathbf{B} ' & \mathbf{0}\\
\mathbf{0} & \mathbf{D}
\end{pmatrix}
$$

再根据上两节知识，分别求解两部分方程的通解。

