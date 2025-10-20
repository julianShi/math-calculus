# 高等数学笔记 📚

一个综合性的交互式微积分学习仓库，将理论知识与SymPy实践相结合。本仓库提供Markdown格式的数学基础理论和可执行的Jupyter笔记本，用于微积分概念的实践探索。

## 🌟 特色功能

- **双语内容**：数学概念的中英文双语解释
- **交互式学习**：配合SymPy代码的Jupyter笔记本，用于计算探索
- **全面覆盖**：按照标准微积分课程组织的12个章节
- **实践示例**：真实应用场景和可视化演示
- **开源项目**：社区驱动开发，欢迎贡献

## 🎯 适用读者

- **高等数学备考**：考研和期末考试复习参考
- **SymPy学习者**：学习强大、免费、开源且持续维护的SymPy软件，辅助科研工作
- **编程数学爱好者**：比SymPy官方文档更浅显易懂的中文教程
- **实践学习者**：开箱即用的Jupyter Notebook例题和演示
- **双语学习者**：中英文对照的数学内容

## 📖 课程目录

基于同济大学《高等数学》第3版教材：

1. **函数与极限** (Functions and Limits)
2. **导数与微分** (Derivatives and Differentials)
3. **微分中值定理与导数的应用** (Mean Value Theorem and Applications)
4. **不定积分** (Indefinite Integrals)
5. **定积分** (Definite Integrals)
6. **定积分的应用** (Applications of Definite Integrals)
7. **微分方程** (Differential Equations)
8. **向量代数与空间解析几何** (Vector Algebra and Analytic Geometry)
9. **多元函数微分法及其应用** (Multivariable Calculus)
10. **重积分** (Multiple Integrals)
11. **曲线积分与曲面积分** (Line and Surface Integrals)
12. **无穷级数** (Infinite Series)

## 🚀 快速开始

### 在线使用（推荐）

- **启动Binder**: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/julianShi/math-calculus/HEAD)
- **启动JupyterLab**: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/julianShi/math-calculus/HEAD?urlpath=lab)

### 本地安装

#### 环境要求

- Python 3.8 或更高版本
- Git

#### 安装步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/julianShi/math-calculus.git
   cd math-calculus
   ```

2. **配置虚拟环境**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows用户: .venv\Scripts\activate
   ```

3. **安装依赖**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **启动 Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

#### 替代方案：使用Conda

```bash
conda env create -f environment.yml
conda activate math-calculus
jupyter notebook
```

### 使用指南

导航到任意章节文件夹（例如 `12-infinite-series/`）并探索：

- **`.md` 文件**：理论背景和数学基础
- **`.ipynb` 文件**：交互式代码示例和计算

推荐学习流程：
1. 阅读 `07-fourier-series.md` 了解理论基础
2. 打开 `07-fourier-series.ipynb` 进行实践练习
3. 运行代码单元查看SymPy计算过程

## 📁 仓库结构

```
math-calculus/
├── README.md                    # 英文说明文档
├── README-zh.md                 # 中文说明文档（本文件）
├── CONTRIBUTING.md             # 贡献指南
├── requirements.txt            # Python依赖
├── 01-functions-limits/        # 第1章（计划中）
├── 02-derivatives/             # 第2章（计划中）
├── ...                         # 第3-11章（计划中）
└── 12-infinite-series/         # 第12章（已实现）
    ├── README-zh.md            # 章节概述
    ├── 07-fourier-series.md    # 傅里叶级数理论（中文）
    ├── 07-fourier-series.ipynb # 傅里叶级数笔记本（英文）
    └── ...                     # 其他小节
```

## 🛠️ 技术栈

- **[SymPy](https://www.sympy.org/)**：Python符号数学库
- **[Jupyter](https://jupyter.org/)**：交互式计算环境
- **[NumPy](https://numpy.org/)**：数值计算
- **[Matplotlib](https://matplotlib.org/)**：数据可视化
- **[SciPy](https://scipy.org/)**：科学计算

## 🤝 参与贡献

我们欢迎社区贡献！本仓库设计为协作项目，提供以下贡献机会：

- 实现新章节（第1-11章）
- 为现有章节添加更多小节
- 改进现有内容
- 翻译内容
- 修复错误和改进代码示例

详细指南请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📝 内容规范

### Markdown 文件 (`.md`)
- **语言**：主要使用中文编写理论内容
- **用途**：数学背景、定理、证明和解释
- **格式**：支持LaTeX数学符号

### Jupyter 笔记本 (`.ipynb`)
- **语言**：代码注释和markdown单元使用英文
- **用途**：交互式演示、计算和可视化
- **库**：主要使用SymPy及相关支持库

## 🎯 学习目标

本仓库旨在帮助学习者：

- 通过清晰的解释理解基础微积分概念
- 使用计算工具应用理论知识
- 通过交互式图表可视化数学概念
- 架起理论与实际应用的桥梁
- 培养Python数学编程能力

## 📄 许可证

本项目采用 [MIT许可证](LICENSE) 开源。

## 🙏 致谢

- 基于同济大学《高等数学》教材
- 受开源教育社区启发
- 使用强大的SymPy生态系统构建

## 📞 支持

- **问题反馈**：通过 [GitHub Issues](https://github.com/yourusername/math-calculus/issues) 报告错误或请求功能
- **讨论交流**：在 [GitHub Discussions](https://github.com/yourusername/math-calculus/discussions) 参与社区讨论
- **参与贡献**：查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与

---

**祝学习愉快！🎓**

*通过交互式计算和清晰的数学阐述，探索微积分之美。*
