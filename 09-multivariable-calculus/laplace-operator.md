# 拉普拉斯算子

在[数学](https://zh.wikipedia.org/wiki/數學)以及[物理](https://zh.wikipedia.org/wiki/物理)中，**拉普拉斯算子**或是**拉普拉斯算符**（英语：Laplace operator, Laplacian）是由[欧几里得空间](https://zh.wikipedia.org/wiki/欧几里得空间)中的一个函数的[梯度](https://zh.wikipedia.org/wiki/梯度)的[散度](https://zh.wikipedia.org/wiki/散度)给出的[微分算子](https://zh.wikipedia.org/wiki/微分算子)，通常写成

- $\Delta$
- $\nabla^2$
- $\nabla \cdot \nabla$

拉普拉斯算子出现描述许多物理现象的微分方程里。例如，常用于[波方程](https://zh.wikipedia.org/wiki/波方程)的[数学模型](https://zh.wikipedia.org/wiki/数学模型)、[热传导方程](https://zh.wikipedia.org/wiki/熱傳導方程)、[流体力学](https://zh.wikipedia.org/wiki/流体力学)以及[亥姆霍兹方程](https://zh.wikipedia.org/wiki/亥姆霍茲方程式)。在[静电学](https://zh.wikipedia.org/wiki/靜電學)中，[拉普拉斯方程](https://zh.wikipedia.org/wiki/拉普拉斯方程)和[泊松方程](https://zh.wikipedia.org/wiki/泊松方程)的应用随处可见。在[量子力学](https://zh.wikipedia.org/wiki/量子力學)中，其代表[薛定谔方程](https://zh.wikipedia.org/wiki/薛丁格方程)中的[动能](https://zh.wikipedia.org/wiki/動能)项。

## 平面极坐标 Laplace

在直角坐标系中，Laplace 算子的定义是

$\nabla ^{2} =\frac{\partial ^{2}}{\partial x^{2}} +\frac{\partial ^{2}}{\partial y^{2}} =\left(\frac{\partial }{\partial x} ,\frac{\partial }{\partial y}\right)\left(\frac{\partial }{\partial x} ,\frac{\partial }{\partial y}\right)^{T}$

回顾 [nabla-operator.md](nabla-operator.md), 一阶偏导 Nabla 算子的坐标变换公式

$\begin{pmatrix}
\frac{\partial }{\partial x}\\
\frac{\partial }{\partial y}
\end{pmatrix} = \displaystyle \left(\begin{array}{ c c }
\cos (\theta ) & -\frac{\sin (\theta )}{r}\\
\sin (\theta ) & \frac{\cos (\theta )}{r}
\end{array}\right)\begin{pmatrix}
\frac{\partial }{\partial r}\\
\frac{\partial }{\partial \theta }
\end{pmatrix} =\begin{pmatrix}
\cos \theta \frac{\partial }{\partial r} -\frac{\sin \theta }{r}\frac{\partial }{\partial \theta }\\
\sin \theta \frac{\partial }{\partial r} +\frac{\cos \theta }{r}\frac{\partial }{\partial \theta }
\end{pmatrix}$

现在分别对 $x$ 求两次复合偏导

$\displaystyle  \begin{array}{{>{\displaystyle}l}} \frac{\partial ^{2}}{\partial x^{2}} =
\left(\cos \theta \frac{\partial }{\partial r} -\frac{\sin \theta }{r}\frac{\partial }{\partial \theta }\right)\left(\cos \theta \frac{\partial }{\partial r} -\frac{\sin \theta }{r}\frac{\partial }{\partial \theta }\right)\\
=\cos^{2} \theta \frac{\partial ^{2}}{\partial r^{2}} +\frac{\sin \theta \cos \theta }{r^{2}}\frac{\partial }{\partial \theta } +\frac{\sin^{2} \theta }{r}\frac{\partial }{\partial r} +\sin \theta \frac{\partial }{\partial \theta }\left(\sin \theta \frac{\partial }{\partial \theta }\right)\\
=\cos^{2} \theta \frac{\partial ^{2}}{\partial r^{2}} +\frac{\sin \theta \cos \theta }{r^{2}}\frac{\partial }{\partial \theta } +\frac{\sin^{2} \theta }{r}\frac{\partial }{\partial r} +\frac{\sin \theta \cos \theta }{r^{2}}\frac{\partial }{\partial \theta } +\frac{\sin^{2} \theta }{r^{2}}\frac{\partial ^{2}}{\partial \theta ^{2}}\\
=\cos^{2} \theta \frac{\partial ^{2}}{\partial r^{2}} +\frac{\sin^{2} \theta }{r}\frac{\partial }{\partial r} +\frac{\sin^{2} \theta }{r^{2}}\frac{\partial ^{2}}{\partial \theta ^{2}} +\frac{2\sin \theta \cos \theta }{r^{2}}\frac{\partial }{\partial \theta }
\end{array}$

以及对 $y$ 求两次复合偏导

$\displaystyle  \begin{array}{{>{\displaystyle}l}} \frac{\partial ^{2}}{\partial y^{2}} =
\left(\sin \theta \frac{\partial }{\partial r} +\frac{\cos \theta }{r}\frac{\partial }{\partial \theta }\right)\left(\sin \theta \frac{\partial }{\partial r} +\frac{\cos \theta }{r}\frac{\partial }{\partial \theta }\right)\\
=\sin \theta \frac{\partial }{\partial r}\left(\sin \theta \frac{\partial }{\partial r}\right) +\sin \theta \frac{\partial }{\partial r}\left(\frac{\cos \theta }{r}\frac{\partial }{\partial \theta }\right) +\frac{\cos \theta }{r}\frac{\partial }{\partial \theta }\left(\sin \theta \frac{\partial }{\partial r}\right) +\left(\frac{\cos \theta }{r}\frac{\partial }{\partial \theta }\right)\left(\frac{\cos \theta }{r}\frac{\partial }{\partial \theta }\right)\\
=\sin^{2} \theta \frac{\partial ^{2}}{\partial r^{2}} -\frac{\sin \theta \cos \theta }{r^{2}}\frac{\partial }{\partial \theta } +\frac{\cos^{2} \theta }{r}\frac{\partial }{\partial r} -\frac{\sin \theta \cos \theta }{r^{2}}\frac{\partial }{\partial \theta } +\frac{\cos^{2} \theta }{r^{2}}\frac{\partial ^{2}}{\partial \theta ^{2}}\\
=\sin^{2} \theta \frac{\partial ^{2}}{\partial r^{2}} -\frac{2\sin \theta \cos \theta }{r^{2}}\frac{\partial }{\partial \theta } +\frac{\cos^{2} \theta }{r}\frac{\partial }{\partial r} +\frac{\cos^{2} \theta }{r^{2}}\frac{\partial ^{2}}{\partial \theta ^{2}}
\end{array}$

求和并化简得到

$\displaystyle \frac{\partial ^{2}}{\partial x^{2}} +\frac{\partial ^{2}}{\partial y^{2}}=\frac{\partial ^{2}}{\partial r^{2}} +\frac{1}{r}\frac{\partial }{\partial r} +\frac{1}{r^{2}}\frac{\partial ^{2}}{\partial \theta ^{2}}$

用 Mathematica 求解

```mathematica
(*Derivative over x in polar coordinates*)
duDx[r_,\[Theta]_]:=Cos[\[Theta]]*D[#1,r]-Sin[\[Theta]]/r*D[#1,\[Theta]] &

(*Second derivative over x in polar coordinates*)
duDx2=duDx[r,\[Theta]][duDx[r,\[Theta]][u[r,\[Theta]]]]

(*Derivative over y in polar coordinates*)
duDy[r_,\[Theta]_]:=Sin[\[Theta]]*D[#1,r]+Cos[\[Theta]]/r*D[#1,\[Theta]] &

(*Second derivative over y in polar coordinates*)
duDy2=duDy[r,\[Theta]][duDy[r,\[Theta]][u[r,\[Theta]]]]

(*Laplace operator in polar coordinates*)
Simplify[duDx2+duDy2]
```

见在线结果

https://www.wolframcloud.com/obj/yulinshiapp/Published/09-laplace-operator.nb

## 讨论：能否用系数矩阵求逆法

回顾 [nabla-operator.md](nabla-operator.md), 我们用系数矩阵求逆法，简化了一阶偏导 nabla 算子的转换表达式计算

$\nabla =\frac{\partial }{\partial x_{i}} =\mathbf{J}^{-1}\frac{\partial }{\partial r_{j}}$

其中 $i$  表示直角坐标系下的2个坐标，$j$ 表示球坐标系下的2个坐标。那么

$\nabla ^{2} =\left(\frac{\partial }{\partial x_{i}}\right)^{T}\left(\frac{\partial }{\partial x_{i}}\right) =\left(\mathbf{J}^{-1}\frac{\partial }{\partial r_{j}}\right)^{T}\left(\mathbf{J}^{-1}\frac{\partial }{\partial r_{j}}\right)$

到这一步，读者似乎看到了线性代数矩阵简化的希望。但是遗憾的是，算子并不满足交换律

$( AB)^{T} \neq B^{T} A^{T}$

即

$\left(\mathbf{J}^{-1}\frac{\partial }{\partial r_{j}}\right)^{T} \neq \left(\frac{\partial }{\partial r_{j}}\right)^{T}\mathbf{J}^{-T}$

所以，简化计算的尝试失败。还是得一步一步地计算 二阶偏导 Laplace 算子的转换表达式。

## 球坐标 Laplace

三维 Laplace 定义

$\nabla ^{2} =\frac{\partial ^{2}}{\partial x^{2}} +\frac{\partial ^{2}}{\partial y^{2}} +\frac{\partial ^{2}}{\partial z^{2}}$

将求解二维极坐标的Laplace的方法，推广到三维球坐标 sphere coordinates。

回顾 [nabla-operator.md](nabla-operator.md), 一阶偏导 Nabla 算子的球坐标变换公式，同理可以求二阶偏导，再求和得到答案。

但是过程过于冗长，不值得手算，所以我们求助于 Mathematica

```Mathematica
(*Part 2: Laplace in sphere coordinates*)
x[r_,\[Theta]_,\[Phi]_]:=r*Cos[\[Theta]]*Cos[\[Phi]];
y[r_,\[Theta]_,\[Phi]_]:=r*Cos[\[Theta]]*Sin[\[Phi]];
z[r_,\[Theta]_,\[Phi]_]:=r*Sin[\[Theta]];

(*Jacob coefficient matrix*)
J3={
{D[x[r,\[Theta],\[Phi]],r],D[y[r,\[Theta],\[Phi]],r],D[z[r,\[Theta],\[Phi]],r]},
{D[x[r,\[Theta],\[Phi]],\[Theta]],D[y[r,\[Theta],\[Phi]],\[Theta]],D[z[r,\[Theta],\[Phi]],\[Theta]]},
{D[x[r,\[Theta],\[Phi]],\[Phi]],D[y[r,\[Theta],\[Phi]],\[Phi]],D[z[r,\[Theta],\[Phi]],\[Phi]]}
}

(*This is the coefficient matrix from x-y-z coordinates to shpere coordinates*)
J3Inverse=Simplify[Inverse[J3]]
(*==== The above are the same to nabla-operator.md =====*)

(*This is the first-order nabla operator in shpere coordinates*)
dvDx=J3Inverse[[1]].{D[#1,r],D[#1,\[Theta]],D[#1,\[Phi]]}& 
dvDy=J3Inverse[[2]].{D[#1,r],D[#1,\[Theta]],D[#1,\[Phi]]}& 
dvDz=J3Inverse[[3]].{D[#1,r],D[#1,\[Theta]],D[#1,\[Phi]]}& 

(*Second-order direvatives in shpere coordinates*)
dvDx2=dvDx[dvDx[u[r,\[Theta],\[Phi]]]]
dvDy2=dvDy[dvDy[u[r,\[Theta],\[Phi]]]]
dvDz2=dvDz[dvDz[u[r,\[Theta],\[Phi]]]]
(*You can see how tedious and error prone if we calculate manually*)

(*This is the Laplace operator in sphere coordinates*)
laplace3=Simplify[dvDx2+dvDy2+dvDz2]
```

我这里贴出来对 $x$ 的二阶偏导，只为了让读者感受一下手算的难度。

$ \begin{array}{l}
\frac{\partial ^{2} u}{\partial x^{2}} =\cos \theta \cos \phi \left(\frac{\sin \theta \cos \phi u^{(0,1,0)}}{r^{2}} +\frac{\sec \theta \sin \phi u^{(0,0,1)}}{r^{2}} +\cos \theta \cos \phi u^{(2,0,0)} -\frac{\sin \theta \cos \phi u^{(1,1,0)}}{r} -\frac{\sec \theta \sin \phi u^{(1,0,1)}}{r}\right)\\
-\frac{\sec \theta \sin \phi }{r}\left(\frac{\sin \theta \sin \phi u^{(0,1,0)}}{r} +\cos \theta \cos \phi u^{(1,0,1)} -\frac{\sin \theta \cos \phi u^{(0,1,1)}}{r} -\cos \theta \sin \phi u^{(1,0,0)} -\frac{\sec \theta \cos \phi u^{(0,0,1)}}{r} -\frac{\sec \theta \sin \phi u^{(0,0,2)}}{r}\right)\\
-\frac{\sin \theta \cos \phi }{r}\left( -\frac{\cos \theta \cos \phi u^{(0,1,0)}}{r} +\cos \theta \cos \phi u^{(1,1,0)} -\frac{\sin \theta \cos \phi u^{(0,2,0)}}{r} -\sin \theta \cos \phi u^{(1,0,0)} -\frac{\sec \theta \sin \phi u^{(0,1,1)}}{r} -\frac{\tan \theta \sec \theta \sin \phi u^{(0,0,1)}}{r}\right)
\end{array}$

最终大多数项可以相消，得到最终答案

$\nabla^2=\frac{\partial ^{2}}{\partial r^{2}} +\frac{2}{r}\frac{\partial }{\partial r} +\frac{1}{r^{2}}\left(\frac{\partial ^{2}}{\partial \theta ^{2}} -\tan \theta \frac{\partial }{\partial \theta } +\sec^{2} \theta \frac{\partial ^{2}}{\partial \phi ^{2}}\right)$

见在线结果 

https://www.wolframcloud.com/obj/yulinshiapp/Published/09-laplace-operator.nb

