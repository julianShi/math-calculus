这一章节，我们考察的微分方程 differential equation, 是一元常微分方程 ordinary differential equation (ODE)。其有别于 多元偏微分方程 partial differential equation (PDE). 

我们考察 ODE 的一些有用性质，也介绍几种常用的求解方法。和工程相关的微分方程，可以参考《数学物理方法》这门课程。

## 物理问题

### 弹簧

根据胡克(Hooke)定律，一维弹簧由如下 微分方程描述

$$
m\ddot{x}(t)=-kx(t)
$$

令 $\omega^2=k/m$, 则

$$
\ddot{x}(t)+\omega^2x(t)=0
$$

已知其解为

$$
x(t) = A \cos(\omega t)+B\sin(\omega t)
$$

在此，不解释求解过程。读者可以把解 $x(t)$ 代入到原微分方程中验证。

### 其他

其他中学物理介绍过的常微分方程

自由落体，抛物线运动

$\displaystyle y''=g$

降落伞的运动。考虑空气阻力

$\displaystyle mv'=mg-bv^{2}$

电路

$\displaystyle LI''+RI'+I/C=E'$

单摆

$\displaystyle L\theta ''+g\sin \theta =0$

## 常微分方程的分类

物理给数学家提供了很多有趣的微分方程。但是，即使能写出解析的微分方程，迄今发现，能简单求得解析解的，也只占其中一小部分。不容易求解的微分方程，诸如

* 三体问题 

$$
\ddot{r}_{i} =-\frac{GM_{j}{}}{|r_{i} -r_{j} |^{3}}( r_{i} -r_{j}) -\frac{GM_{k}}{|r_{i} -r_{k} |^{3}}( r_{i} -r_{k})
$$

* 一维连续弹性体（比如尺子）碰撞问题 （非光滑）

$$
\rho A\frac{\partial ^{2} u}{\partial t^{2}} dx=EA\frac{\partial ^{2} u}{\partial x^{2}} dx, u \leq U
$$

这些不容易求解的，需要用到更复杂的数学工具，比如说 微扰法，数值方法等，不在《高等数学》的讨论范围内。

本章只介绍几种适用于简单求解的 常微分方程（后文简称为“方程”），引读者入门。

### 按照阶数区分

按照最高微分项，来区分

- 一阶。诸如 $y'+y=x$
- 二阶。诸如 $y''= \sqrt{x+y}$ 
- 高阶。诸如 $y^{(n)} + 3x y^{(n-1)} + ... =0$

### 按照线性区分

形如如下形式的是线性微分方程

$$
a_n(x)y^{(n)} + a_{n-1}(x)y^{(n-1)} + \dots + a_1(x)y' + a_0(x)y = b(x)
$$

其中 $y^{(n)}$ 都是一次幂（无平方、乘积、三角函数等非线性运算）

否则，为非线形微分方程。

| **性质**     | **线性微分方程**                                             | **非线性微分方程**                                     |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------ |
| **叠加原理** | 成立：若 $y_1, y_2$ 是解，则 $C_1y_1 + C_2y_2$ 也是解（齐次方程）。 | 不成立：解的线性组合通常不是解。                       |
| **求解方法** | 有系统解法（如分离变量、常数变易法、特征方程法等）。         | 无通用解法，仅特殊类型可解（如可降阶、伯努利方程等）。 |
| **解的结构** | 解空间是线性空间，通解可表示为特解+齐次通解。                | 解的结构复杂，可能出现混沌、分岔等现象。               |
| **适用场景** | 描述线性系统（如小幅度振动、线性电路等）。                   | 描述非线性系统（如大变形力学、混沌现象、化学反应等）。 |

### 按照齐次/非齐次区分

齐次方程有简单解法。这里不作过多介绍。留在各个小节中介绍。



## 目录

1. 微分方程的基本概念 (Basic Concepts of Differential Equations)
2. 可分离变量的微分方程 (Separable Differential Equations)
3. 齐次方程 (Homogeneous Equations)
4. 一阶线性微分方程 (First-Order Linear Differential Equations)
5. 可降阶的高阶微分方程 (Higher-Order Differential Equations That Can Be Reduced in Order)
6. 高阶线性微分方程 (Higher-Order Linear Differential Equations)
7. 常系数齐次线性微分方程 (Linear Homogeneous Differential Equations with Constant Coefficients)
8. 常系数非齐次线性微分方程 (Linear Nonhomogeneous Differential Equations with Constant Coefficients)