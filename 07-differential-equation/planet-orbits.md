

本文从最基本的能量守恒，和角动量守恒，来推导在中心力场（地球-太阳系统）下的行星运行轨迹（椭圆轨道，开普勒第一定律）。讨论将不局限于三维（各项同性）空间。将推广到二维，四维。

# 背景知识

## 地日中心保守力场

### 受力分析

为了推导地球轨道，考虑地球的受力：

1. 星际尘埃的阻尼：产生和速度方向相反的切向受力分量
2. 太阳风和光压：仍然是中心力场，但是能量不守恒
3. 木星等其他星体的拉扯：角动量不守恒
3. 地球不是一个质点：受太阳潮汐力

但是因为距离较远，地球-太阳 可简化为 二体质点系统，并且假设能量守恒和角动量守恒。

地日系统的质量中心不是太阳中心，太阳也作回归运动。但是为了方便讨论，假设太阳被固定在坐标原点。读者读完本篇之后，可以把太阳回归运动也考虑进来，也能得到类似形式的解。

### 2，3，4维空间引力公式

三维均匀各向同性空间（以下简称三位空间）中，把太阳看作一个质点的话，地日之间的万有引力随距离的平方衰减

$$F=-\frac{GMm}{r^{2}}$$

其中 $G$ 为引力常数， $M$ 是太阳质量， $m$ 是地球质量， $r$ 是地日距离

用矢量表示的话，

$$m\ddot{\mathbf{r}} =\mathbf{F} =-\frac{GMm}{| \mathbf{r}| ^{3}}\mathbf{r}$$

其中，粗体表示矢量， $$\ddot{\mathbf{r}}$$ 表示 位置矢量 对时间的二次微分，即加速度。

| 维度 | 引力                 | 引力势                |
| ---- | -------------------- | --------------------- |
| 2    | $-\frac{GMm}{r}$     | $-GMm\ln{r}+C$        |
| 3    | $-\frac{GMm}{r^{2}}$ | $-\frac{GMm}{r}$      |
| 4    | $-\frac{GMm}{r^{3}}$ | $-\frac{GMm}{2r^{2}}$ |

在不同维度的空间中，引力随距离的衰减快慢也不一样。这可以由 无源闭合曲面的引力通量为0来推导

$$ \oint _{\Gamma }\mathbf{g} d\mathbf{s} =0 $$

这也叫做 高斯重力定律 http://www.shuxueji.com/w/2221 

这个公式也能用拉格朗日方法，从中心引力势场中推导出来。详见 https://zhuanlan.zhihu.com/p/1953136636943634732。

$$T-V=\frac{1}{2}\left( m\dot{r}^{2} +mr^{2}\dot{\theta }^{2}\right) +\frac{GMm}{r}$$

第二是角动量守恒

$$L=mr^{2} \omega =mr^{2}\dot{\theta }$$

从这两点出发，既可以通过拉格朗日的方法推导，也可以通过牛顿第二定律推导。本文只介绍第二种方法。

## 极坐标系

### 极坐标系转换

在推导之前，先介绍直角坐标系和极坐标系。

中学主要学习直角坐标系，任意二维矢量可以在直角坐标系中分解

$$\mathbf{r} =r_{x}\mathbf{e}_{x} +r_{y}\mathbf{e}_{y}$$

其中 $$\mathbf{e}_{x} ,\ \mathbf{e}_{y}$$ 是单位向量

而在极坐标系中

$$\mathbf{r} =r\mathbf{e}_{n} +0\mathbf{e}_{t}$$

其中 $r$ 是 $\theta $ 的函数， $\theta $ 是 $t$ 的函数，即 $r( \theta ( t))$ 

但是我们最关心的是 $r( \theta )$，即行星轨迹。 时间将作为隐变量消去。

两套单位向量的转换关系是：

径向

$$\mathbf{e}_{n} =\mathbf{e}_{x}\cos \theta +\mathbf{e}_{y}\sin \theta $$

切向

$$\mathbf{e}_{t} =-\mathbf{e}_{x}\sin \theta +\mathbf{e}_{y}\cos \theta $$

若写成矩阵形式，可以看作从 $$(\mathbf{e}_{x} ,\mathbf{e}_{y})$$ 到 $$(\mathbf{e}_{n} ,\mathbf{e}_{t})$$ 的旋转变换。

### 极坐标系微分

单位极坐标的微分形式为：

对角度微分

$$\frac{d}{d\theta }\mathbf{e}_{n} =-\mathbf{e}_{x}\sin \theta +\mathbf{e}_{y}\cos \theta =\mathbf{e}_{t}$$

对角度微分

