## 常用积分公式

幂函数

$$
\int x^{a} dx=\frac{x^{a+1}}{a+1} +C
$$

$$
\int \frac{1}{x} dx=\ln |x|+C
$$

指数函数

$$
\int a^{x} dx=\frac{1}{\ln a} a^{x} +C
$$

三角函数

$$
\int \frac{1}{a^{2} +x^{2}} dx\ =\frac{1}{a} \ \arctan\frac{x}{a} +C
$$

$$
\int \frac{1}{\sqrt{a^{2} -x^{2}}} dx=\arcsin\frac{x}{a} +C
$$

$$
\int \cos xdx=\sin x+C
$$

其中 $C$ 是任意常数。

## 积分法

《高等数学》教程中只介绍了为数不多的，可以得到解析解的积分公式。解题过程中，往往利用已知公式，结合技巧，来找到解析解。下面介绍几个常用技巧



### 换元积分法

第一类换元法：把被积项 integrand 中部分移到 微分符号里面

$$
\int f( g( t)) g'( t) dt=\int f( g( t)) dg( t)
$$

第二类换元法：第一类换元法的逆过程

$$
\int f( x) dx=\int f( x( t)) x'( t) dt
$$



### 部分积分法

假设函数 $u(x),v(x)$ 和其微分都存在，则

$$
uv=uv'+u'v
$$

对两边积分，有

$$
uv=\int ( uv) 'dx=\int uv'dx+\int u'vdx
$$


交换顺序，得到部分积分公式

$$
\int uv'dx=\int udv=uv-\int vu'dx
$$



例如，另 $u=x,\ v'=e^{x}$, 那么

$$
\int xe^{x} dx=\int xde^{x} =xe^{x} -\int e^{x} dx
$$

另 $u=x^{2} ,\ v'=e^{x}$, 那么

$$
\int x^{2} e^{x} dx=\int x^{2} de^{x} =x^{2} e^{x} -\int e^{x} dx^{2} =x^{2} e^{x} -2\int xe^{x} dx
$$



### 有理函数积分技巧

形如 

$$
\int \frac{P( x)}{Q( x)} dx
$$

的有理函数，可以分成两步：

1. 把有理函数分解成分母为 $x$ 的一次，或者二次函数

2. 利用三角函数积分公式求解 分解后的积分问题



