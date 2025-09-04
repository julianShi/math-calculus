## 函数的求导法则

**函数的和差积商**

如果函数 $u( x) ,\ v( x)$ 在 x 点都有导数，那么它们的和差积商在 x 点也有导数

$$
u( x) +v( x) =u'( x) +v'( x)
$$

$$
u( x) v( x) =u'( x) v( x) +u( x) v'( x)
$$

$$
\left(\frac{u( x)}{v( x)}\right) '=\frac{u'( x) v( x) -u( x) v'( x)}{v^{2}( x)} ,v( x) \neq 0
$$

**反函数**

$$
\left[ f^{-1}( x)\right] '=\frac{1}{f'( y)}
$$

**复合函数**

对于函数 $z( y) ,y( x)$, 若他们导数在 x 点存在，则

$$
z'( x) =z'( y) y'( x)
$$



## 高阶导数

$$
[\sin x]^{( n)} =\sin( x+\pi n/2)
$$



## 隐函数的导数

假设存在

$$
x( t) ,y( t)
$$

且他们的导数存在，则

$$
\frac{dy}{dx} =\frac{dy/dt}{dx/dt} =\frac{y'( t)}{x'( t)}
$$

$$
\frac{d^{2} y}{dx^{2}} =\frac{d}{dx}\frac{dy}{dx} =\frac{d}{dt}\left(\frac{y'( t)}{x'( t)}\right)\frac{dt}{dx} =\frac{y''( t)x'( t) -y'( t) x''( t)}{x^{\prime 3}( t)}
$$

## 弧长微元

### 直角坐标表示

$$
ds = \sqrt{dx^2+dy^2} = \sqrt{dx^2+y'^2dx^2} = \sqrt{1+y'^2} dx
$$

### 极坐标表示

在极坐标中

$$
x=r(\theta)\cos(\theta), y=r(\theta)\sin(\theta)
$$

$$
dx=r'd\theta\cos(\theta) - r\sin(\theta)d\theta, dy=r'd\theta\sin(\theta) + r\cos(\theta)d\theta
$$

所以

$$
ds=\sqrt{( r'd\theta \cos (\theta )-r\sin (\theta )d\theta )^{2} +( r'd\theta \sin (\theta )+r\cos (\theta )d\theta )^{2}}
$$

化简

$$
ds=\sqrt{r^{2} +r^{\prime 2}} d\theta
$$