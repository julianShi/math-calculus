# 微积分应用

利用例题，体验微积分的用处。

- 求解面积
- 转动惯量

## 面积计算

例1：求解椭圆面积。已知椭圆有直角坐标表示

$\frac{x^{2}}{a^{2}} +\frac{y^{2}}{b^{2}} =1$

或者

$y=\pm b\sqrt{1-\frac{x^{2}}{a^{2}}}$

用来求积分

$S=4\int _{0}^{a} |y|dx=4\int _{0}^{a} b\sqrt{1-\frac{x^{2}}{a^{2}}} dx$

得到面积

$S=\frac{4b}{a}\int _{0}^{a}\sqrt{a^{2} -x^{2}} dx=\pi ab$

例2：计算心形线

$\rho=a(1+\cos\theta)$

围成的面积

已知 $d\theta$ 扫过的面积微元是扇形

$dS=\frac{1}{2}\rho^2d\theta$

则面积是

$\displaystyle S=\int _{0}^{2\pi }\frac{1}{2} \rho ^{2} d\theta =\frac{a^{2}}{2}\int _{0}^{2\pi }( 1+\cos \theta )^{2} d\theta $

Cont.

$\displaystyle S=\frac{a^{2}}{4}\int _{0}^{2\pi }( 3+4\cos \theta +\cos 2\theta ) d\theta =\frac{3\pi a^{2}}{2}$

## 转动惯量

距离中心 $r$  的微元 $dm$ 的转动惯量是

$dl=r^2dm$

则转笔的时候，长度为 $l$, 线密度为常数 $\sigma$ 的笔的转动惯量是

$L=\int _{-l/2}^{l/2} r^{2} \sigma dr$

解为

$L=\sigma \left[\frac{r^{3}}{3}\right]_{-l/2}^{l/2} =\frac{\sigma l^{3}}{12}$

转半径为R，面密度为常数 $\sigma$ 的圆盘的时候，转动惯量公式为

$L=\int _{0}^{2\pi }\int _{0}^{R} r^{2} \sigma dS$

其中，极坐标下面积微元为

$dS=rdrd\theta$

所以解为

$L=\int _{0}^{2\pi }\int _{0}^{R} r^{2} \sigma rdrd\theta =\sigma \int _{0}^{2\pi } d\theta \int _{0}^{R} r^{3} dr=\frac{\pi \sigma R^{4}}{2}$



