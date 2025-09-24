

本文从最基本的能量守恒，和角动量守恒，来推导在中心力场（地球-太阳系统）下的行星运行轨迹（椭圆轨道，开普勒第一定律）。讨论将不局限于三维（各项同性）空间。将推广到二维，四维。

https://zhuanlan.zhihu.com/p/1953136636943634732

https://zhuanlan.zhihu.com/p/136265256 

## 3维行星椭圆轨道推导

### 能量守恒和角动量守恒

三维均匀各向同性空间（以下简称三位空间）中，把太阳看作一个质点的话，地日之间的万有引力随距离的平方衰减

$\displaystyle F=-\frac{GMm}{r^{2}}$

其中 $\displaystyle G$ 为引力常数，$\displaystyle M$ 是太阳质量，$\displaystyle m$ 是地球质量

用矢量表示的话，

$\displaystyle m\ddot{\mathbf{r}} =\mathbf{F} =-\frac{GMm}{| \mathbf{r}| ^{3}}\mathbf{r}$

其中，粗体表示矢量，$\displaystyle \ddot{\mathbf{r}}$ 表示 位置矢量 对时间的二次微分，即加速度。

这个公式也能用拉格朗日方法，从中心引力势场中推导出来。详见https://zhuanlan.zhihu.com/p/1953136636943634732。

$\displaystyle T-V=\frac{1}{2}\left( m\dot{r}^{2} +mr^{2}\dot{\theta }^{2}\right) +\frac{GMm}{r^{2}}$

第二是角动量守恒

$\displaystyle L=mr^{2} \omega =mr^{2}\dot{\theta }$

从这两点出发，既可以通过拉格朗日的方法推导，也可以通过牛顿第二定律推导。本文只介绍第二种方法。

在推导之前，先介绍直角坐标系和极坐标系。

中学主要学习直角坐标系，任意二维矢量可以在直角坐标系中分解

$\displaystyle \mathbf{r} =r_{x}\mathbf{e}_{x} +r_{y}\mathbf{e}_{y}$

其中 $\displaystyle \mathbf{e}_{x} ,\ \mathbf{e}_{y}$ 是单位向量

而在极坐标系中

$\displaystyle \mathbf{r} =r\mathbf{e}_{n} +0\mathbf{e}_{t}$

其中 $\displaystyle r$ 是 $\displaystyle \theta $ 的函数， $\displaystyle \theta $ 是 $\displaystyle t$ 的函数，即 $\displaystyle r( \theta ( t))$ 

但是我们最关心的是 $\displaystyle r( \theta )$，即行星轨迹。 时间将作为隐变量消去。

两套单位向量的转换关系是

$\displaystyle \mathbf{e}_{n} =\mathbf{e}_{x}\cos \theta +\mathbf{e}_{y}\sin \theta $

,

$\displaystyle \mathbf{e}_{t} =-\mathbf{e}_{x}\sin \theta +\mathbf{e}_{y}\cos \theta $

若写成矩阵形式，可以看作从 $\displaystyle (\mathbf{e}_{x} ,\mathbf{e}_{y})$ 到 $\displaystyle (\mathbf{e}_{n} ,\mathbf{e}_{t})$ 的旋转变换。

单位极坐标的微分形式为

$\displaystyle \frac{d}{d\theta }\mathbf{e}_{n} =-\mathbf{e}_{x}\sin \theta +\mathbf{e}_{y}\cos \theta =\mathbf{e}_{t}$

,

$\displaystyle \frac{d}{d\theta }\mathbf{e}_{t} =-\mathbf{e}_{x}\cos \theta -\mathbf{e}_{y}\sin \theta =-\mathbf{e}_{n}$

,

$\displaystyle \dot{\mathbf{e}}_{n} =\frac{d\theta }{dt}\frac{d}{d\theta }\mathbf{e}_{n} =\dot{\theta }\mathbf{e}_{t}$

,

$\displaystyle \dot{\mathbf{e}}_{t} =\frac{d\theta }{dt}\frac{d}{d\theta }\mathbf{e}_{t} =-\dot{\theta }\mathbf{e}_{n}$

这个微分公式将在后文用到。



我们把加速度公式

$\displaystyle \ddot{\mathbf{r}} =-\frac{GM}{|r|^{3}}\mathbf{r}$

表示成为对 $\displaystyle \theta $ 的微分

$\displaystyle \dot{\mathbf{r}} =\dot{r}\mathbf{e}_{n} +r\dot{\mathbf{e}}_{n} =\dot{r}\mathbf{e}_{n} +r\dot{\theta }\mathbf{e}_{t}$

,

