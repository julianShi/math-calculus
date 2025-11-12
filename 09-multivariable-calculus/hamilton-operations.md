# 哈密顿算子和运算

哈密顿算子和运算规则在数学、物理及工程等多个领域都具有重要意义和广泛的实用性。

目录

1. 哈密顿算子
2. 三种基本运算
4. 常用公式总结

## 哈密顿算子

三维空间中，哈密顿 Hamilton 算子定义如下

$\displaystyle \nabla :=\frac{\partial }{\partial x}\vec{i} +\frac{\partial }{\partial y}\vec{j} +\frac{\partial }{\partial z}\vec{k}$

其中 $\displaystyle \vec{i} ,\vec{j} ,\vec{k}$ 表示三维直角坐标系中  $\displaystyle x,y,z$ 方向的单位基向量。

令 $\displaystyle u$ 表示标量函数 $\displaystyle u( x,y,z)$

$\displaystyle \vec{A} \ $ 表示3维向量（也叫做矢量）函数

$\displaystyle \vec{A} =A_{x}\vec{i} +A_{y}\vec{j} +A_{z}\vec{k}$

其中下标表示的是在这个方向的分量标量，不表示偏导数

有时候也用粗体 $\displaystyle \mathbf{A}$ 来表示向量

## 三种基本运算

其有三种基本的运算

1. 标量函数的梯度运算

$\displaystyle \nabla u=\left(\frac{\partial }{\partial x}\vec{i} +\frac{\partial }{\partial y}\vec{j} +\frac{\partial }{\partial z}\vec{k}\right) u$

2. 向量函数的散度运算

$\displaystyle \nabla \cdot \vec{A} =\left(\frac{\partial }{\partial x}\vec{i} +\frac{\partial }{\partial y}\vec{j} +\frac{\partial }{\partial z}\vec{k}\right) \cdot ( A_{x}\vec{i} +A_{y}\vec{j} +A_{z}\vec{k}) =\frac{\partial A_{x}}{\partial x} +\frac{\partial A_{y}}{\partial y} +\frac{\partial A_{z}}{\partial z}$

3. 向量函数的旋度运算

$\displaystyle \nabla \times \vec{A} =\begin{vmatrix}
\vec{i} & \vec{j} & \vec{k}\\
\frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z}\\
A_{x} & A_{y} & A_{z}
\end{vmatrix} =\left(\frac{\partial A_{z}}{\partial y} -\frac{\partial A_{y}}{\partial z}\right)\vec{i} +\left(\frac{\partial A_{x}}{\partial z} -\frac{\partial A_{z}}{\partial x}\right)\vec{j} +\left(\frac{\partial A_{y}}{\partial x} -\frac{\partial A_{x}}{\partial y}\right)\vec{k}$

从上到下，总结为

| 简写 | 名称 | 物理示例 |
| ---- | ---- | -------- |
| grad | 梯度 | 温度场的温度梯度（热流方向） |
| div  | 散度 | 流体速度场的源汇强度（出入流）   |
| curl | 旋度 | 流体速度场的旋转（涡度/龙卷风）   |

## 常用恒等式

### 几个运算技巧

梯度的旋度为0

$\nabla \times ( \nabla u) =\vec{0}$

旋度的散度为0

$\nabla \cdot ( \nabla \times \vec{A}) =0$

复合标量函数

$\nabla f( u) =( \nabla u)\frac{df}{du}$

复合矢量函数

$\nabla \cdot \vec{A}( u) =( \nabla u) \cdot \frac{d\vec{A}}{du}$

Delta 函数

$\nabla ^{2}\frac{1}{r} =-4\pi \delta ( r)$

### 几个复合函数运算恒等式

算子的分部求导公式

$\nabla ( uv) =v\nabla u+u\nabla v$

分部散度公式

$\nabla \cdot ( u\vec{A}) =( \nabla u) \cdot \vec{A} +u( \nabla \cdot \vec{A})$

分部旋度公式

$\nabla \times ( u\vec{A}) =( \nabla u) \times \vec{A} +u( \nabla \times \vec{A})$

