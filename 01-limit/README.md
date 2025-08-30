高等数学的第一章介绍了集合、函数、极限等概念，作为微积分这一门课程的基础。

这一章所需要的计算过程不多，更多是作为证明而存在，适合 [Lean4](https://lean-lang.org/) 这门编程语言。不适合 SymPy，所以按下不表。

### 值得背诵的几种函数
由基本初等函数（幂、指数、对数、三角、反），经过有限次的加减乘除和复合而得的函数，就是初等函数。

一个值得研究的不连续函数
$\sin(1/x)$
可以在 https://www.desmos.com/calculator 上面画出其形状。
可见其在 $x=0$ 处不连续。

### 值得背诵的几个重要极限

$\displaystyle \lim _{x\rightarrow 0}\frac{\sin x}{x} =1$

$\displaystyle \lim _{x\rightarrow \infty }( 1+1/x)^{x} =e$


### 洛必达 L'hopital 法则

对于可导的函数 $\displaystyle f( x) ,g( x)$，若 $\displaystyle f( x_{0}) =g( x_{0}) =0$，则有

$\displaystyle \lim _{x\rightarrow x_{0}}\frac{f( x)}{g( x)} =\lim _{x\rightarrow x_{0}}\frac{f'( x)}{g'( x)}$

这个法则可以在介绍了幂级数之后，简单证明。按下不表。