$\displaystyle \ddot{\mathbf{r}} =\ddot{r}\mathbf{e}_{n} +\dot{r}\dot{\theta }\mathbf{e}_{t} +(\dot{r}\dot{\theta } +r\ddot{\theta })\mathbf{e}_{t} -r\dot{\theta }^{2}\mathbf{e}_{n}$

代回加速度公式，即

$\displaystyle \ddot{r}\mathbf{e}_{n} +\dot{r}\dot{\theta }\mathbf{e}_{t} +(\dot{r}\dot{\theta } +r\ddot{\theta })\mathbf{e}_{t} -r\dot{\theta }^{2}\mathbf{e}_{n} =-\frac{GM}{r^{2}}\mathbf{e}_{n}$

因为 $\displaystyle \mathbf{e}_{n} ,\mathbf{e}_{t}$ 相互正交，所以得到两套等式

$\displaystyle \ddot{r} -r\dot{\theta }^{2} +\frac{GM}{r^{2}} =0$

,

$\displaystyle 2\dot{r}\dot{\theta } +r\ddot{\theta } =0$

其中，第二套左右各乘以 $\displaystyle r$，即得到

$\displaystyle 2r\dot{r}\dot{\theta } +r^{2}\ddot{\theta } =\frac{d}{dt}\left( r^{2}\dot{\theta }\right) =0$

积分得到

$\displaystyle r^{2}\dot{\theta } =C_{1}$

这正是动量守恒公式

$\displaystyle \frac{L}{m} =r^{2}\dot{\theta } =C_{1}$



根据链式法则

$\displaystyle r=r( \theta ( t))$

,

$\displaystyle \dot{r} =\frac{d}{dt} r( \theta ( t)) =\frac{dr}{d\theta }\frac{d\theta }{dt} =\frac{dr}{d\theta }\dot{\theta }$

回代动量守恒公式

$\displaystyle \dot{r} =\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}$

,

$\displaystyle \ddot{r} =\frac{d}{dt}\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right) =\dot{\theta }\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right)$

继续回代动量守恒公式

$\displaystyle \ddot{r} =\frac{C_{1}}{r^{2}}\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right)$

代回第一套等式（加速度公式），即消去了 $\displaystyle t$, 得到对于 $\displaystyle \theta $ 的轨道微分方程

$\displaystyle \frac{C_{1}}{r^{2}}\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right) -r\left(\frac{C_{1}}{r^{2}}\right)^{2} +\frac{GM}{r^{2}} =0$

,

$\displaystyle \frac{d}{d\theta }\left(\frac{1}{r^{2}}\frac{dr}{d\theta }\right) -\frac{1}{r} +\frac{GM}{C_{1}^{2}} =0$

### 第一种变量替换法

再对 $\displaystyle \theta $ 作微分

$\displaystyle \frac{d^{2}}{d\theta ^{2}}\left(\frac{1}{r^{2}}\frac{dr}{d\theta }\right) +\frac{1}{r^{2}}\frac{dr}{d\theta } =0$

作变量替换

$\displaystyle z=\frac{1}{r^{2}}\frac{dr}{d\theta }$

即为求解

$\displaystyle \frac{d^{2} z}{d\theta ^{2}} +z=0$

这是个对于$\displaystyle z( \theta )$ 的二阶常系数齐次微分方程，有通解

$\displaystyle z=C_{4}\cos \theta +C_{5}\sin \theta =C_{6}\cos( \theta +\theta _{0})$

即为求解

$\displaystyle \frac{1}{r^{2}}\frac{dr}{d\theta } =C_{6}\cos( \theta +\theta _{0})$

用分离变量法

$\displaystyle \frac{dr}{r^{2}} =C_{6}\cos( \theta +\theta _{0}) d\theta $

对两边积分，得到

$\displaystyle -\frac{1}{r} =C_{6}\sin( \theta +\theta _{0}) +C_{7}$

### 第二种变量替换法

定义

$\displaystyle x=1/r,\ r=1/x$

则有

$\displaystyle \frac{dr}{d\theta } =\frac{dx}{d\theta }\frac{dr}{dx} =-\frac{1}{x^{2}}\frac{dx}{d\theta }$

轨道微分方程变成

$\displaystyle \frac{d}{d\theta }\left(\frac{dx}{d\theta }\right) +x-\frac{GM}{C_{1}^{2}} =0$

得到通解

$\displaystyle \frac{1}{r} =x=C_{3}\cos \theta +C_{4}\sin \theta +\frac{GM}{C_{1}^{2}} =C_{6}\cos( \theta +\theta _{0}) +\frac{GMm^{2}}{L^{2}}$

