

本文从最基本的能量守恒，和角动量守恒，来推导在中心力场（地球-太阳系统）下的行星运行轨迹（椭圆轨道，开普勒第一定律）。讨论将不局限于三维（各项同性）空间。将推广到二维，四维。

# 背景知识

## 能量守恒和角动量守恒

三维均匀各向同性空间（以下简称三位空间）中，把太阳看作一个质点的话，地日之间的万有引力随距离的平方衰减

$\displaystyle F=-\frac{GMm}{r^{2}}$

其中 $\displaystyle G$ 为引力常数，$\displaystyle M$ 是太阳质量，$\displaystyle m$ 是地球质量，$r$ 是地日距离

用矢量表示的话，

$\displaystyle m\ddot{\mathbf{r}} =\mathbf{F} =-\frac{GMm}{| \mathbf{r}| ^{3}}\mathbf{r}$

其中，粗体表示矢量，$\displaystyle \ddot{\mathbf{r}}$ 表示 位置矢量 对时间的二次微分，即加速度。

| 维度 | 引力                 | 引力势                                                       |
| ---- | -------------------- | ------------------------------------------------------------ |
| 2    | $-\frac{GMm}{r}$     | $-GMm\ln{r}+C$                                               |
| 3    | $-\frac{GMm}{r^{2}}$ | $\int _{r}^{\infty } -\frac{GMm}{r^{2}} dr=\left[\frac{GMm}{r}\right]_{r}^{\infty } =-\frac{2GMm}{r}$ |
| 4    | $-\frac{GMm}{r^{3}}$ | $\int _{r}^{\infty } -\frac{GMm}{r^{3}} dr=\left[\frac{2GMm}{r^{2}}\right]_{r}^{\infty } =-\frac{2GMm}{r^{2}}$ |

在不同维度的空间中，引力随距离的衰减快慢也不一样。这可以由 闭合曲面的引力通量为0来推导

$$ \oint _{\Gamma }\mathbf{g} d\mathbf{s} =0 $$

这也叫做 高斯重力定律 http://www.shuxueji.com/w/2221 

这个公式也能用拉格朗日方法，从中心引力势场中推导出来。详见 https://zhuanlan.zhihu.com/p/1953136636943634732。

$\displaystyle T-V=\frac{1}{2}\left( m\dot{r}^{2} +mr^{2}\dot{\theta }^{2}\right) +\frac{GMm}{r^{2}}$

第二是角动量守恒

$\displaystyle L=mr^{2} \omega =mr^{2}\dot{\theta }$

从这两点出发，既可以通过拉格朗日的方法推导，也可以通过牛顿第二定律推导。本文只介绍第二种方法。

## 极坐标系

在推导之前，先介绍直角坐标系和极坐标系。

中学主要学习直角坐标系，任意二维矢量可以在直角坐标系中分解

$\displaystyle \mathbf{r} =r_{x}\mathbf{e}_{x} +r_{y}\mathbf{e}_{y}$

其中 $\displaystyle \mathbf{e}_{x} ,\ \mathbf{e}_{y}$ 是单位向量

而在极坐标系中

$\displaystyle \mathbf{r} =r\mathbf{e}_{n} +0\mathbf{e}_{t}$

其中 $\displaystyle r$ 是 $\displaystyle \theta $ 的函数， $\displaystyle \theta $ 是 $\displaystyle t$ 的函数，即 $\displaystyle r( \theta ( t))$ 

但是我们最关心的是 $\displaystyle r( \theta )$，即行星轨迹。 时间将作为隐变量消去。

两套单位向量的转换关系是：

径向

$\displaystyle \mathbf{e}_{n} =\mathbf{e}_{x}\cos \theta +\mathbf{e}_{y}\sin \theta $

切向

$\displaystyle \mathbf{e}_{t} =-\mathbf{e}_{x}\sin \theta +\mathbf{e}_{y}\cos \theta $

若写成矩阵形式，可以看作从 $\displaystyle (\mathbf{e}_{x} ,\mathbf{e}_{y})$ 到 $\displaystyle (\mathbf{e}_{n} ,\mathbf{e}_{t})$ 的旋转变换。

单位极坐标的微分形式为：

对角度微分

$\displaystyle \frac{d}{d\theta }\mathbf{e}_{n} =-\mathbf{e}_{x}\sin \theta +\mathbf{e}_{y}\cos \theta =\mathbf{e}_{t}$

对角度微分

