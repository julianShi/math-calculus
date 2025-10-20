# 多元函数微分

和一元函数类似，我们定义二元函数

$F(x,y)$

的微分为极限的形式

$f_{x}( x,y) =\lim _{\Delta x\rightarrow 0}\frac{f( x+\Delta x,y) -f( x,y)}{\Delta x}$

则二元函数的微分表示为

$df( x,y) =f_{x}( x,y) dx+f_{y}( x,y) dy$

## 微分几何意义

微分表达式的几何意义表示为光滑曲面的切平面

$z=f_x x + f_y y + C$

则

$0=f_x x + f_y y + C$ 

表示一簇平行的等值线。平面的这一簇等值线有相同的法向量。

$(f_x,f_y)$

法向量的几何意义是最大坡度方向。

## 方向导数

对于方向 $l$, 用 $\alpha, \beta$ 分别表示其与 $x,y$ 轴的夹角，那么

$dz=f_{x}\cos \alpha dl +f_{y}\cos \beta dl$

是方向微分

方向导数可以定义为

$f_{l}( x,y) =\lim _{\Delta l\rightarrow 0}\frac{f( x+\cos \alpha \Delta l,y+\cos \beta \Delta l) -f( x,y)}{\Delta l}$

举一个反例

$z(r,\theta)=r\cos(4\theta)$

在 $r=0$ 处，其方向导数存在，为

$z_r(r,\theta) = \cos(4\theta)$

但是因为没有相同的切平面。所以不可微。

点击链接，观察图像

https://www.desmos.com/3d/5pvegulqof

举一个正例

$z(r,\theta)=r^2\cos(4\theta)$

在 $r=0$ 处，其方向导数存在，为

$z_r(r,\theta) = r\cos(4\theta)$

可微分。

总结来说，这4个命题的充分必要关系如图

```mermaid
flowchart LR
    continous[函数连续]
    derivative[函数可导]
    differential[函数可微]
    derivative_continous[偏导数连续]
    derivative_continous --> differential
    continous x--x derivative
    differential --> continous
    differential --> derivative
```

## 方程组几何意义

隐式方程 

$f(x,y,z)=0$

表示三维空间中的曲面，则方程组

$f(x,y,z)=0,g(x,y,z)=0$

表示两个曲面的交线。

例题：圆锥曲线。请读者回顾高中所学的3类圆锥曲线。圆锥面和不同斜率的平面的交线，就是这3类圆锥曲线的一种。请参加3D动画

https://www.desmos.com/3d/hx6atbta7j

## 平面极坐标

**在平面极坐标下 $\nabla$ 算子的形式推导**

在平面直角坐标系中， $\nabla$ 算子表示为 $\nabla=\hat{i}\frac{\partial}{\partial x}+\hat{j}\frac{\partial}{\partial y}$ 。

从直角坐标 $(x,y)$ 到极坐标 $(r,\theta)$ 的变换关系为 $x = r\cos\theta$ ， $y = r\sin\theta$ 。

根据链式法则，我们可以求出 $\frac{\partial}{\partial r}$ 和 $\frac{\partial}{\partial \theta}$ 与 $\frac{\partial}{\partial x}$ 和 $\frac{\partial}{\partial y}$ 的关系。

- 首先求 $\frac{\partial}{\partial r}$ ：
  -  $\frac{\partial}{\partial r}=\frac{\partial x}{\partial r}\frac{\partial}{\partial x}+\frac{\partial y}{\partial r}\frac{\partial}{\partial y}=\cos\theta\frac{\partial}{\partial x}+\sin\theta\frac{\partial}{\partial y}$ 。
- 然后求 $\frac{\partial}{\partial \theta}$ ：
  -  $\frac{\partial}{\partial \theta}=\frac{\partial x}{\partial \theta}\frac{\partial}{\partial x}+\frac{\partial y}{\partial \theta}\frac{\partial}{\partial y}=-r\sin\theta\frac{\partial}{\partial x}+r\cos\theta\frac{\partial}{\partial y}$ 。
- 解上述关于 $\frac{\partial}{\partial x}$ 和 $\frac{\partial}{\partial y}$ 的方程组可得：
  -  $\frac{\partial}{\partial x}=\cos\theta\frac{\partial}{\partial r}-\frac{\sin\theta}{r}\frac{\partial}{\partial \theta}$ 。
  -  $\frac{\partial}{\partial y}=\sin\theta\frac{\partial}{\partial r}+\frac{\cos\theta}{r}\frac{\partial}{\partial \theta}$ 。

- 在极坐标中，单位向量 $\hat{r}=\cos\theta\hat{i}+\sin\theta\hat{j}$ ， $\hat{\theta}=-\sin\theta\hat{i}+\cos\theta\hat{j}$ 。
- 那么 $\nabla$ 算子在极坐标下的形式为：
  -  $\nabla=\hat{r}\frac{\partial}{\partial r}+\frac{\hat{\theta}}{r}\frac{\partial}{\partial \theta}$ 。

