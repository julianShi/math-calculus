形如

$$
y'+p(x)y=q(x)
$$

叫做一阶线性常微分方程。其中

* $q(x)=0$ 叫做齐次方程
* $q(x)\neq 0$ 叫做非齐次方程

### 齐次方程的解

齐次方程的解是

$$
y=C e^{-\int p dx}
$$

请读者把解代回到方程中，自行验证。

### 非齐次方程的解

《高等数学》教材中介绍了“常数变易法”。但是“常数变易法”有局限，就是1.靠猜测，2.有可能遗漏。所以，我们希望，找到一种方法，能够严格不遗漏地找出所有解。

我们尝试重写非齐次方程左侧，为 $(\mu(x)y)'$ 形式

已知

$$
(\mu y)'=\mu'y+\mu y'
$$

其中，为了简化，省略了 $(x)$ 

则可以看到，微分方程有望写成如下形式

$$
y'+\frac{\mu '}{\mu } y= \frac{( \mu y) '}{\mu }= q
$$

只要

$$
\displaystyle \mu'/\mu=p
$$

即

$$
\mu= C_1 e^{\int p dx}
$$

。既然能把一阶项和零阶项写到一起，那么

$$
( \mu y) ' = q \mu
$$

变成

$$
(e^{\int p dx} y)' = q e^{\int p dx}
$$

。左右积分得到

$$
e^{\int p dx} y = \int q e^{\int p dx} dx + C_2
$$

即

$$
y = e^{-\int p dx} \left( \int q e^{\int p dx} dx + C_2 \right)
$$

读者可以尝试重复一遍推导过程，加深体验。

### 通解特解

我们注意到，上式可以展开成
$$
y = e^{-\int p dx} \int q e^{\int p dx} dx + C_2  e^{-\int p dx}
$$
其中，加号左侧叫做**特解** particular solution，加号右侧是其次方程的**通解** general solution。这个叠加性还可以推广到高阶齐次方程。

### 伯努利方程

形如如下，类似于一阶线性微分方程，但是多了 $y^n$ 项的，叫做伯努利方程。因为有解析解，所以拿出来当作练习

$\displaystyle \frac{dy}{dx} +P( x) y=Q( x) y^{n}$

通过如下变量替换，

$\displaystyle z=y^{1-n}$

可将原方程转换成一阶线性方程形式，进而套公式求解。

$\displaystyle \frac{1}{1-n}\frac{dz}{dx} +P( x) z=Q( x)$

请读者自行推导，当作练习。不是考点。