$\displaystyle \frac{d}{d\theta }\mathbf{e}_{t} =-\mathbf{e}_{x}\cos \theta -\mathbf{e}_{y}\sin \theta =-\mathbf{e}_{n}$

对时间微分

$\displaystyle \dot{\mathbf{e}}_{n} =\frac{d\theta }{dt}\frac{d}{d\theta }\mathbf{e}_{n} =\dot{\theta }\mathbf{e}_{t}$

对时间微分

$\displaystyle \dot{\mathbf{e}}_{t} =\frac{d\theta }{dt}\frac{d}{d\theta }\mathbf{e}_{t} =-\dot{\theta }\mathbf{e}_{n}$

这个微分公式将在后文用到。

# 行星轨道方程求解

## 3维空间行星轨道

我们把加速度公式

$\displaystyle \ddot{\mathbf{r}} =-\frac{GM}{|r|^{3}}\mathbf{r}$

表示成为对 $\displaystyle \theta $ 的微分：

一次微分

$\displaystyle \dot{\mathbf{r}} =\dot{r}\mathbf{e}_{n} +r\dot{\mathbf{e}}_{n} =\dot{r}\mathbf{e}_{n} +r\dot{\theta }\mathbf{e}_{t}$

二次微分

$\displaystyle \ddot{\mathbf{r}} =\ddot{r}\mathbf{e}_{n} +\dot{r}\dot{\theta }\mathbf{e}_{t} +(\dot{r}\dot{\theta } +r\ddot{\theta })\mathbf{e}_{t} -r\dot{\theta }^{2}\mathbf{e}_{n}$

代回加速度公式，即

$\displaystyle \ddot{r}\mathbf{e}_{n} +\dot{r}\dot{\theta }\mathbf{e}_{t} +(\dot{r}\dot{\theta } +r\ddot{\theta })\mathbf{e}_{t} -r\dot{\theta }^{2}\mathbf{e}_{n} =-\frac{GM}{r^{2}}\mathbf{e}_{n}$

因为 $\displaystyle \mathbf{e}_{n} ,\mathbf{e}_{t}$ 相互正交，所以得到两套等式：

径向

$\displaystyle \ddot{r} -r\dot{\theta }^{2} +\frac{GM}{r^{2}} =0$

切向

$\displaystyle 2\dot{r}\dot{\theta } +r\ddot{\theta } =0$

其中，第二套左右各乘以 $\displaystyle r$，即得到

$\displaystyle 2r\dot{r}\dot{\theta } +r^{2}\ddot{\theta } =\frac{d}{dt}\left( r^{2}\dot{\theta }\right) =0$

积分得到

$\displaystyle r^{2}\dot{\theta } =C_{1}$

这正是动量守恒公式

$\displaystyle \frac{L}{m} =r^{2}\dot{\theta } =C_{1}$

第二套等式积分这么简洁，正是因为恒星对行星的中心引力没有切向 $\mathbf{e}_{n}$ 的分量，所以也说明了，中心力场是角动量守恒的前提条件。

根据链式法则

$\displaystyle r=r( \theta ( t))$

一次微分

$\displaystyle \dot{r} =\frac{d}{dt} r( \theta ( t)) =\frac{dr}{d\theta }\frac{d\theta }{dt} =\frac{dr}{d\theta }\dot{\theta }$

回代动量守恒公式

$\displaystyle \dot{r} =\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}$

二次微分

$\displaystyle \ddot{r} =\frac{d}{dt}\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right) =\dot{\theta }\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right)$

继续回代动量守恒公式

$\displaystyle \ddot{r} =\frac{C_{1}}{r^{2}}\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right)$

代回第一套等式（加速度公式），即消去了 $\displaystyle t$, 得到对于 $\displaystyle \theta $ 的轨道微分方程

$\displaystyle \frac{C_{1}}{r^{2}}\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right) -r\left(\frac{C_{1}}{r^{2}}\right)^{2} +\frac{GM}{r^{2}} =0$

消去相同因式

$\displaystyle \frac{d}{d\theta }\left(\frac{1}{r^{2}}\frac{dr}{d\theta }\right) -\frac{1}{r} +\frac{GM}{C_{1}^{2}} =0$

## 第一种变量替换法

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

## 第二种变量替换法

定义

$\displaystyle x=1/r,\ r=1/x$

则有

$\displaystyle \frac{dr}{d\theta } =\frac{dx}{d\theta }\frac{dr}{dx} =-\frac{1}{x^{2}}\frac{dx}{d\theta }$

轨道微分方程变成

