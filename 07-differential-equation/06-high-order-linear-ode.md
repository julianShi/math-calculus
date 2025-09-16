## 物理例子

举一个二阶线性方程的例子

串联电路的振荡方程

$\displaystyle E-L\frac{di}{dt} -\frac{q}{C} -Ri=E_{0}\sin \omega t$

其中，待求电流 $\displaystyle i( t)$ 是时间的函数

给定初值 $\displaystyle i( 0)$，能够唯一地确定 $\displaystyle i( t)$

## 二阶齐次线性方程

先来讨论二阶齐次线性方程

$\displaystyle y''+P( x) y'+Q( x) y=0$

**定理一**：如果存在两个函数 $\displaystyle y_{1}( x) ,\ y_{2}( x)$ 是上述方程的两个解，那么

$\displaystyle y( x) =C_{1} y_{1}( x) +C_{2} y_{2}( x)$

也是方程的解。

证明：把“解”代入原方程左侧

$\displaystyle [ C_{1} y_{1} ''( x) +C_{2} y_{2} ''( x)] +P( x)[ C_{1} y_{1} '( x) +C_{2} y_{2} '( x)] +Q( x)[ C_{1} y_{1}( x) +C_{2} y_{2}( x)]$

合并同类函数

$\displaystyle C_{1}( y_{1} ''+P( x) y_{1} '+Q( x) y_{1}) +C_{2}( y_{2} ''+P( x) y_{2} '+Q( x) y_{2}) =0$

证t毕

## 线性无关函数

线性无关函数，与线性相关函数的概念

**定义**：若存在非零的系数 $\displaystyle k_{i}$，使得

$\displaystyle k_{1} y_{1} +k_{2} y_{2} +...+k_{n} y_{n} =0$

那么 $\displaystyle y_{1} ,y_{2} ,...,y_{n}$ 函数系线性相关

线性无关函数例子

$\displaystyle 1,\cos x,\ \sin x$

因为 $\displaystyle k_{1} =k_{2} =k_{3} =0$ 是

$\displaystyle k_{1} +k_{2}\cos x+k_{3}\sin x=0$

的唯一解

线性相关函数例子

$\displaystyle 1,\ \cos^{2} x,\ \sin^{2} x$

因为存在非零解

$\displaystyle k_{1} =-1，k_{2} =k_{3} =1$

使得

$\displaystyle -1+\cos^{2} x+\sin^{2} x=0$

## 二阶齐次线性方程通解

**定理二**：若二阶齐次线性方程存在两个线性无关的解 $\displaystyle y_{1} ,y_{2}$, 那么

$\displaystyle y=C_{1} y_{1} +C_{2} y_{2}$

是方程的通解，其中 $\displaystyle C_{1} ,C_{2}$是任意常数。



推广到n维：

n阶齐次线性方程

$\displaystyle y^{( n)} +a_{1}( x) y^{( n-1)} +...+a_{n-1}( x) y^{( 1)} +a_{n}( x) y=0$

的通解是

$\displaystyle y=C_{1} y_{1} +C_{2} y_{2} +...+C_{n} y_{n}$

## 二阶齐次线性方程特解

**定理三**：设 $\displaystyle y^{*}( x)$ 是二阶非齐次线性方程

$\displaystyle y''+P( x) y'+Q( x) y=f( x)$

的一个特解，那么

$\displaystyle y=C_{1} y_{1} +C_{2} y_{2} +y^{*}( x)$

是方程的通解



**定理四**：二阶非齐次线性方程的特解定理可以推广到高阶。

至此，介绍了这类方程的几个性质。其中，特殊的常系数方程，有解析解，请阅读下一节。