# 哈密顿算子

在场论当中，我们用算子表示不同的微分组合。

用二维举例，对于标量函数 $f(x,y)$, 

$\nabla \cdot f:=\left(\frac{\partial }{\partial x} ,\frac{\partial }{\partial y}\right) f$

这个定义的 $\nabla$ 就是 哈密顿算子（Hamiltonian）

## 平面极坐标 Nabla

平面极坐标 polar coordinates 变换公式

- $x=r\cos \theta $
- $y=r\sin \theta $

其中，$r,\theta$  是独立变量。如图

![polar-coordinates](resources/polar-coordinates.svg)

在三维空间中，叫做柱坐标。 $z$   方向不需要做坐标转换。

### Jacob 矩阵求逆法

容易得到偏微分

- $\frac{\partial x}{\partial r} =\cos \theta ,\frac{\partial x}{\partial \theta } =-r\sin \theta$
- $\frac{\partial y}{\partial r} =\sin \theta ,\frac{\partial y}{\partial \theta } =r\cos \theta$

按照链式法则，

- $\frac{\partial }{\partial r} =\frac{\partial x}{\partial r}\frac{\partial }{\partial x} +\frac{\partial y }{\partial r}\frac{\partial }{\partial y }$
- $\frac{\partial }{\partial \theta } =\frac{\partial x}{\partial \theta }\frac{\partial }{\partial x} +\frac{\partial y }{\partial \theta }\frac{\partial }{\partial y }$

可见其偏导算子的变换是线性的。可以写成矩阵形式

$\begin{pmatrix}
\frac{\partial }{\partial r}\\
\frac{\partial }{\partial \theta }
\end{pmatrix} =\frac{\partial ( x,y)}{\partial ( r,\theta )}\begin{pmatrix}
\frac{\partial }{\partial x}\\
\frac{\partial }{\partial y}
\end{pmatrix} =\begin{pmatrix}
\cos \theta  & \sin \theta \\
-r\sin \theta  & r\cos \theta 
\end{pmatrix}\begin{pmatrix}
\frac{\partial }{\partial x}\\
\frac{\partial }{\partial y}
\end{pmatrix}$

其中，系数叫做雅可比 Jacob 矩阵

$\mathbf{J}=\frac{\partial ( x,y)}{\partial ( r,\theta )}$

既然两套偏导算子是线性关系，可以用矩阵求逆的方式，计算出逆变换

$\begin{pmatrix}
\frac{\partial }{\partial x}\\
\frac{\partial }{\partial y}
\end{pmatrix} =\left(\frac{\partial ( x,y)}{\partial ( r,\theta )}\right)^{-1}\begin{pmatrix}
\frac{\partial }{\partial r}\\
\frac{\partial }{\partial \theta }
\end{pmatrix}$

其中，Jacob 矩阵的逆是

$\mathbf{J}^{-1} =\begin{pmatrix}
\cos \theta  & \sin \theta \\
-r\sin \theta  & r\cos \theta 
\end{pmatrix}^{-1} =\left(\begin{array}{ c c }
\cos (\theta ) & -\frac{\sin (\theta )}{r}\\
\sin (\theta ) & \frac{\cos (\theta )}{r}
\end{array}\right)$

用这一套线性变换，就能够得到 二维极坐标表示的 Nabla 算子

$\nabla \cdot f=\left(\begin{array}{ c c }
\cos (\theta ) & -\frac{\sin (\theta )}{r}\\
\sin (\theta ) & \frac{\cos (\theta )}{r}
\end{array}\right)\begin{pmatrix}
\frac{\partial }{\partial r}\\
\frac{\partial }{\partial \theta }
\end{pmatrix} f$

用 Mathematica 求解

```mathematica
(*Part 1: nabla in polar coordinates*)
(*Define functions*)
x[r_,\[Theta]_]:=r*Cos[\[Theta]];
y[r_,\[Theta]_]:=r*Sin[\[Theta]];

(*Jacob coefficient matrix*)
J={
  {D[x[r,\[Theta]],r],{D[y[r,\[Theta]],r],
  D[x[r,\[Theta]],\[Theta]]},D[y[r,\[Theta]],\[Theta]]}
}

(*Inverse of the Jacob coefficient matrix*)
JInverse=Simplify[Inverse[J]]

MatrixForm[JInverse]
```