$\displaystyle \frac{d}{d\theta }\left(\frac{dx}{d\theta }\right) +x-\frac{GM}{C_{1}^{2}} =0$

这就是 比耐公式 https://wuli.wiki/online/Binet.html

得到通解

$\displaystyle \frac{1}{r} =x=C_{3}\cos \theta +C_{4}\sin \theta +\frac{GM}{C_{1}^{2}} =C_{6}\cos( \theta +\theta _{0}) +\frac{GMm^{2}}{L^{2}}$

这，即是开普勒辛辛苦苦花费8年，1609年才拼凑出来的椭圆轨道。而我们用1665年牛顿发明微积分，8分钟就求解出了椭圆轨道解。可见，物理人掌握先进的数学工具有多么重要。珍惜生命，学好数学。



掌握上述公式之后，接下来就是有趣的，分析不同维度行星轨道。

## 4维空间行星轨道

在4维空间，引力随距离的3次方衰减，加速度等式变成

$\displaystyle \ddot{\mathbf{r}} =-\frac{GMm}{| \mathbf{r}| ^{3}}\mathbf{r}$

可见，至少在 $\displaystyle GM$ 这一项中，变化了 $\displaystyle r$ 的指数。所以，我们跳过推导过程，直接得到轨道微分方程

$\displaystyle \frac{C_{1}}{r^{2}}\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right) -r\left(\frac{C_{1}}{r^{2}}\right)^{2} +\frac{GM}{r^{3}} =0$

消除相同因式

$\displaystyle \frac{d}{d\theta }\left(\frac{1}{r^{2}}\frac{dr}{d\theta }\right) -\frac{1}{r} +\frac{GM}{C_{1}^{2} r} =0$

作变量替换，得到

$\displaystyle \frac{d}{d\theta }\left(\frac{dx}{d\theta }\right) +\left( 1-\frac{GMm^{2}}{L^{2}}\right) x=0$

这是二元齐次常系数线性微分方程。

根据其特征根的正负号，作如下讨论

### 自由态

角动量大的时候

$\displaystyle 1-\frac{GMm^2}{L^{2}}  >0$ 

有通解

$\displaystyle \frac{1}{r} =x=C_{6}\cos\left(\sqrt{1-\frac{GMm^{2}}{L^{2}}} \theta +\theta _{0}\right)$

### 临界态

角动量刚好的时候

$\displaystyle 1-\frac{GMm^2}{L^{2}} =0$

有通解

$\displaystyle \frac{1}{r} =x=C_{7} +C_{8} \theta $

是一条螺旋线。当 $C_8>0$  行星旋出。当 $C_8<0$  行星旋进。当 $C_8=0$  行星是不稳定的圆形轨道。

如果旋进的话，行星会不会旋进到太阳呢？

对通解两侧对时间微分

$-\frac{1}{r^{2}}\dot{r} =C_{8}\dot{\theta }$

代入动量公式

$L=mr^{2}\dot{\theta }$

消去角度，得到

$-\frac{1}{r^{2}}\dot{r} =C_{8}\dot{\theta } =\frac{C_{8} L}{mr^{2}}$

消去相同因式，得到

$\dot{r} =-\frac{C_{8} L}{m}$

积分得到

$r( t) =R_0-\frac{C_{8} L}{m} t$

即行星会以恒定径向速度，坠入恒星（角速度越来越快），或者远离恒星。

### 束缚态

角动量小的时候

 $\displaystyle 1-\frac{GMm^2}{L^{2}} < 0$ 

有通解

$\displaystyle \frac{1}{r} =x=C_{7}\exp\left(\sqrt{\frac{GMm^{2}}{L^{2}} -1} \theta \right) +C_{8}\exp\left( -\sqrt{\frac{GMm^{2}}{L^{2}} -1} \theta \right)$

假设 $\theta(t)$ 单调递增。

当 $C_7C_8>0$ ，即同号 ，$r$ 有最大值。意味着，即使行星刚开始旋出，也会随后旋入，最终坠落到恒星。

当 $C_7 C_8<0$  ，$r$ 无最大值。意味着，即使行星旋出的话，将以渐近线的方式运动到无穷远。

当 $C_7C_8=0$  ，行星轨道退化成螺旋线

### 总结

| 分类   | 判定  | 3维轨道 | 判定        | 4维轨道      |
| ------ | ----- | ------- | ----------- | ------------ |
| 自由态 | $T>V$ | 双曲线  | $L^2>GMm^2$ | 可相交渐近线 |
| 临界态 | $T=V$ | 抛物线  | $L^2=GMm^2$ | 螺旋         |
| 束缚态 | $T<V$ | 椭圆    | $L^2<GMm^2$ | 螺旋         |

