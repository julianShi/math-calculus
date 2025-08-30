满足狄利克雷边界条件 Dirichlet Boundary Conditions 的周期复变函数，也可以展开成为无穷正弦和余弦和的形式。

### 欧拉公式

先回顾一下欧拉公式

$$
e^{ix}=\cos{}x+i\sin{}x
$$

以及其正交性

$$
\int _{-\pi }^{\pi } e^{inx} dx=\int _{-\pi }^{\pi } (\cos nx+i\sin nx) dx=0
$$

其中 $n=\pm 1,\pm 2,...$

用欧拉公式表示傅立叶级数
$$
f( x) =\sum _{n=-\infty }^{\infty } a_{n} e^{inx}
$$


其中

$$
a_{n} =\frac{1}{2\pi }\int _{-\pi }^{\pi } f(x)e^{-inx} dx
$$

### 证明

对 $f( x)$的傅立叶展开式左右乘以 $e^{-imx}$，并在 $[ -\pi ,\pi ]$ 上积分，

$$
\int _{-\pi }^{\pi } f( x) e^{-imx} dx=\sum _{n=-\infty }^{\infty } a_{n}\int _{-\pi }^{\pi } e^{inx} e^{-imx} dx
$$

注意到，右侧 $\int _{-\pi }^{\pi } e^{inx} e^{-imx} dx$ 只有当 $m=n$，才有非0定积分 $2\pi $

所以

$$
\int _{-\pi }^{\pi } f( x)\cos( mx) dx=2\pi a_{m}
$$

即

$$
a_{m} =\frac{1}{2\pi } \int _{-\pi }^{\pi } f( x) e^{-imx} dx
$$

证毕