### 直接方法

读者们可以尝试先做坐标的逆转换，

- $r=\sqrt{x^{2} +y^{2}}$
- $\theta =\arctan\frac{y}{x}$

这样可以避免求 Jacob 系数矩阵的逆，而是直接求解极坐标下的 Nabla 算符表达式，但是步骤会更冗长一些。

用 Mathematica 求解

```mathematica
(*Part 1: nabla in polar coordinates*)
(*Define functions*)
r[x_,y_]:=Sqrt[x^2+y^2];
\[Theta][x_,y_]:=ArcTan[y/x];

(*Calculate the nabla in polar coordinates*)
polarNabla={
  {D[r[x,y],x],D[r[x,y],y]},
  {D[\[Theta][x,y],x],D[\[Theta][x,y],y]}
}

(*Prettify and print the nabla in polar coordinates*)
polarNabla1=MatrixForm[Simplify[polarNabla]]

(*Express the x,y in r,\[Theta]*)
Simplify[(polarNabla1/.x->r*Cos[\[Theta]])/.y->r*Sin[\[Theta]],Assumptions -> r > 0]
```

## 球面坐标 Nabla

将定义推广到三维

- $x=r\cos \theta \cos \phi $
- $y=r\cos \theta \sin \phi $
- $z=r\sin \theta $

其中，在球坐标当中， $\theta$ 是纬度， $\phi$ 是经度。如图

![sphere-coordinates](resources/sphere-coordinates.svg)

### Jacob 矩阵求逆法

用 Mathematica 求解微分

```mathematica
(*Part 2: nabla in sphere coordinates*)
(*Define functions*)
Clear[x,y,z];
x[r_,\[Theta]_,\[Phi]_]:=r*Cos[\[Theta]]*Cos[\[Phi]];
y[r_,\[Theta]_,\[Phi]_]:=r*Cos[\[Theta]]*Sin[\[Phi]];
z[r_,\[Theta]_,\[Phi]_]:=r*Sin[\[Theta]];

(*Jacob coefficient matrix*)
J3={
  {D[x[r,\[Theta],\[Phi]],r],D[y[r,\[Theta],\[Phi]],r],D[z[r,\[Theta],\[Phi]],r]},
  {D[x[r,\[Theta],\[Phi]],\[Theta]],D[y[r,\[Theta],\[Phi]],\[Theta]],D[z[r,\[Theta],\[Phi]],\[Theta]]},
  {D[x[r,\[Theta],\[Phi]],\[Phi]],D[y[r,\[Theta],\[Phi]],\[Phi]],D[z[r,\[Theta],\[Phi]],\[Phi]]}
}

(*Inverse of the Jacob coefficient matrix*)
J3Inverse=Simplify[Inverse[J3]]

MatrixForm[J3Inverse]
```

得到答案

$\nabla =\frac{\partial }{\partial x_{i}} =\frac{\partial r_{j}}{\partial x_{i}}\frac{\partial }{\partial r_{j}}$

其中 $i$  表示直角坐标系下的3个坐标，$j$ 表示球坐标系下的3个坐标。系数矩阵

$\frac{\partial r_{j}}{\partial x_{i}} =\left(
\begin{array}{ccc}
 \cos (\theta ) \cos (\phi ) & -\frac{\sin (\theta ) \cos (\phi )}{r} & -\frac{\sec
  (\theta ) \sin (\phi )}{r} \\
 \cos (\theta ) \sin (\phi ) & -\frac{\sin (\theta ) \sin (\phi )}{r} & \frac{\sec
  (\theta ) \cos (\phi )}{r} \\
 \sin (\theta ) & \frac{\cos (\theta )}{r} & 0 \\
\end{array}
\right)$

读者也可以访问在线笔记，阅读上述代码和渲染的输出

https://www.wolframcloud.com/obj/yulinshiapp/Published/09-nabla-operator.nb