## 2维空间行星轨道

在2维空间，引力随距离的1次方衰减，加速度等式变成

$\displaystyle \ddot{\mathbf{r}} =-\frac{GMm}{| \mathbf{r}| }\mathbf{r}$

类似4维空间，我们直接得到2维空间的轨道微分方程

$\displaystyle \frac{C_{1}}{r^{2}}\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right) -r\left(\frac{C_{1}}{r^{2}}\right)^{2} +\frac{GM}{r} =0$

消去相同因式

$\displaystyle \frac{d}{d\theta }\left(\frac{1}{r^{2}}\frac{dr}{d\theta }\right) -\frac{1}{r} +\frac{GM}{C_{1}^{2}} r=0$

作类似变量替换，得到

$\displaystyle \frac{d}{d\theta }\left(\frac{dx}{d\theta }\right) +x-\frac{GM}{C_{1}^{2} x} =0$

这不是线性方程，没有解析解。但是知道其引力势场的方程为

$\displaystyle V=\int -\frac{GMm}{r} dr=-GMm\ln r$

在无穷远处为无穷大，所以知道，对于有限动能的行星，其轨道一定不会到无穷远。

# 软件工具

## 免费网页SymPy计算器

忘记怎么求解微分方程？这个好办。可以使用免费的 网页计算器 https://bubbleuniverse.github.io/symbolic/calculator

### 3维比耐方程

针对3维比耐方程

$$ \frac{d}{dx}\frac{d}{dx}f\left(x\right)+f\left(x\right)-\frac{GMm^2}{L^2} = 0 $$

在网页上

1. 粘贴下述 LaTeX 公式到输入框

```latex
 \frac{d}{dx}\frac{d}{dx}f\left(x\right)+f\left(x\right)-\frac{GMm^2}{L^2} 
```

2. 选择  ”求解微分方程 dsolve “
3. 点击“计算 Calculate” 按钮，即可得到通解

$$ f{\left(x \right)} = C_{1} \sin{\left(x \right)} + C_{2} \cos{\left(x \right)} + \frac{G M m^{2}}{L^{2}} $$

### 4维比耐方程

针对4维比耐方程

$$ \frac{d}{dx}\frac{d}{dx}f\left(x\right)+\left(1-\frac{GMm^2}{L^2}\right)f\left(x\right) = 0 $$ 

在网页上

1. 粘贴下述 LaTeX 公式到输入框

```latex
 \frac{d}{dx}\frac{d}{dx}f\left(x\right)+\left(1-\frac{GMm^2}{L^2}\right)f\left(x\right) 
```

2. 选择  ”求解微分方程 dsolve “
3. 点击“计算 Calculate” 按钮，即可得到通解

$$ f{\left(x \right)} = C_{1} e^{- \frac{x \sqrt{G M m^{2} - L^{2}}}{L}} + C_{2} e^{\frac{x \sqrt{G M m^{2} - L^{2}}}{L}} $$



## Desmos 作图

### 4维自由态

点击链接 https://www.desmos.com/calculator/bt0m6bwlcr 得到 下述公式，和行星轨道曲线

$\displaystyle r=\frac{1}{\cos (l\theta)} ,l\in ( 0,1), l\theta \in (-\frac{\pi}{2},\frac{\pi}{2})$

可见，动量大时，行星轨道是一条不闭合的曲线。从无穷远来，到无穷远去。

<div>
  <iframe src="https://www.desmos.com/calculator/bt0m6bwlcr?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>
</div>



### 4维临界态

点击链接 https://www.desmos.com/calculator/k7pgzyqo5a 得到 下述公式，和行星轨道曲线

$\displaystyle r=\frac{1}{\theta }$

可见，轨道是螺旋线

<iframe src="https://www.desmos.com/calculator/k7pgzyqo5a?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

物理解释：如果是旋进的话，行星最终会坠落到恒星上。

### 4维束缚态

点击链接 https://www.desmos.com/calculator/pdxfdpfehy 得到 下述公式，和行星轨道曲线

$\displaystyle r=\frac{1}{C_1\exp( l\theta ) +C_2\exp( -l\theta )}$

<iframe src="https://www.desmos.com/calculator/pdxfdpfehy?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

# 参考

https://zhuanlan.zhihu.com/p/1953136636943634732

https://zhuanlan.zhihu.com/p/136265256 

https://wuli.wiki/online/Binet.html

