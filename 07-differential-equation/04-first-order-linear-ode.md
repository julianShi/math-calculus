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
y=C\exp\left( -\int p(x)dx\right)
$$
请读者自行验证。

### 非齐次方程的解

我们希望，通过变量分离的方式，简化非齐次方程。我们尝试重写非齐次方程左侧，为 $(\mu(x)y)'$ 形式

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
建议读者尝试自己重复一遍推导过程，而不是死记硬背“常数变易法”。