即是开普勒辛辛苦苦花费8年，1609年才拼凑出来的椭圆轨道。而我们用1665年牛顿发明微积分，8分钟就求解出了椭圆轨道解。可见，物理人掌握先进的数学工具有多么重要。珍惜生命，学好数学。



掌握上述公式之后，接下来就是有趣的，分析不同维度行星轨道。

### 4维空间行星轨道

在4维空间，引力随距离的3次方衰减，加速度等式变成

$\displaystyle \ddot{\mathbf{r}} =-\frac{GMm}{| \mathbf{r}| ^{3}}\mathbf{r}$

可见，至少在 $\displaystyle GM$ 这一项中，变化了 $\displaystyle r$ 的指数。所以，我们跳过推导过程，直接得到轨道微分方程

$\displaystyle \frac{C_{1}}{r^{2}}\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right) -r\left(\frac{C_{1}}{r^{2}}\right)^{2} +\frac{GM}{r^{3}} =0$

,

$\displaystyle \frac{d}{d\theta }\left(\frac{1}{r^{2}}\frac{dr}{d\theta }\right) -\frac{1}{r} +\frac{GM}{C_{1}^{2} r} =0$

作变量替换，得到

$\displaystyle \frac{d}{d\theta }\left(\frac{dx}{d\theta }\right) +\left( 1-\frac{GMm^{2}}{L^{2}}\right) x=0$

这是二元齐次常系数线性微分方程。

当$\displaystyle 1-\frac{GMm^2}{L^{2}}  >0$ ，即角动量非常大

有通解

$\displaystyle \frac{1}{r} =x=C_{6}\cos\left(\sqrt{1-\frac{GMm^{2}}{L^{2}}} \theta +\theta _{0}\right)$

当$\displaystyle 1-\frac{GMm^2}{L^{2}} =0$

有通解

$\displaystyle \frac{1}{r} =x=C_{7} +C_{8} \theta $

是一条螺旋线

当 $\displaystyle 1-\frac{GMm^2}{L^{2}} < 0$ ，即角动量非常小

有通解

$\displaystyle \frac{1}{r} =x=C_{7}\exp\left(\sqrt{\frac{GMm^{2}}{L^{2}} -1} \theta \right) +C_{8}\exp\left( -\sqrt{\frac{GMm^{2}}{L^{2}} -1} \theta \right)$

总结而言

| 分类   | 判定  | 3维轨道 | 判定        | 4维轨道      |
| ------ | ----- | ------- | ----------- | ------------ |
| 束缚态 | $T<V$ | 椭圆    | $L^2<GMm^2$ | 螺旋         |
| 临界态 | $T=V$ | 抛物线  | $L^2=GMm^2$ | 螺旋         |
| 自由态 | $T>V$ | 双曲线  | $L^2>GMm^2$ | 可相交渐近线 |



### Desmos 作图

在 https://www.desmos.com/calculator 中输入下述公式

$\displaystyle r=\frac{1}{\cos (l\theta +a)} ,l\in ( 0,1)$

可见，动量大时，行星轨道是一条不闭合的曲线。从无穷远来，到无穷远去。



在 https://www.desmos.com/calculator 中输入下述公式

$\displaystyle r=\frac{1}{1+a\theta }$

可见，轨道是螺旋线



在 https://www.desmos.com/calculator 中输入下述公式

$\displaystyle r=\frac{1}{\exp( l\theta ) +a\exp( -l\theta )}$



轨道是一种特殊的螺旋线

### 2维空间行星轨道

在2维空间，引力随距离的1次方衰减，加速度等式变成

$\displaystyle \ddot{\mathbf{r}} =-\frac{GMm}{| \mathbf{r}| }\mathbf{r}$

类似4维空间，我们直接得到2维空间的轨道微分方程

$\displaystyle \frac{C_{1}}{r^{2}}\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right) -r\left(\frac{C_{1}}{r^{2}}\right)^{2} +\frac{GM}{r} =0$

,

$\displaystyle \frac{d}{d\theta }\left(\frac{1}{r^{2}}\frac{dr}{d\theta }\right) -\frac{1}{r} +\frac{GM}{C_{1}^{2}} r=0$

作变量替换，得到

$\displaystyle \frac{d}{d\theta }\left(\frac{dx}{d\theta }\right) +x-\frac{GM}{C_{1}^{2} x} =0$

这不是线性方程，没有解析解。但是知道其引力势场的方程为

$\displaystyle V=\int -\frac{GMm}{r} dr=-GMm\ln r$

在无穷远处为无穷大，所以知道，对于有限动能的行星，其轨道一定不会到无穷远。

