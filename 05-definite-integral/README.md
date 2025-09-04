# 定积分

定积分有许多有意思的性质，比如说 函数可积性，中值定理，收敛判定，都是考研考点。但是因为 SymPy 擅长符号计算，不擅长定理证明，所以按下不表。



## 变上限积分

用 $\displaystyle F( x) ,f( x)$ 分别表示原函数 及其导数，

$\displaystyle f( x) =\frac{dF( x)}{dx}$

将其写成积分形式，需要使用变上线积分

$\displaystyle F( x) =\int _{a}^{x} f( t) dt$

变上限积分常常在无法求出原函数 $\displaystyle F( x)$ 的时候，用被积函数 $\displaystyle f( t)$ 间接表示 $\displaystyle F( x)$



## 定积分性质

对于奇函数，

$\displaystyle f( -x) =-f( x) ,x\in [ -a,a]$

有

$\displaystyle \int _{-a}^{a} f( x) dx=0$

对于偶函数，

$\displaystyle f( -x) =f( x) ,x\in [ -a,a]$

有

$\displaystyle \int _{-a}^{a} f( x) dx=2\int _{0}^{a} f( x) dx$

对于周期函数

$\displaystyle f( x+T) =f( x)$

有

$\displaystyle \int _{a}^{a+nT} f( x) dx=n\int _{0}^{T} f( x) dx,n\in \mathbb{Z}$

定积分的分步积分法

$\displaystyle \int _{a}^{b} uv'dx=uv|_{a}^{b} -\int _{a}^{b} u'vdx$



