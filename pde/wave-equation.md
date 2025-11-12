# 波动方程

波动方程是3种经典的椭圆偏微分方程（PDE）的一种，在特殊情况下有解析解。学习波动方程求解，有助于读者掌握椭圆微分方程。这也是《电磁学》的数学基础。

目录

1. 求解一维齐次波动方程
2. 达朗贝尔解法
3. 初值问题
4. 求解三维齐次球对称波动方程

## 一维波动方程

一维线性的弦的波动 $u(x,t)$ 由如下偏微分方程描述

$\displaystyle u_{tt} -a^{2} u_{xx} =f( x,t)$

其中 $f( x,t)$ 是外力导致的横向加速度。

当  $f( x,t)=0$ ， 则得到齐次PDE

## 达朗贝尔 d'Alembert 解法

对于一维波动的完整描述，是动力学方程和初值条件，边值条件

$\displaystyle t=0:u=\varphi ( x) ,\frac{\partial u}{\partial t} =\psi ( x)$

做变量替换。这个变量替换不是随便选取的，而是能让二阶PDE能化成对角形式的二次型的线性变换。

$\displaystyle \xi =x-at,\eta =x+at$

然后根据链式法则，做微分项的替换

$\displaystyle \frac{\partial }{\partial t} =\frac{\partial \xi }{\partial t}\frac{\partial }{\partial \xi } +\frac{\partial \eta }{\partial t}\frac{\partial }{\partial \eta } =-a\frac{\partial }{\partial \xi } +a\frac{\partial }{\partial \eta }$

继续得到二阶偏导数算子的转换

$\displaystyle \frac{\partial ^{2}}{\partial t^{2}} =\left( -a\frac{\partial }{\partial \xi } +a\frac{\partial }{\partial \eta }\right)^{2}$

同理根据链式法则，做对 $x$  偏导数的替换

$\displaystyle \frac{\partial }{\partial x} =\frac{\partial \xi }{\partial x}\frac{\partial }{\partial \xi } +\frac{\partial \eta }{\partial x}\frac{\partial }{\partial \eta } =\frac{\partial }{\partial \xi } +\frac{\partial }{\partial \eta }$

继续得到二阶偏导数算子的转换

$\displaystyle \frac{\partial ^{2}}{\partial x^{2}} =\left(\frac{\partial }{\partial \xi } +\frac{\partial }{\partial \eta }\right)^{2}$

这个时候，原方程可以简化为

$\displaystyle u_{tt} -a^{2} u_{xx} =a^{2}\left( -\frac{\partial }{\partial \xi } +\frac{\partial }{\partial \eta }\right)^{2} -a^{2}\left(\frac{\partial }{\partial \xi } +\frac{\partial }{\partial \eta }\right)^{2} =-4a^{2}\frac{\partial ^{2}}{\partial \xi \partial \eta } u=f( x,t)$

当 $f( x,t)=0$ 的时候，

$\displaystyle \frac{\partial ^{2} u}{\partial \xi \partial \eta } =0$

重积分得到

$\displaystyle u=g( \xi ) +h( \eta )$

以及非齐次方程的一个特解

$\displaystyle u^{*} =\frac{-1}{4a^{2}}\int \int f( \xi ,\eta ) d\xi d\eta $

所以通解是

$u=g( \xi ) +h( \eta ) -\frac{1}{4a^{2}}\int \int f( \xi ,\eta ) d\xi d\eta $

**解的物理意义**

现在反过头来看，变量替换

$\displaystyle \xi =x-at,\eta =x+at$

表示的是，如果盯着

$x=at, x=-at$

看，波形没有发生变化。也可以认为，波峰在以速度 $a$ 向左或者向右行进。

## 初值问题

解自由运动对应的齐次波动方程，得到通解

$u(x,t)=g( x-at ) +h( x+at )$

现在将初始条件代入第一个初始条件

$u( x,0) =g( x) +h( x) =\varphi ( x)$

和第二个初始条件（初始速度条件）

