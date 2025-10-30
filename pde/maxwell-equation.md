# 求解麦克斯韦方程组

”上帝说麦克斯韦，然后就有了光” -- **光速不变原理**是通过求解**麦克斯韦方程组**得到的，并为 1887年迈克尔逊-莫雷实验所证实，是学习狭义相对论的基础。在麦克斯韦之前，人们对于光速充满了疑问。

1. 为什么真空中光速不变。光还能更快一些吗？
2. 为什么光的传播不需要以太作为介质？
3. 为什么不同惯性系中，测量的光速不变？

本文将带领读者，一步一步推导光速，对光速去魅。

目录

1. 微分形式的麦克斯韦方程组
2. 构造波动方程
3. 求解一维波动方程
4. 求解光速
5. 求解三维球对称波动方程

## 微分形式的麦克斯韦方程组

回顾微分形式的麦克斯韦 Maxwell 方程组

1. 法拉第感应定律

$\displaystyle \nabla \times \vec{E} =-\frac{\partial \vec{B}}{\partial t}$

其中 $\displaystyle \vec{E}$ 是电场，$\displaystyle \vec{B}$ 是磁场，是坐标和时间的函数

2. 麦克斯韦-安培定律

$\displaystyle \nabla \times \vec{B} =\mu _{0}\vec{J} +\mu _{0} \epsilon _{0}\frac{\partial \vec{E}}{\partial t}$

其中，$\displaystyle \mu _{0}$ 是磁常数，$\displaystyle \epsilon _{0}$ 是电常数，$\displaystyle \vec{J}$ 是电流密度

3. 高斯定律

$\displaystyle \nabla \cdot \vec{E} =\frac{\rho }{\epsilon _{0}}$

其中，$\displaystyle \rho $ 是电荷密度。

4. 高斯磁定律（宇宙中没有观察到过磁单极）

$\displaystyle \nabla \cdot \vec{B} =0$

考虑真空环境中，没有电流或者电荷，把麦克斯韦方程组重写为

1. $\displaystyle \nabla \times \vec{E} =-\frac{\partial \vec{B}}{\partial t}$

2. $\displaystyle \nabla \times \vec{B} =\mu _{0} \epsilon _{0}\frac{\partial \vec{E}}{\partial t}$

3. $\displaystyle \nabla \cdot \vec{E} =0$

4. $\displaystyle \nabla \cdot \vec{B} =0$

其中，电场和磁场在真空的散度为0

## 波动方程

接下来求解真空中电场，磁场，和电磁波传播速度（光速）

对1式两边求旋度

$\displaystyle \nabla \times \nabla \times \vec{E} =-\nabla \times \frac{\partial \vec{B}}{\partial t}$

根据二阶旋度恒等式 [hamilton-operations.md](../09-multivariable-calculus/hamilton-operations.md)，和偏导的交换律

$\displaystyle \nabla ( \nabla \cdot \vec{E}) -\nabla ^{2}\vec{E} =-\frac{\partial }{\partial t}( \nabla \times \vec{B})$

代入3式和2式，得到

$\displaystyle -\nabla ^{2}\vec{E} =-\frac{\partial }{\partial t}\left( \mu _{0} \epsilon _{0}\frac{\partial \vec{E}}{\partial t}\right)$

化简成标准形式，得到

$\displaystyle \frac{\partial ^{2}\vec{E}}{\partial t^{2}} =\frac{1}{\mu _{0} \epsilon _{0}} \nabla ^{2}\vec{E}$

同理可以得到

$\displaystyle \frac{\partial ^{2}\vec{B}}{\partial t^{2}} =\frac{1}{\mu _{0} \epsilon _{0}} \nabla ^{2}\vec{B}$

可见，两者都是标准的波动方程。

## 一维波动方程

考虑一维情况，比如说光纤里的电磁波，激光束，或者平面光墙附近的法向光波。

不妨只先求解 x 方向电场 和时间的函数，和 y, z 无关

$\displaystyle \vec{E}( x, y, z, t) =E( x,t)\vec{e}$

$E( x,t)$ 是标量场。

下文将隐去自变量 $\displaystyle x,t$ 

向量场的波动方程变成标量场的波动方程

$\displaystyle \frac{\partial ^{2}}{\partial t^{2}} E =\frac{1}{\mu _{0} \epsilon _{0}}\frac{\partial ^{2}}{\partial x^{2}} E$

参考 [../pde/wave-equation.md](../pde/wave-equation.md) 可解得电场通解

$\displaystyle E=E_{1}( ct-x) +E_{2}( ct+x)$

其中 $\displaystyle c=\frac{1}{\sqrt{\mu _{0} \epsilon _{0}}}$ ，就是波传播的速度（光速）

根据解的形式，知道，电磁波（光波）能以速度 $c$ 匀速地向 x 轴正方向和反方向传播。

在上述推导过程中，没有像机械波（声波，水面波等）一样，需要借助传播介质来构造波动方程。所以说，电磁波不依赖于介质，不依赖于参考系。这一结论是狭义相对论的基础。

## 光速

实验测得

1. 真空磁导率 $\displaystyle \mu _{0} \approx 1.25663706212\times 10^{-6}( V\cdot s) /( A\cdot m)$

2. 真空电容率 $\displaystyle \epsilon _{0} \approx 8.854187817\times 10^{-12} F/m$

