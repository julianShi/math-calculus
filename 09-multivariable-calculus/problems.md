# 例题

## 极坐标形式梯度算子


假设我们有一个标量函数 $f(r,\theta)=r\cos\theta$ ，我们分别用直角坐标和极坐标形式的 $\nabla$ 算子对其作用并验证结果。

- **直角坐标形式**：
  - 先将 $f$ 转换为直角坐标形式 $f(x,y)= \sqrt{x^{2}+y^{2}}\frac{x}{\sqrt{x^{2}+y^{2}}}=x$ 。
  - $\nabla f=\hat{i}\frac{\partial f}{\partial x}+\hat{j}\frac{\partial f}{\partial y}=\hat{i}$ 。
- **极坐标形式**：
  -  $f(r,\theta)=r\cos\theta$ 。
  -  $\nabla f=\hat{r}\frac{\partial f}{\partial r}+\frac{\hat{\theta}}{r}\frac{\partial f}{\partial \theta}$ 。
  -  $\frac{\partial f}{\partial r}=\cos\theta$ ， $\frac{\partial f}{\partial \theta}=-r\sin\theta$ 。
  -  所以 $\nabla f=\hat{r}\cos\theta+\frac{\hat{\theta}}{r}(-r\sin\theta)=\hat{r}\cos\theta-\hat{\theta}\sin\theta$ 。
  -  转换回直角坐标： $(\cos\theta\hat{i}+\sin\theta\hat{j})\cos\theta-(-\sin\theta\hat{i}+\cos\theta\hat{j})\sin\theta=\hat{i}(\cos^{2}\theta+\sin^{2}\theta)=\hat{i}$ ，与直角坐标形式结果一致。

对于向量函数的 $\nabla$ 运算（如散度 $\nabla\cdot\vec{F}$ 和旋度 $\nabla\times\vec{F}$ ），在极坐标下也有相应的公式：

 - 设向量函数 $\vec{F}=F_{r}\hat{r}+F_{\theta}\hat{\theta}$ ，散度 $\nabla\cdot\vec{F}=\frac{1}{r}\frac{\partial (rF_{r})}{\partial r}+\frac{1}{r}\frac{\partial F_{\theta}}{\partial \theta}$ 。
 - 旋度 $\nabla\times\vec{F}=(\frac{1}{r}\frac{\partial F_{r}}{\partial \theta}-\frac{\partial F_{\theta}}{\partial r})\hat{z}$ （在二维平面极坐标扩展到三维柱坐标时， $\hat{z}$ 方向分量才有旋度，这里仅考虑二维平面极坐标相关部分）。 







