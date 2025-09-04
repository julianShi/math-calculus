## 泰勒公式

泰勒公式实际上是函数的幂级数

$$
f( x) =f( x_{0}) +f'( x_{0})( x-x_{0}) +\frac{f''( x_{0})}{2!}( x-x_{0})^{2} +...=\sum _{n=0}^{\infty }\frac{f^{( n)}( x_{0})}{n!}( x-x_{0})^{n}
$$


回顾几个值得背诵的泰勒公式

$$
e^x = x - \frac{x^{2}}{2} + \frac{x^{3}}{3} - \frac{x^{4}}{4} + \frac{x^{5}}{5} + O\left(x^{6}\right)
$$

$$
\sin(x) = x - \frac{x^{3}}{6} + \frac{x^{5}}{120} + O\left(x^{6}\right)
$$

$$
\cos(x) = 1 - \frac{x^{2}}{2} + \frac{x^{4}}{24} + O\left(x^{6}\right)
$$

$$
e^{ix} = 1 + i x - \frac{x^{2}}{2} - \frac{i x^{3}}{6} + \frac{x^{4}}{24} + \frac{i x^{5}}{120} + O\left(x^{6}\right)
$$

可见，

$$
e^{ix} =\cos x+i\sin x
$$
