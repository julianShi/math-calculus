# 偏微分方程

大学《高等数学》介绍了多元函数微积分知识。《偏微分方程》单独作为一门课程开设。

## 二阶线性偏微分方程

为了方便学生体验，教材先教授了求解几个经典的二阶偏微分方程。

之所以先介绍它们，是因为它们属于椭圆型，双曲型或者抛物型的PDE。有比较容易求解的解析解。

| 偏微分方程   | 低阶公式                                                     | 解                                                           |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 波动方程     | $\frac{\partial^{2}u}{\partial t^{2}} = c^{2}\frac{\partial^{2}u}{\partial x^{2}}$ | $u(x,t)=f(x + ct)+g(x - ct)$                                 |
| 热传导方程   | $\frac{\partial u}{\partial t}=\alpha\frac{\partial^{2}u}{\partial x^{2}}$ | $u(x,t)=\sum_{n = 1}^{\infty}b_{n}\sin(\frac{n\pi x}{L})e^{-\alpha(\frac{n\pi}{L})^{2}t}$ |
| 拉普拉斯方程 | $\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}} = 0$ | $u(x,y)=\sum_{n = 1}^{\infty}(A_{n}\cosh(\frac{n\pi y}{a})+B_{n}\sinh(\frac{n\pi y}{a}))\sin(\frac{n\pi x}{a})$ |
| 泊松方程     | $\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}}=\rho(x,y)$ | $u(x,y)=\iint_{D}G(x,y;x_{0},y_{0})\rho(x_{0},y_{0})dx_{0}dy_{0}$ |

**波动方程（Wave Equation）**

- **方程形式**：
  - 一维波动方程： $\frac{\partial^{2}u}{\partial t^{2}} = c^{2}\frac{\partial^{2}u}{\partial x^{2}}$ ，其中 $u = u(x,t)$ 表示在位置 $x$ 和时间 $t$ 处的物理量（如弦的位移）， $c$ 是波速。
  - 三维波动方程： $\frac{\partial^{2}u}{\partial t^{2}}=c^{2}(\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}}+\frac{\partial^{2}u}{\partial z^{2}})$ 。
- **通解形式**：
  - 一维波动方程的达朗贝尔（d'Alembert）解为 $u(x,t)=f(x + ct)+g(x - ct)$ ，其中 $f$ 和 $g$ 是任意两次可微函数。这表示波动方程的解由两个行波组成，一个向右传播（ $f(x + ct)$ ），一个向左传播（ $g(x - ct)$ ）。
  - 对于三维波动方程，在一些特殊条件下，如初始条件和边界条件给定，可通过分离变量法等方法求解。例如，在球对称情况下，可转化为常微分方程求解。

**热传导方程（Heat Equation）**

- **方程形式**：
  - 一维热传导方程： $\frac{\partial u}{\partial t}=\alpha\frac{\partial^{2}u}{\partial x^{2}}$ ，其中 $u = u(x,t)$ 表示温度， $\alpha$ 是热扩散系数。
  - 三维热传导方程： $\frac{\partial u}{\partial t}=\alpha(\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}}+\frac{\partial^{2}u}{\partial z^{2}})$ 。
- **解的形式**：
  - 对于一维热传导方程，当给定初始条件 $u(x,0)=\varphi(x)$ 和边界条件（如 $u(0,t)=u(L,t)=0$ ）时，利用分离变量法，设 $u(x,t)=X(x)T(t)$ ，代入方程得到两个常微分方程。求解后可得解的形式为 $u(x,t)=\sum_{n = 1}^{\infty}b_{n}\sin(\frac{n\pi x}{L})e^{-\alpha(\frac{n\pi}{L})^{2}t}$ ，其中 $b_{n}=\frac{2}{L}\int_{0}^{L}\varphi(x)\sin(\frac{n\pi x}{L})dx$ 。

**拉普拉斯方程（Laplace Equation）**

- **方程形式**：
  - 二维拉普拉斯方程： $\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}} = 0$ ， $u = u(x,y)$ 。常用于描述稳态的物理现象，如静电场中的电势、稳态温度分布等。
  - 三维拉普拉斯方程： $\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}}+\frac{\partial^{2}u}{\partial z^{2}} = 0$ 。
- **解的形式**：
  - 在二维区域 $D$ 上，若 $D$ 是矩形区域 $0\leq x\leq a$ ， $0\leq y\leq b$ ，且给定边界条件（如 $u(x,0)=f_{1}(x)$ ， $u(x,b)=f_{2}(x)$ ， $u(0,y)=g_{1}(y)$ ， $u(a,y)=g_{2}(y)$ ），使用分离变量法设 $u(x,y)=X(x)Y(y)$ ，代入方程得到两个常微分方程。求解后可得 $u(x,y)=\sum_{n = 1}^{\infty}(A_{n}\cosh(\frac{n\pi y}{a})+B_{n}\sinh(\frac{n\pi y}{a}))\sin(\frac{n\pi x}{a})$ ，系数 $A_{n}$ 和 $B_{n}$ 由边界条件确定。

**泊松方程（Poisson Equation）**

- **方程形式**：
  - 二维泊松方程： $\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}}=\rho(x,y)$ ，其中 $\rho(x,y)$ 是已知函数，可看作是某种源项。例如在静电学中， $\rho$ 表示电荷密度， $u$ 表示电势。
  - 三维泊松方程： $\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}}+\frac{\partial^{2}u}{\partial z^{2}}=\rho(x,y,z)$ 。
- **解的形式**：
  - 一般通过格林函数法求解。对于二维泊松方程，设 $G(x,y;x_{0},y_{0})$ 是格林函数，满足 $\frac{\partial^{2}G}{\partial x^{2}}+\frac{\partial^{2}G}{\partial y^{2}}=\delta(x - x_{0})\delta(y - y_{0})$ （ $\delta$ 是狄拉克函数），则解 $u(x,y)=\iint_{D}G(x,y;x_{0},y_{0})\rho(x_{0},y_{0})dx_{0}dy_{0}$ ，其中积分区域 $D$ 是问题所在的二维区域。

这些典型的偏微分方程在物理学、工程学、数学等多个领域都有广泛的应用，不同的求解方法适用于不同的边界条件和初始条件。 

## 方程通解

求解偏微分方程能得到系统的通解。

然后根据狄利克雷边界条件，可以得到稳态解。

或者根据初始条件，得到初值问题的唯一解。

## 边界条件

| 边界   | 名字                  | 已知条件         |
| ------ | --------------------- | ---------------- |
| 第一类 | Dirichlet（狄利克雷） | 边界值           |
| 第二类 | Neumann（诺伊曼）     | 边界值的法向微商 |
| 第三类 | Robin（罗宾）         | 线性混合         |

