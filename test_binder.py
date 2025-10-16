#!/usr/bin/env python3
"""
Test script to verify MyBinder setup works correctly.
This script tests all the key dependencies that should be available in the Binder environment.
"""

def test_imports():
    """Test that all required packages can be imported."""
    try:
        import sympy as sp
        print("✅ SymPy imported successfully")
        print(f"   SymPy version: {sp.__version__}")
    except ImportError as e:
        print(f"❌ SymPy import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ NumPy imported successfully")
        print(f"   NumPy version: {np.__version__}")
    except ImportError as e:
        print(f"❌ NumPy import failed: {e}")
        return False
    
    try:
        import matplotlib.pyplot as plt
        print("✅ Matplotlib imported successfully")
        print(f"   Matplotlib version: {plt.matplotlib.__version__}")
    except ImportError as e:
        print(f"❌ Matplotlib import failed: {e}")
        return False
    
    try:
        import scipy
        print("✅ SciPy imported successfully")
        print(f"   SciPy version: {scipy.__version__}")
    except ImportError as e:
        print(f"❌ SciPy import failed: {e}")
        return False
    
    
    return True

def test_sympy_basic():
    """Test basic SymPy functionality."""
    try:
        import sympy as sp
        x = sp.Symbol('x')
        expr = x**2 + 2*x + 1
        derivative = sp.diff(expr, x)
        print("✅ SymPy basic functionality works")
        print(f"   Derivative of {expr} = {derivative}")
        return True
    except Exception as e:
        print(f"❌ SymPy basic functionality failed: {e}")
        return False

def test_jupyter_environment():
    """Test Jupyter environment."""
    try:
        import IPython
        print("✅ IPython imported successfully")
        print(f"   IPython version: {IPython.__version__}")
        return True
    except ImportError as e:
        print(f"❌ IPython import failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing MyBinder setup for math-calculus...")
    print("=" * 50)
    
    all_tests_passed = True
    
    print("\n📦 Testing package imports...")
    all_tests_passed &= test_imports()
    
    print("\n🔢 Testing SymPy functionality...")
    all_tests_passed &= test_sympy_basic()
    
    print("\n📓 Testing Jupyter environment...")
    all_tests_passed &= test_jupyter_environment()
    
    print("\n" + "=" * 50)
    if all_tests_passed:
        print("🎉 All tests passed! MyBinder setup should work correctly.")
    else:
        print("⚠️  Some tests failed. Please check the requirements.txt file.")