所以真空光速

 $c =\frac{1}{\sqrt{\mu _{0} \epsilon _{0}}} \approx \frac{1}{\sqrt{1.25663706212\times 10^{-6} \times 8.854187817\times 10^{-12}}} m/s$

即

$c \approx 2.997924579\times 10^{8} m/s$

## 三维球面波

求解一种特殊情况，即三维球对称情况的电场波动方程。比如说点光源的情况。

这个时候，电场只是距离和时间的函数，和角度无关

$\displaystyle \vec{E}( r,\theta ,\phi ,t) =E( r,t)\vec{e}$

下文将隐去自变量 $\displaystyle r,t$ 

向量场的波动方程变成标量场的波动方程

$\displaystyle \frac{\partial ^{2}}{\partial t^{2}} E =\frac{1}{\mu _{0} \epsilon _{0}}\nabla^2 E$

参考 [laplace-operator.md](../09-multivariable-calculus/laplace-operator.md)，已知在球坐标中，拉普拉斯算子

$\nabla^2=\frac{\partial ^{2}}{\partial r^{2}} +\frac{2}{r}\frac{\partial }{\partial r} +\frac{1}{r^{2}}\left(\frac{\partial ^{2}}{\partial \theta ^{2}} -\tan \theta \frac{\partial }{\partial \theta } +\sec^{2} \theta \frac{\partial ^{2}}{\partial \phi ^{2}}\right)$

因为球对称的假设，所以对 $\theta, \phi$ 的偏导数都为 0

$\nabla^2=\frac{\partial ^{2}}{\partial r^{2}} +\frac{2}{r}\frac{\partial }{\partial r}$ 

这个时候，形如

$\displaystyle \frac{\partial ^{2}}{\partial t^{2}} E=c^{2}\left(\frac{\partial ^{2}}{\partial r^{2}} +\frac{2}{r}\frac{\partial }{\partial r}\right) E$

的波动方程仍然难以求解。但是可以作如下变量替换

$\displaystyle v=rE$

那么

$\displaystyle E=\frac{v}{r}$

一阶偏导

$\displaystyle \frac{\partial }{\partial r}\frac{v}{r} =\left(\frac{1}{r}\frac{\partial }{\partial r} -\frac{1}{r^{2}}\right) v$

二阶偏导

$\displaystyle \frac{\partial ^{2}}{\partial r^{2}}\frac{v}{r} =\frac{\partial }{\partial r}\left(\frac{1}{r}\frac{\partial }{\partial r} -\frac{1}{r^{2}}\right) v=\left( -\frac{1}{r^{2}}\frac{\partial }{\partial r} +\frac{1}{r}\frac{\partial ^{2}}{\partial r^{2}} +\frac{2}{r^{3}} -\frac{1}{r^{2}}\frac{\partial }{\partial r}\right) v$

代回原波动方程，得到

$\displaystyle \frac{\partial ^{2}}{\partial t^{2}}\frac{v}{r} =c^{2}\left( -\frac{1}{r^{2}}\frac{\partial }{\partial r} +\frac{1}{r}\frac{\partial ^{2}}{\partial r^{2}} +\frac{2}{r^{3}} -\frac{1}{r^{2}}\frac{\partial }{\partial r} +\frac{2}{r}\left(\frac{1}{r}\frac{\partial }{\partial r} -\frac{1}{r^{2}}\right)\right) v$

相消化简得到

$\displaystyle \frac{\partial ^{2}}{\partial t^{2}}\frac{v}{r} =\frac{c^{2}}{r}\frac{\partial ^{2}}{\partial r^{2}} v$

同乘以 $\displaystyle r$ ，得到

$\displaystyle \frac{\partial ^{2}}{\partial t^{2}} v=c^{2}\frac{\partial ^{2}}{\partial r^{2}} v$

令人欣喜的是，这正是一维波动方程标准形式，有通解

$\displaystyle v( r,t) =v_{1}( ct-r) +v_{2}( ct+r)$

所以，波的解为

$\displaystyle E( r,t) =\frac{1}{r}( v_{1}( ct-r) +v_{2}( ct+r))$

其物理意义是，电磁波（光）以光速 $\displaystyle c$ 沿着径向向内或者向外传播。

其波幅以距离倒数衰减。

同理，可得到球对称的磁场函数

$\displaystyle B( r,t) =\frac{1}{r}( v_{3}( ct-r) +v_{4}( ct+r))$

考虑电磁波能量密度公式

$\displaystyle \sigma =\frac{\epsilon _{0}}{2} E^{2} +\frac{1}{2\mu _{0}} B^{2}$

可得到球对称的电磁波能量密度函数为

$\displaystyle \sigma ( r,t) =\frac{\epsilon _{0}}{2} E^{2}( r,t) +\frac{2}{\mu _{0}} B^{2}( r,t)$

代入得到

$\displaystyle \sigma ( r,t) =\frac{\epsilon _{0}}{2r^{2}}( v_{1}( ct-r) +v_{2}( ct+r))^{2} +\frac{1}{2\mu _{0} r^{2}}( v_{3}( ct-r) +v_{4}( ct+r))^{2}$

可见，能量密度以距离平方的倒数衰减。

这是因为，随着距离增加，球面光波总面积和距离平方成正比。两项相乘，得到总的电磁波能量守恒。

