# Contributing to Calculus Notebook 🤝

Thank you for your interest in contributing to the Calculus Notebook project! This guide will help you understand how to contribute effectively to this educational resource.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Types of Contributions](#types-of-contributions)
- [Content Guidelines](#content-guidelines)
- [Development Setup](#development-setup)
- [Submission Process](#submission-process)
- [Code of Conduct](#code-of-conduct)

## 🚀 Getting Started

### Prerequisites

Before contributing, ensure you have:

- Python 3.8+ installed
- Git knowledge and GitHub account
- Basic understanding of calculus concepts
- Familiarity with Jupyter notebooks and Markdown
- Optional: Knowledge of SymPy for mathematical computations

### First-Time Contributors

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/math-calculus.git
   cd math-calculus
   ```
3. **Set up the development environment** (see [Development Setup](#development-setup))
4. **Create a new branch** for your contribution:
   ```bash
   git checkout -b feature/your-contribution-name
   ```

## 🎯 Types of Contributions

We welcome various types of contributions:

### 1. New Chapter Implementation
- **Priority**: Chapters 1-11 are planned for implementation
- **Structure**: Follow the existing pattern in Chapter 12
- **Content**: Include both theoretical (`.md`) and practical (`.ipynb`) components

### 2. Section Expansion
- **Current Need**: Chapter 12 sections 1-6 and 8
- **Format**: Match existing section 7 structure
- **Languages**: Chinese for theory, English for code

### 3. Content Enhancement
- **Improvements**: Clarify existing explanations
- **Visualizations**: Add plots and interactive elements
- **Examples**: Provide more practical applications

### 4. Translation Work
- **Bilingual Support**: Help maintain English/Chinese consistency
- **Documentation**: Translate README or contributing guides
- **Comments**: Add bilingual code comments

### 5. Bug Fixes and Code Quality
- **Code Issues**: Fix SymPy implementation problems
- **Formatting**: Improve markdown or notebook formatting
- **Dependencies**: Update or fix package requirements

## 📝 Content Guidelines

### Markdown Files (`.md`)

**Language**: Primarily Chinese (中文)
**Purpose**: Mathematical theory, definitions, theorems, proofs

**Structure**:
```markdown
## 章节标题 (Section Title)

### 定义 (Definition)
Mathematical definition with LaTeX notation

### 定理 (Theorem)
Theorem statement with proper mathematical formatting

### 证明 (Proof)
Step-by-step proof with clear mathematical reasoning

### 例题 (Examples)
Worked examples demonstrating the concepts
```

**Math Notation**:
- Use LaTeX syntax: `$inline math$` or `$$display math$$`
- Ensure proper symbol usage and formatting
- Include both Chinese terms and English equivalents when helpful

### Jupyter Notebooks (`.ipynb`)

**Language**: English for code and explanations
**Purpose**: Interactive demonstrations and computations

**Cell Structure**:
1. **Theory Cell**: Brief explanation in English
2. **Setup Cell**: Import statements and symbol definitions
3. **Implementation Cells**: Step-by-step SymPy code
4. **Visualization Cells**: Plots and interactive elements
5. **Exercise Cells**: Practice problems for learners

**Code Style**:
```python
# Import statements
from sympy import *
import sympy as sp
import matplotlib.pyplot as plt

# Initialize pretty printing
init_printing()

# Define symbols clearly
x, y, z, t = symbols('x y z t')
n, m, k = symbols('n m k', integer=True)

# Use descriptive variable names
fourier_series = a_0/2 + Sum(a_n*cos(n*x) + b_n*sin(n*x), (n, 1, oo))
```

### File Naming Conventions

- **Chapters**: `##-chapter-name/` (e.g., `01-functions-limits/`)
- **Sections**: `##-section-name.md` and `##-section-name.ipynb`
- **Language**: `README-zh.md` for Chinese, `README.md` for English
- **Use hyphens**: Separate words with hyphens, not underscores

## 🛠️ Development Setup

### 1. Environment Setup
```bash
# Create virtual environment
python -m venv .venv

# Activate environment
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Jupyter Configuration
```bash
# Start Jupyter notebook
jupyter notebook

# Or use JupyterLab
pip install jupyterlab
jupyter lab
```

### 3. Testing Your Content
- **Markdown**: Preview using GitHub or a markdown editor
- **Notebooks**: Run all cells to ensure they execute without errors
- **Math Rendering**: Verify LaTeX expressions render correctly

## 📤 Submission Process

### 1. Pre-Submission Checklist

- [ ] All notebook cells execute without errors
- [ ] Mathematical notation renders correctly
- [ ] Content follows the established structure
- [ ] Chinese content uses proper mathematical terminology
- [ ] English code comments are clear and helpful
- [ ] New dependencies are added to `requirements.txt`
- [ ] Files follow naming conventions

### 2. Pull Request Process

1. **Commit your changes** with descriptive messages:
   ```bash
   git add .
   git commit -m "Add Chapter 3: Mean Value Theorem section"
   ```

2. **Push to your fork**:
   ```bash
   git push origin feature/your-contribution-name
   ```

3. **Create a Pull Request** on GitHub with:
   - **Clear title**: Describe what you're adding/fixing
   - **Detailed description**: Explain the mathematical content
   - **Screenshots**: If adding visualizations or new notebooks
   - **Testing notes**: Mention any specific testing you've done

### 3. Review Process

- **Maintainer Review**: Content will be reviewed for mathematical accuracy
- **Code Review**: SymPy implementations will be checked
- **Language Review**: Chinese content may be reviewed by native speakers
- **Educational Value**: Content will be assessed for learning effectiveness

## 🌟 Best Practices

### Mathematical Content
- **Accuracy**: Ensure all mathematical statements are correct
- **Clarity**: Explain concepts step-by-step
- **Completeness**: Include necessary background and context
- **References**: Cite sources when appropriate

### Code Quality
- **Readability**: Use clear variable names and comments
- **Efficiency**: Choose appropriate SymPy functions
- **Documentation**: Explain complex calculations
- **Testing**: Verify results with known examples

### Educational Value
- **Progressive Difficulty**: Build concepts gradually
- **Multiple Examples**: Provide various applications
- **Visual Learning**: Include plots and diagrams when helpful
- **Practice Opportunities**: Add exercises for learners

## 🎨 Content Suggestions

### High-Priority Contributions

1. **Chapter 1: Functions and Limits**
   - Limit definitions and theorems
   - Continuity and discontinuity
   - Limit calculation techniques

2. **Chapter 2: Derivatives and Differentials**
   - Derivative definitions
   - Differentiation rules
   - Implicit differentiation

3. **Chapter 5: Definite Integrals**
   - Riemann sums
   - Fundamental Theorem of Calculus
   - Integration techniques

### Enhancement Ideas

- **Interactive Widgets**: Use `ipywidgets` for parameter exploration
- **3D Visualizations**: Add surface plots for multivariable concepts
- **Animation**: Show limit processes or series convergence
- **Real Applications**: Include physics, engineering, or economics examples

## 📚 Resources for Contributors

### Mathematical References
- Tongji University "Advanced Mathematics" 3rd Edition
- [SymPy Documentation](https://docs.sympy.org/)
- [LaTeX Mathematical Notation](https://en.wikibooks.org/wiki/LaTeX/Mathematics)

### Technical Resources
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)
- [Chinese Mathematical Terminology](https://zh.wikipedia.org/wiki/数学术语)

## 🤝 Code of Conduct

### Our Standards

- **Respectful Communication**: Be kind and constructive in all interactions
- **Educational Focus**: Prioritize learning value in all contributions
- **Quality Over Quantity**: Focus on well-crafted, accurate content
- **Collaborative Spirit**: Help other contributors and learners

### Unacceptable Behavior

- Harassment or discriminatory language
- Submitting inaccurate mathematical content
- Plagiarism or copyright violation
- Disruptive or unconstructive criticism

## 🆘 Getting Help

### Questions and Support

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For general questions and ideas
- **Pull Request Comments**: For specific implementation questions

### Mentorship

New contributors are welcome! If you're new to:
- **Mathematical typesetting**: We can help with LaTeX
- **SymPy programming**: Examples and guidance available
- **Chinese mathematical terminology**: Native speakers can assist

## 🏆 Recognition

Contributors will be recognized through:
- **GitHub Contributors List**: Automatic recognition
- **Special Thanks**: Major contributors mentioned in releases
- **Educational Impact**: Your work helps students worldwide!

---

## 🎉 Thank You!

Your contributions make this educational resource valuable for learners worldwide. Whether you're adding a single example or implementing an entire chapter, every contribution matters.

**Happy Contributing! 📚✨**

*Together, we're making calculus more accessible and interactive for everyone.*