两个向量的旋度的分部散度公式

$\nabla \cdot (\vec{A} \times \vec{B}) =( \nabla \times \vec{A}) \cdot \vec{B} +\vec{A} \cdot ( \nabla \times \vec{B})$

两个向量的旋度的分部旋度公式

$\nabla \times (\vec{A} \times \vec{B}) =( \nabla \times \vec{A}) \times \vec{B} +\vec{A} \times ( \nabla \times \vec{B})$

二阶旋度恒等式

$\displaystyle \nabla \times ( \nabla \times \vec{A}) =\nabla ( \nabla \cdot \vec{A}) -\nabla ^{2}\vec{A}$

**Mathematica 验证**

读者们可以尝试用 Mathematica 验证

```mathematica
(*Part 2*)
(*\[Del]\[Times](\[Del]u)=0*)
Curl[Grad[u[x,y,z],{x,y,z}],{x,y,z}]

(*\[Del](\[Del]\[Times]A)=0*)
A={Ax[x,y,z],Ay[x,y,z],Az[x,y,z]}
Div[Curl[A,{x,y,z}],{x,y,z}]

(*\[Del](uv)=v\[Del](u)+u\[Del](v)*)
lhs=Grad[u[x,y,z]*v[x,y,z],{x,y,z}]
rhs=Grad[u[x,y,z],{x,y,z}]*v[x,y,z]+u[x,y,z]*Grad[v[x,y,z],{x,y,z}]

(*\[Del](uA)=(\[Del]u).A+u(\[Del].A)*)
lhs=Div[u[x,y,z]*A,{x,y,z}]
rhs=Grad[u[x,y,z],{x,y,z}].A+u[x,y,z]*Div[A,{x,y,z}]
Simplify[lhs-rhs]

(*\[Del]\[Times](uA)=(\[Del]u)\[Times]A+u(\[Del]\[Times]A)*)
lhs3=Curl[u[x,y,z]*A,{x,y,z}]
rhs3=Cross[Grad[u[x,y,z],{x,y,z}],A]+u[x,y,z]*Curl[A,{x,y,z}]
Simplify[lhs3-rhs3]
```

结果参见

https://www.wolframcloud.com/obj/yulinshiapp/Published/09-hamilton-operations.nb

### 二阶旋度恒等式证明

其中“二阶旋度恒等式”可以用在求解麦克斯韦方程组中，从旋度方程推出波动方程。所以我们多费笔墨写出证明过程。

$\displaystyle \nabla \times ( \nabla \times \vec{A}) =\nabla ( \nabla \cdot \vec{A}) -\nabla ^{2}\vec{A}$

**证明**

展开二阶旋度恒等式第一项

$\displaystyle \nabla \times ( \nabla \times \vec{A}) =\begin{vmatrix}
\vec{i} & \vec{j} & \vec{k}\\
\frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z}\\
\frac{\partial A_{z}}{\partial y} -\frac{\partial A_{y}}{\partial z} & \frac{\partial A_{x}}{\partial z} -\frac{\partial A_{z}}{\partial x} & \frac{\partial A_{y}}{\partial x} -\frac{\partial A_{x}}{\partial y}
\end{vmatrix}$

我们先只研究其 x 方向分量

$\displaystyle \begin{vmatrix}
\frac{\partial }{\partial y} & \frac{\partial }{\partial z}\\
\frac{\partial A_{x}}{\partial z} -\frac{\partial A_{z}}{\partial x} & \frac{\partial A_{y}}{\partial x} -\frac{\partial A_{x}}{\partial y}
\end{vmatrix} =\frac{\partial }{\partial y}\left(\frac{\partial A_{y}}{\partial x} -\frac{\partial A_{x}}{\partial y}\right) -\frac{\partial }{\partial z}\left(\frac{\partial A_{x}}{\partial z} -\frac{\partial A_{z}}{\partial x}\right)$

简化