$$\frac{d}{d\theta }\mathbf{e}_{t} =-\mathbf{e}_{x}\cos \theta -\mathbf{e}_{y}\sin \theta =-\mathbf{e}_{n}$$

对时间微分

$$\dot{\mathbf{e}}_{n} =\frac{d\theta }{dt}\frac{d}{d\theta }\mathbf{e}_{n} =\dot{\theta }\mathbf{e}_{t}$$

对时间微分

$$\dot{\mathbf{e}}_{t} =\frac{d\theta }{dt}\frac{d}{d\theta }\mathbf{e}_{t} =-\dot{\theta }\mathbf{e}_{n}$$

这个微分公式将在后文用到。

# 行星轨道方程求解

## 3维空间行星轨道

### 受力分解

我们把加速度公式

$$\ddot{\mathbf{r}} =-\frac{GM}{|r|^{3}}\mathbf{r}$$

表示成为对 $\theta $ 的微分：

一次微分

$$\dot{\mathbf{r}} =\dot{r}\mathbf{e}_{n} +r\dot{\mathbf{e}}_{n} =\dot{r}\mathbf{e}_{n} +r\dot{\theta }\mathbf{e}_{t}$$

二次微分

$$\ddot{\mathbf{r}} =\ddot{r}\mathbf{e}_{n} +\dot{r}\dot{\theta }\mathbf{e}_{t} +(\dot{r}\dot{\theta } +r\ddot{\theta })\mathbf{e}_{t} -r\dot{\theta }^{2}\mathbf{e}_{n}$$

代回加速度公式，即

$$\ddot{r}\mathbf{e}_{n} +\dot{r}\dot{\theta }\mathbf{e}_{t} +(\dot{r}\dot{\theta } +r\ddot{\theta })\mathbf{e}_{t} -r\dot{\theta }^{2}\mathbf{e}_{n} =-\frac{GM}{r^{2}}\mathbf{e}_{n}$$

因为 $$\mathbf{e}_{n} ,\mathbf{e}_{t}$$ 相互正交，所以得到两套等式：

径向

$$\ddot{r} -r\dot{\theta }^{2} +\frac{GM}{r^{2}} =0$$

切向

$$2\dot{r}\dot{\theta } +r\ddot{\theta } =0$$

### 角动量守恒

其中，第二套左右各乘以 $r$，即得到

$$2r\dot{r}\dot{\theta } +r^{2}\ddot{\theta } =\frac{d}{dt}\left( r^{2}\dot{\theta }\right) =0$$

积分得到

$$r^{2}\dot{\theta } =C_{1}$$

这正是动量守恒公式

$$\frac{L}{m} =r^{2}\dot{\theta } =C_{1}$$

第二套等式积分这么简洁，正是因为恒星对行星的中心引力没有切向 $$\mathbf{e}_{n}$$ 的分量，所以也说明了，中心力场是角动量守恒的前提条件。

### 径向加速度方程

根据链式法则

$$r=r( \theta ( t))$$

一次微分

$$\dot{r} =\frac{d}{dt} r( \theta ( t)) =\frac{dr}{d\theta }\frac{d\theta }{dt} =\frac{dr}{d\theta }\dot{\theta }$$

回代动量守恒公式

$$\dot{r} =\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}$$

二次微分

$$\ddot{r} =\frac{d}{dt}\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right) =\dot{\theta }\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right)$$

继续回代动量守恒公式

$$\ddot{r} =\frac{C_{1}}{r^{2}}\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right)$$

代回第一套等式（加速度公式），即消去了 $t$, 得到对于 $\theta $ 的轨道微分方程

$$\frac{C_{1}}{r^{2}}\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right) -r\left(\frac{C_{1}}{r^{2}}\right)^{2} +\frac{GM}{r^{2}} =0$$

消去相同因式

$$\frac{d}{d\theta }\left(\frac{1}{r^{2}}\frac{dr}{d\theta }\right) -\frac{1}{r} +\frac{GM}{C_{1}^{2}} =0$$

### 第一种变量替换法

再对 $\theta $ 作微分

$$\frac{d^{2}}{d\theta ^{2}}\left(\frac{1}{r^{2}}\frac{dr}{d\theta }\right) +\frac{1}{r^{2}}\frac{dr}{d\theta } =0$$

作变量替换

$$z=\frac{1}{r^{2}}\frac{dr}{d\theta }$$

即为求解

$$\frac{d^{2} z}{d\theta ^{2}} +z=0$$

这是个对于$z( \theta )$ 的二阶常系数齐次微分方程，有通解

$$z=C_{4}\cos \theta +C_{5}\sin \theta =C_{6}\cos( \theta +\theta _{0})$$

