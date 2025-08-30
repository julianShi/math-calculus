满足狄利克雷边界条件 Dirichlet Boundary Conditions 的周期函数，可以展开成为无穷正弦和余弦和的形式，也叫做傅立叶级数。

### 三角函数的正交性

先回顾一下三角函数的正交性

$\int _{-\pi }^{\pi }\sin( mx)\sin( nx) dx=\pi \delta _{mn}$

$\int _{-\pi }^{\pi }\cos( mx)\cos( nx) dx=\pi \delta _{mn}$

$\int _{-\pi }^{\pi }\sin( mx)\cos( nx) dx=0$

$\int _{-\pi }^{\pi }\sin( mx) dx=0$

$\int _{-\pi }^{\pi }\cos( mx) dx=0$

其中 $\delta _{mn}$  是克罗内克 delta 函数，整数 $m\neq 0,n\neq 0$。意味着，当 $m\neq n$，积分为0，两组三角函数基底正交。

### 傅立叶级数

由于这些函数在 $[ -\pi ,\pi ]$ 上构成完备正交函数系，函数可以取如下形式

$$
f( x) =\frac{a_{0}}{2} +\sum _{n=1}^{\infty } a_{n}\cos( nx) +\sum _{n=1}^{\infty } b_{n}\sin( nx)
$$

其中

$a_{0} =\frac{1}{\pi }\int _{-\pi }^{\pi } f( x) dx$

$a_{n} =\frac{1}{\pi }\int _{-\pi }^{\pi } f( x)\cos( nx) dx$

$b_{n} =\frac{1}{\pi }\int _{-\pi }^{\pi } f( x)\sin( nx) dx$

###  证明

对 $f( x)$的傅立叶展开式左右乘以 $\cos( mx)$，并在  $[ -\pi ,\pi ]$ 上积分，

$$
\int _{-\pi }^{\pi } f( x)\cos( mx) dx=\frac{a_{0}}{2}\int _{-\pi }^{\pi }\cos( mx) dx+\sum _{n=1}^{\infty } a_{n}\int _{-\pi }^{\pi }\cos( nx)\cos( mx) dx+\sum _{n=1}^{\infty } b_{n}\int _{-\pi }^{\pi }\sin( nx)\cos( mx) dx
$$

注意到，右侧

$\int _{-\pi }^{\pi }\cos( nx)\cos( mx) dx$ 只有当 $m=n$，才有非0定积分 $\pi $

所以

$\int _{-\pi }^{\pi } f( x)\cos( mx) dx=\pi a_{m}$

所以

$a_{m} =\frac{1}{\pi }\int _{-\pi }^{\pi } f( x)\cos( mx) dx$

同理，得到其他系数的表达式

证毕