对于有非$y^{(n)}$ 项的高阶常系数非齐次线性微分方程

$$
y^{( n)} +a_{1} y^{( n-1)} +...+a_{n-1} y^{( 1)} +a_{n} y=f(x)
$$


我们推导其通解。

### 特征方程无重根

可参照上一节，将高阶方程转化为一阶方程组

$$
\mathbf{y} '=\mathbf{Ay} +\mathbf{f}(x)
$$


其中

$$
\mathbf{f}(x) =( 0,0,...,0,f( x))^{T}
$$


可将常系数矩阵 $\boldsymbol{A}$ 对角化，

$$
\mathbf{A} = \mathbf{P}^{-1}\mathbf{\Lambda P}
$$


则原方程组为

$$
\mathbf{Py} '=\Lambda \mathbf{Py} +\mathbf{Pf}(x)
$$


即求一阶常系数非齐次线性微分方程组

$$
\mathbf{z} '=\mathbf{\Lambda z} +\mathbf{b}( x)
$$


其中

$$
\mathbf{z} =\mathbf{Py} ,\mathbf{b}( x) =\mathbf{Pf}( x)
$$


其中第 i 项有

$$
z_{i} '=\lambda _{i} z_{i} +b_{i}( x)
$$


其通解为

$$
z_{i} =e^{\int \lambda _{i} dx}\left(\int b_{i}( x) e^{-\int \lambda _{i} dx} dx+C_{i}\right)
$$


求出 $\mathbf{z}$ 之后，再通过线性变换得到

$$
\mathbf{y} =\mathbf{P}^{-1}\mathbf{z} 
$$


### 特征方程有重根与非重根

还是拿上一节4阶齐次线性微分方程举例。但是这次交换换元顺序，得到

$$
\displaystyle \zeta _{1} =y' -\lambda y
$$


$$
\displaystyle \zeta _{2} =\zeta _{1} ' -\lambda \zeta _{1}
$$


$$
\displaystyle z_{1} =\zeta _{2} ' -\lambda _{1} \zeta _{2}
$$


$$
\displaystyle z_{1} ' -\lambda _{2} z_{1} =f(x)
$$


$$
\displaystyle \begin{pmatrix}
y'\\
\zeta _{1} '\\
\zeta _{2} '\\
z_{1} '
\end{pmatrix} =\begin{pmatrix}
\lambda  & 1 &  & \\
 & \lambda  & 1 & \\
 &  & \lambda _{1} & 1\\
 &  &  & \lambda _{2}
\end{pmatrix}\begin{pmatrix}
y\\
\zeta _{1}\\
\zeta _{2}\\
z_{1}
\end{pmatrix}
$$


分解成上下两块

$$
\displaystyle \begin{pmatrix}
y'\\
z'
\end{pmatrix} =\begin{pmatrix}
\mathbf{B} & \mathbf{C}\\
0 & \mathbf{D}
\end{pmatrix}\begin{pmatrix}
y\\
z
\end{pmatrix} +\begin{pmatrix}
\mathbf{0}\\
\mathbf{f}( x)
\end{pmatrix}
$$


即

$$
\displaystyle \mathbf{y} '=\mathbf{By} +\mathbf{Cz}
$$


$$
\mathbf{z} '=\mathbf{Dz} +\mathbf{f}( x)
$$


其中，$\mathbf{B}$ 不可对角化的上三角矩阵，$\mathbf{D}$ 可对角化。

根据 "**特征方程无重根** " 中介绍的方法，可求得通解 $\mathbf{z}( x)$


进而求解

$$
\displaystyle \mathbf{y} '=\mathbf{By} +\mathbf{g}(x)
$$


其中 

$$
\mathbf{g}(x)=\mathbf{Cz}(x)
$$


因为 $\mathbf{B}$ 不可对角化的上三角矩阵，所以可以展开成为标量形式，从下到上依次求解一阶常系数非齐次线性微分方程，得到通解 $\mathbf{y}(x)$。