即为求解

$$\frac{1}{r^{2}}\frac{dr}{d\theta } =C_{6}\cos( \theta +\theta _{0})$$

用分离变量法

$$\frac{dr}{r^{2}} =C_{6}\cos( \theta +\theta _{0}) d\theta $$

对两边积分，得到

$$-\frac{1}{r} =C_{6}\sin( \theta +\theta _{0}) +C_{7}$$

### 第二种变量替换法

定义

$$u=1/r,\ r=1/u$$

则有

$$\frac{dr}{d\theta } =\frac{du}{d\theta }\frac{dr}{du} =-\frac{1}{u^{2}}\frac{du}{d\theta }$$

轨道微分方程变成

$$\frac{d}{d\theta }\left(\frac{du}{d\theta }\right) +u-\frac{GM}{C_{1}^{2}} =0$$

这就是 比耐 Binet 公式 https://wuli.wiki/online/Binet.html

这是 二阶非齐次常系数线性微分方程，有通解

$$\frac{1}{r} =u=C_{3}\cos \theta +C_{4}\sin \theta +\frac{GM}{C_{1}^{2}} = (e\cos (\theta +\theta _{0} )+1)\frac{GMm^{2}}{L^{2}}$$

其中 待定系数 $e$ 是偏心率。写成 倒数形式

$$ r=\frac{L^{2}}{GMm^{2}}\frac{1}{1+e\cos (\theta +\theta _{0} )} $$

即为标准的圆锥曲线方程。坐标原点是圆锥曲线的一个焦点。

这即是开普勒辛辛苦苦花费8年，1609年才拼凑出来的行星轨道。而我们用1665年牛顿发明微积分，8分钟就求解出了圆锥曲线轨道解。可见，物理人掌握先进的数学工具有多么重要。珍惜生命，学好数学。



掌握上述公式之后，接下来就是有趣的，分析不同维度行星轨道。

## 4维空间行星轨道

在4维空间，引力随距离的3次方衰减，加速度等式变成

$$\ddot{\mathbf{r}} =-\frac{GM}{| \mathbf{r}| ^{3}}\mathbf{r}$$

可见，只是在 $GM$ 外力这一项中，变化了 $r$ 的指数。所以，我们跳过推导过程，直接写出轨道微分方程

$$\frac{C_{1}}{r^{2}}\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right) -r\left(\frac{C_{1}}{r^{2}}\right)^{2} +\frac{GM}{r^{3}} =0$$

消除相同因式

$$\frac{d}{d\theta }\left(\frac{1}{r^{2}}\frac{dr}{d\theta }\right) -\frac{1}{r} +\frac{GM}{C_{1}^{2} r} =0$$

作 $u=1/r$ 变量替换，得到

$$\frac{d}{d\theta }\left(\frac{du}{d\theta }\right) +\left( 1-\frac{GMm^{2}}{L^{2}}\right) u=0$$

这是二元齐次常系数线性微分方程。

根据其特征根的正负号，作如下讨论

### 自由态

角动量大的时候

$$1-\frac{GMm^2}{L^{2}}  >0$$ 

有通解

$$\frac{1}{r} =u=C_{6}\cos\left(\sqrt{1-\frac{GMm^{2}}{L^{2}}} \theta +\theta _{0}\right)$$

### 临界态

角动量刚好的时候

$$1-\frac{GMm^2}{L^{2}} =0$$

有通解

$$\frac{1}{r} =u=C_{7} +C_{8} \theta $$

是一条螺旋线。当 $C_8>0$  行星旋出。当 $C_8<0$  行星旋进。当 $C_8=0$  行星是不稳定的圆形轨道。

如果旋进的话，行星会不会旋进到太阳呢？

对通解两侧对时间微分

$$-\frac{1}{r^{2}}\dot{r} =C_{8}\dot{\theta }$$

代入动量公式

$$L=mr^{2}\dot{\theta }$$

消去角度，得到

$$-\frac{1}{r^{2}}\dot{r} =C_{8}\dot{\theta } =\frac{C_{8} L}{mr^{2}}$$

消去相同因式，得到

$$\dot{r} =-\frac{C_{8} L}{m}$$

积分得到

$$r( t) =R_0-\frac{C_{8} L}{m} t$$

即行星会以恒定径向速度，坠入恒星（角速度越来越快），或者远离恒星。

### 束缚态

角动量小的时候

 $1-\frac{GMm^2}{L^{2}} < 0$ 

有通解

$$\frac{1}{r} =u=C_{7}\exp\left(\sqrt{\frac{GMm^{2}}{L^{2}} -1} \theta \right) +C_{8}\exp\left( -\sqrt{\frac{GMm^{2}}{L^{2}} -1} \theta \right)$$