$\displaystyle \frac{\partial }{\partial y}\frac{\partial A_{y}}{\partial x} -\frac{\partial }{\partial y}\frac{\partial A_{x}}{\partial y} -\frac{\partial }{\partial z}\frac{\partial A_{x}}{\partial z} +\frac{\partial }{\partial z}\frac{\partial A_{z}}{\partial x}$

展开二阶旋度恒等式第二项

$\displaystyle \nabla ( \nabla \cdot \vec{A}) =\nabla \left(\frac{\partial A_{x}}{\partial x} +\frac{\partial A_{y}}{\partial y} +\frac{\partial A_{z}}{\partial z}\right)$

我们先只研究其 x 方向分量

$\displaystyle \frac{\partial }{\partial x}\left(\frac{\partial A_{x}}{\partial x} +\frac{\partial A_{y}}{\partial y} +\frac{\partial A_{z}}{\partial z}\right) =\frac{\partial }{\partial x}\frac{\partial A_{x}}{\partial x} +\frac{\partial }{\partial x}\frac{\partial A_{y}}{\partial y} +\frac{\partial }{\partial x}\frac{\partial A_{z}}{\partial z}$

展开二阶旋度恒等式第三项

$\displaystyle \nabla ^{2}\vec{A} =\left(\frac{\partial ^{2}}{\partial x^{2}} +\frac{\partial ^{2}}{\partial y^{2}} +\frac{\partial ^{2}}{\partial z^{2}}\right)\vec{A}$

我们先只研究其 x 方向分量

$\displaystyle \left(\frac{\partial ^{2}}{\partial x^{2}} +\frac{\partial ^{2}}{\partial y^{2}} +\frac{\partial ^{2}}{\partial z^{2}}\right) A_{x} =\frac{\partial ^{2} A_{x}}{\partial x^{2}} +\frac{\partial ^{2} A_{x}}{\partial y^{2}} +\frac{\partial ^{2} A_{x}}{\partial z^{2}}$

恒等式右侧求和

$\displaystyle \left( \nabla ( \nabla \cdot \vec{A}) -\nabla ^{2}\vec{A}\right)_{x} =\frac{\partial }{\partial x}\frac{\partial A_{x}}{\partial x} +\frac{\partial }{\partial x}\frac{\partial A_{y}}{\partial y} +\frac{\partial }{\partial x}\frac{\partial A_{z}}{\partial z} -\left(\frac{\partial ^{2} A_{x}}{\partial x^{2}} +\frac{\partial ^{2} A_{x}}{\partial y^{2}} +\frac{\partial ^{2} A_{x}}{\partial z^{2}}\right)$

化简为

$\displaystyle \frac{\partial }{\partial x}\frac{\partial A_{y}}{\partial y} +\frac{\partial }{\partial x}\frac{\partial A_{z}}{\partial z} -\left(\frac{\partial ^{2} A_{x}}{\partial y^{2}} +\frac{\partial ^{2} A_{x}}{\partial z^{2}}\right)$

可见，恒等式 x 方向左右相等。

同理，可以验证恒等式 y, z 方向左右也相等。

得证。

**Mathematica 验证**

也可以用 Mathematica 代码完整地求证三个方向的恒等式

```mathematica
(*Part 1: prove the second-order rotation equation*)
(*\[Del]\[Times]\[Del]\[Times]=\[Del](\[Del].)-\[Del].\[Del]*)

(*Define the vector as a function of x,y,z*)
A={Ax[x,y,z],Ay[x,y,z],Az[x,y,z]}
(*Expand the first term in the equation*)
lhs=Curl[Curl[A,{x,y,z}],{x,y,z}]

(*Expand the second term in the equation*)
rhs1=Grad[Div[A,{x,y,z}],{x,y,z}]

(*Expand the third term in the equation*)
rhs2=Div[Grad[A,{x,y,z}],{x,y,z}]

lhs-rhs1+rhs2
(*The zeros proved the second-order rotation equation*)
```

结果参见

https://www.wolframcloud.com/obj/yulinshiapp/Published/09-hamilton-operations.nb

### 有旋无源场

