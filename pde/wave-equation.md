# 波动方程

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

$\displaystyle \frac{\partial }{\partial t} =\frac{\partial \xi }{\partial t}\frac{\partial }{\xi } +\frac{\partial \eta }{\partial t}\frac{\partial }{\eta } =-a\frac{\partial }{\xi } +a\frac{\partial }{\eta }$

继续得到二阶偏导数算子的转换

$\displaystyle \frac{\partial }{\partial t}\frac{\partial }{\partial t} =\left( -a\frac{\partial }{\xi } +a\frac{\partial }{\eta }\right)^{2}$

同理根据链式法则，做对 $x$  偏导数的替换

$\displaystyle \frac{\partial }{\partial x} =\frac{\partial \xi }{\partial x}\frac{\partial }{\xi } +\frac{\partial \eta }{\partial x}\frac{\partial }{\eta } =\frac{\partial }{\xi } +\frac{\partial }{\eta }$

继续得到二阶偏导数算子的转换

$\displaystyle \frac{\partial }{\partial x}\frac{\partial }{\partial x} =\left(\frac{\partial }{\xi } +\frac{\partial }{\eta }\right)^{2}$

这个时候，原方程可以简化为

$\displaystyle u_{tt} -a^{2} u_{xx} =a^{2}\left( -\frac{\partial }{\xi } +\frac{\partial }{\eta }\right)^{2} -a^{2}\left(\frac{\partial }{\xi } +\frac{\partial }{\eta }\right)^{2} =-4a^{2}\frac{\partial }{\xi }\frac{\partial }{\eta } u=f( x,t)$

其中  $f( x,t)$ 的时候，

$\displaystyle \frac{\partial }{\xi }\frac{\partial }{\eta } u=0$

重积分得到

$\displaystyle u=g( \xi ) +h( \eta )$

以及非齐次方程的一个特解

$\displaystyle u^{*} =\frac{-1}{4a^{2}}\int \int f( \xi ,\eta ) d\xi d\eta $

所以通解是

$u=g( \xi ) +h( \eta ) -\frac{1}{4a^{2}}\int \int f( \xi ,\eta ) d\xi d\eta $

### 解的物理意义

现在反过头来看，变量替换

$\displaystyle \xi =x-at,\eta =x+at$

表示的是，如果盯着

$x=at, x=-at$

看，波形没有发生变化。也可以认为，波峰在以速度 $a$ 向左或者向右行进。

## 初值问题

解自由运动对应的齐次波动方程，得到通解

$u(x,t)=g( x-at ) +h( x+at )$

现在将初始条件代入第一类边界条件

$u( x,0) =g( x) +h( x) =\varphi ( x)$

和第二类边界条件

$u'( x,0) =-ag'( x) +a'h( x) =\psi ( x)$

对第二类边界条件积分

$-ag( x) +ah( x) =\int_{x_0}^x \psi ( x) dx+C_1$

代回第一类边界条件，解这个线性方程组得到

$g( x) =\frac{1}{2} \varphi ( x) -\frac{1}{2a}\int_{x_0}^x \psi ( x) dx-\frac{1}{2} C_{1}$

和

$h( x) =\frac{1}{2} \varphi ( x) +\frac{1}{2a}\int_{x_0}^x \psi ( x) dx+\frac{1}{2} C_{1}$

做变量替换，得到

$u( x,t) =\frac{1}{2} \varphi ( x-at) +\frac{1}{2} \varphi ( x+at) +\frac{1}{2a}\int _{x-at}^{x+at} \psi ( x) dx$

## Mathematica 代码

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