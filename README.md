# Calculus Notebook 📚

A comprehensive interactive calculus learning repository that combines theoretical knowledge with practical SymPy implementations. This repository provides both mathematical foundations in Markdown format and executable Jupyter notebooks for hands-on exploration of calculus concepts.

## 🌟 Features

- **Bilingual Content**: Mathematical concepts explained in both English and Chinese
- **Interactive Learning**: Jupyter notebooks with SymPy code for computational exploration
- **Comprehensive Coverage**: Organized into 12 chapters following standard calculus curriculum
- **Practical Examples**: Real-world applications and visual demonstrations
- **Open Source**: Community-driven development with contribution opportunities

## 📖 Table of Contents

Based on Tongji University's "Advanced Mathematics" 3rd Edition (同济大学《高等数学》第3版):

1. **Functions and Limits** (函数与极限)
2. **Derivatives and Differentials** (导数与微分)
3. **Mean Value Theorem and Applications of Derivatives** (微分中值定理与导数的应用)
4. **Indefinite Integrals** (不定积分)
5. **Definite Integrals** (定积分)
6. **Applications of Definite Integrals** (定积分的应用)
7. **Differential Equations** (微分方程)
8. **Vector Algebra and Analytic Geometry** (向量代数与空间解析几何)
9. **Multivariable Calculus** (多元函数微分法及其应用)
10. **Multiple Integrals** (重积分)
11. **Line and Surface Integrals** (曲线积分与曲面积分)
12. **Infinite Series** (无穷级数) ✅ *Currently implemented*

## 🚀 Getting Started

### Quick Start (Online)

- **Launch Binder**: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/julianShi/math-calculus/HEAD)
- **Launch with JupyterLab**: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/julianShi/math-calculus/HEAD?urlpath=lab)

### Local Installation

#### Prerequisites

- Python 3.8 or higher
- Git

#### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/julianShi/math-calculus.git
   cd math-calculus
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

#### Alternative: Using Conda

```bash
conda env create -f environment.yml
conda activate math-calculus
jupyter notebook
```

### Quick Start

Navigate to any chapter folder (e.g., `12-infinite-series/`) and explore:

- **`.md` files**: Theoretical background and mathematical foundations
- **`.ipynb` files**: Interactive code examples and computations

Example workflow:
1. Read `07-fourier-series.md` for theoretical understanding
2. Open `07-fourier-series.ipynb` for hands-on practice
3. Run cells to see SymPy calculations in action

## 📁 Repository Structure

```
math-calculus/
├── README.md                    # This file
├── CONTRIBUTING.md             # Contribution guidelines
├── requirements.txt            # Python dependencies
├── 01-functions-limits/        # Chapter 1 (planned)
├── 02-derivatives/             # Chapter 2 (planned)
├── ...                         # Chapters 3-11 (planned)
└── 12-infinite-series/         # Chapter 12 (implemented)
    ├── README-zh.md            # Chinese chapter overview
    ├── 07-fourier-series.md    # Fourier series theory (Chinese)
    ├── 07-fourier-series.ipynb # Fourier series notebook (English)
    └── ...                     # Additional sections
```

## 🛠️ Technology Stack

- **[SymPy](https://www.sympy.org/)**: Symbolic mathematics in Python
- **[Jupyter](https://jupyter.org/)**: Interactive computing environment
- **[NumPy](https://numpy.org/)**: Numerical computing
- **[Matplotlib](https://matplotlib.org/)**: Data visualization
- **[SciPy](https://scipy.org/)**: Scientific computing

## 🤝 Contributing

We welcome contributions from the community! This repository is designed to be collaborative, with opportunities to:

- Implement new chapters (1-11)
- Add more sections to existing chapters
- Improve existing content
- Translate content between languages
- Fix bugs and enhance code examples

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📝 Content Guidelines

### Markdown Files (`.md`)
- **Language**: Primarily Chinese for theoretical content
- **Purpose**: Mathematical background, theorems, proofs, and explanations
- **Format**: LaTeX math notation supported

### Jupyter Notebooks (`.ipynb`)
- **Language**: English for code comments and markdown cells
- **Purpose**: Interactive demonstrations, calculations, and visualizations
- **Libraries**: Primarily SymPy with supporting libraries as needed

## 🎯 Learning Objectives

This repository aims to help learners:

- Understand fundamental calculus concepts through clear explanations
- Apply theoretical knowledge using computational tools
- Visualize mathematical concepts through interactive plots
- Bridge the gap between theory and practical applications
- Develop proficiency in mathematical programming with Python

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Based on Tongji University's "Advanced Mathematics" textbook
- Inspired by the open-source educational community
- Built with the powerful SymPy ecosystem

## 📞 Support

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/yourusername/math-calculus/issues)
- **Discussions**: Join community discussions in [GitHub Discussions](https://github.com/yourusername/math-calculus/discussions)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get involved

---

**Happy Learning! 🎓**

*Explore the beauty of calculus through interactive computation and clear mathematical exposition.*