$u_t( x,0) =-ag'( x) +ah'( x) =\psi ( x)$

对第二个初始条件积分

$-ag( x) +ah( x) =\int_{x_0}^x \psi ( s) ds+C_1$

代回第一个初始条件，解这个线性方程组得到

$g( x) =\frac{1}{2} \varphi ( x) -\frac{1}{2a}\int_{x_0}^x \psi ( s) ds-\frac{1}{2} C_{1}$

和

$h( x) =\frac{1}{2} \varphi ( x) +\frac{1}{2a}\int_{x_0}^x \psi ( s) ds+\frac{1}{2} C_{1}$

做变量替换，得到

$u( x,t) =\frac{1}{2} \varphi ( x-at) +\frac{1}{2} \varphi ( x+at) +\frac{1}{2a}\int _{x-at}^{x+at} \psi ( s) ds$

**Mathematica 代码**

例1：无外力

```mathematica
(* Define the wave equation *)
waveEquation = D[u[x, t], {t, 2}] == c ^ 2 * D[u[x, t], {x, 2}];
(* Solve the wave equation *)
generalSolution = DSolve[waveEquation, u[x, t], {x, t}]

(*Initial conditions*)
ic1=(u[x, t]/.t->0)==Sin[Pi*x];
ic2=(D[u[x, t],t]/.t->0)==0;
(*Boundary conditions*)
ic3=(u[x, t]/.x->0)==0;
ic4=(u[x, t]/.x->1)==0;

generalSolution2 = DSolve[{waveEquation,ic1,ic2,ic3,ic4},u[x,t],{x,t}]
(*
{{u[x,t]->Cos[c \[Pi] t] Sin[\[Pi] x]}}
*)
```

$u(x,t)=\cos(\pi c t) \sin(\pi x)$

例2: 周期外力

$f(x,t)=\sin(\pi x)\sin(\pi t)$

```mathematica
(* Define the wave equation with external periodic force*)
waveEquation2 = D[u[x, t], {t, 2}] -  D[u[x, t], {x, 2}] == Sin[Pi*x]*Sin[Pi*t];
(*Initial condition*)
ic21=(u[x, t]/.t->0)==0;

(* Solve the wave equation *)
solution2 = DSolve[{waveEquation2,ic21,ic2,ic3,ic4}, u[x, t], {x, t}]
```

$u(x,t)=\frac{\sin (\pi x)(\sin (\pi t)-\pi t\cos (\pi t))}{2\pi ^{2}}$

可见，因为共振，振幅会越来越大。

https://www.wolframcloud.com/obj/yulinshiapp/Published/pde-wave-equation.nb

## 三维球对称波动方程

求解三维齐次波动方程中的一种特殊情况，即球对称情况

$ \frac{\partial ^{2}}{\partial t^{2}} u = a^2\nabla^2 u$

参考 [laplace-operator.md](../09-multivariable-calculus/laplace-operator.md)，已知在球坐标中，拉普拉斯算子

$\nabla^2=\frac{\partial ^{2}}{\partial r^{2}} +\frac{2}{r}\frac{\partial }{\partial r} +\frac{1}{r^{2}}\left(\frac{\partial ^{2}}{\partial \theta ^{2}} -\tan \theta \frac{\partial }{\partial \theta } +\sec^{2} \theta \frac{\partial ^{2}}{\partial \phi ^{2}}\right)$

因为球对称的假设，所以对 $\theta, \phi$ 的偏导数都为 0

$\nabla^2=\frac{\partial ^{2}}{\partial r^{2}} +\frac{2}{r}\frac{\partial }{\partial r}$ 

这个时候，形如

$ \frac{\partial ^{2}}{\partial t^{2}} u=a^{2}\left(\frac{\partial ^{2}}{\partial r^{2}} +\frac{2}{r}\frac{\partial }{\partial r}\right) u$

的波动方程仍然难以求解。但是可以作如下变量替换

$\displaystyle v=ru$

那么

$u=\frac{v}{r}$

一阶偏导