假设 $\theta(t)$ 单调递增。

当 $C_7C_8>0$ ，即同号 ， $r$ 有最大值。意味着，即使行星刚开始旋出，也会随后旋入，最终坠落到恒星。

当 $C_7 C_8<0$  ， $r$ 无最大值。意味着，即使行星旋出的话，将以渐近线的方式运动到无穷远。

当 $C_7C_8=0$  ，行星轨道退化成螺旋线

### 总结

| 分类   | 判定  | 3维轨道 | 判定        | 4维轨道            |
| ------ | ----- | ------- | ----------- | ------------------ |
| 自由态 | $T>V$ | 双曲线  | $L^2>GMm^2$ | 可相交渐近线       |
| 临界态 | $T=V$ | 抛物线  | $L^2=GMm^2$ | 螺旋线             |
| 束缚态 | $T<V$ | 椭圆    | $L^2<GMm^2$ | 首尾在原点的螺旋线 |

## 2维空间行星轨道

在2维空间，引力随距离的1次方衰减，加速度等式变成

$$\ddot{\mathbf{r}} =-\frac{GM}{| \mathbf{r}| }\mathbf{r}$$

类似4维空间，我们直接得到2维空间的轨道微分方程

$$\frac{C_{1}}{r^{2}}\frac{d}{d\theta }\left(\frac{dr}{d\theta }\frac{C_{1}}{r^{2}}\right) -r\left(\frac{C_{1}}{r^{2}}\right)^{2} +\frac{GM}{r} =0$$

消去相同因式

$$\frac{d}{d\theta }\left(\frac{1}{r^{2}}\frac{dr}{d\theta }\right) -\frac{1}{r} +\frac{GM}{C_{1}^{2}} r=0$$

作 $u=1/r$ 变量替换，得到

$$\frac{d}{d\theta }\left(\frac{du}{d\theta }\right) +u-\frac{GM}{C_{1}^{2} u} =0$$

这不是线性方程，没有解析解。但是知道其引力势场的方程为

$$V=\int -\frac{GMm}{r} dr=-GMm\ln r$$

在无穷远处为无穷大，所以知道，对于有限动能的行星，其轨道一定不会到无穷远。

## 智慧生命诞生的可能

可以从上述分析看出来：

- 4维宇宙：相当不稳定，行星要么坠落到恒星，要么飞到无穷远。难以产生智慧生命进化的稳定环境。
- 2维宇宙：宇宙不会永远膨胀下去。恒星行星会因为彼此引力的束缚，而约束在有限距离内。甚至连光，都无法穿过整个宇宙。
- 3维宇宙：束缚态的行星能够稳定地环绕恒星，有充足的时间，是智慧生命进化的完美家园。

这也从人择原理解释了，为什么弦理论预言了9维空间，但是宇宙对我们隐藏了额外的6个维度。

当然，也可以乐观地考虑，虽然4维空间中，二体运动很难有稳定轨道。但是复杂的三体或者多体运动，或许能给4维空间增色。即，在极小的概率下，三颗自由态的星体靠近，其中一颗窃取系统的总动能，被弹射出去，剩下两颗刚好处于临界状态，说不定也能维持相当长时间的圆周运动，给智慧生命进化创造稳定的环境。

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

$$r=\frac{1}{\cos (l\theta)} ,l\in ( 0,1), l\theta \in (-\frac{\pi}{2},\frac{\pi}{2})$$

可见，动量大时，行星轨道是一条不闭合的曲线。从无穷远来，到无穷远去。

<div>
  <iframe src="https://www.desmos.com/calculator/bt0m6bwlcr?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>
</div>



### 4维临界态

点击链接 https://www.desmos.com/calculator/k7pgzyqo5a 得到 下述公式，和行星轨道曲线

$$r=\frac{1}{\theta }$$

可见，轨道是螺旋线

<iframe src="https://www.desmos.com/calculator/k7pgzyqo5a?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

物理解释：如果是旋进的话，行星最终会坠落到恒星上。

### 4维束缚态

点击链接 https://www.desmos.com/calculator/pdxfdpfehy 得到 下述公式，和行星轨道曲线

$$r=\frac{1}{C_1\exp( l\theta ) +C_2\exp( -l\theta )}$$

<iframe src="https://www.desmos.com/calculator/pdxfdpfehy?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

# 参考

https://www.bilibili.com/video/BV1aL4y1678A

https://zhuanlan.zhihu.com/p/1953136636943634732

https://zhuanlan.zhihu.com/p/136265256 

https://wuli.wiki/online/Binet.html