$\displaystyle \frac{\partial }{\partial r}\frac{v}{r} =\left(\frac{1}{r}\frac{\partial }{\partial r} -\frac{1}{r^{2}}\right) v$

二阶偏导

$\displaystyle \frac{\partial ^{2}}{\partial r^{2}}\frac{v}{r} =\frac{\partial }{\partial r}\left(\frac{1}{r}\frac{\partial }{\partial r} -\frac{1}{r^{2}}\right) v=\left( -\frac{1}{r^{2}}\frac{\partial }{\partial r} +\frac{1}{r}\frac{\partial ^{2}}{\partial r^{2}} +\frac{2}{r^{3}} -\frac{1}{r^{2}}\frac{\partial }{\partial r}\right) v$

代回原波动方程，得到

$\displaystyle \frac{\partial ^{2}}{\partial t^{2}}\frac{v}{r} =a^{2}\left( -\frac{1}{r^{2}}\frac{\partial }{\partial r} +\frac{1}{r}\frac{\partial ^{2}}{\partial r^{2}} +\frac{2}{r^{3}} -\frac{1}{r^{2}}\frac{\partial }{\partial r} +\frac{2}{r}\left(\frac{1}{r}\frac{\partial }{\partial r} -\frac{1}{r^{2}}\right)\right) v$

相消化简得到

$\displaystyle \frac{\partial ^{2}}{\partial t^{2}}\frac{v}{r} =\frac{a^{2}}{r}\frac{\partial ^{2}}{\partial r^{2}} v$

同乘以 $\displaystyle r$ ，得到

$\displaystyle \frac{\partial ^{2}}{\partial t^{2}} v=a^{2}\frac{\partial ^{2}}{\partial r^{2}} v$

可以得到通解

$\displaystyle v( r,t) =v_{1}( at-r) +v_{2}( at+r)$

以及原函数的解

$u( r,t) =\frac{1}{r}( v_{1}( at-r) +v_{2}( at+r))$

其物理解释是

1. 波以速度 a 沿着径向方向向内或者向外匀速传播
2. 波幅随着距离衰减

不妨假设解为简谐波

- $v_1(at-r) = \sin(t-r)$
- $v_1(at-r) = 0$

看一看向外传播的球面波的波幅函数。用 Desmos 作图。读者可以点击链接

https://www.desmos.com/calculator/vtb5s0xym2

观看动态图

<iframe src="https://www.desmos.com/calculator/vtb5s0xym2?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

由图可见，

1. 波以速度 a 沿着径向方向向内或者向外匀速传播
2. 波幅随着距离衰减

也可以假设解为单个波

- $v_1(at-r) = e^{-(t-r)^2}$
- $v_2(at-r) = 0$

能得到相同的结论，请读者在 Desmos 网页自行尝试。



$$ a_{1}^{2} b_{2}^{2} + a_{1}^{2} b_{3}^{2} - 2 a_{1} a_{2} b_{1} b_{2} - 2 a_{1} a_{3} b_{1} b_{3} + a_{2}^{2} b_{1}^{2} + a_{2}^{2} b_{3}^{2} - 2 a_{2} a_{3} b_{2} b_{3} + a_{3}^{2} b_{1}^{2} + a_{3}^{2} b_{2}^{2} $$

$$a_{1}^{2} b_{1}^{2} + a_{1}^{2} b_{2}^{2} + a_{1}^{2} b_{3}^{3} + a_{2}^{2} b_{1}^{2} + a_{2}^{2} b_{2}^{2} + a_{2}^{2} b_{3}^{3} + a_{3}^{3} b_{1}^{2} + a_{3}^{3} b_{2}^{2} + a_{3}^{3} b_{3}^{3}$$

$$ a_{1}^{2} b_{1}^{2} + 2 a_{1} a_{2} b_{1} b_{2} + 2 a_{1} a_{3} b_{1} b_{3} + a_{2}^{2} b_{2}^{2} + 2 a_{2} a_{3} b_{2} b_{3} + a_{3}^{2} b_{3}^{2} $$
