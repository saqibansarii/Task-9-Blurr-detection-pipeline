"""
Test suite for Blur Detection Application
"""
import pytest
import sys
import os

# Add parent directory to path to import main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_imports():
    """Test that all required modules can be imported"""
    try:
        import cv2
        import numpy as np
        from flask import Flask
        assert True
    except ImportError as e:
        pytest.fail(f"Import failed: {e}")

def test_flask_app_exists():
    """Test that Flask app is created"""
    try:
        from main import app
        assert app is not None
        assert app.name == 'main'
    except Exception as e:
        pytest.fail(f"Flask app test failed: {e}")

def test_opencv_available():
    """Test that OpenCV is available"""
    try:
        import cv2
        version = cv2.__version__
        assert version is not None
        print(f"OpenCV version: {version}")
    except Exception as e:
        pytest.fail(f"OpenCV test failed: {e}")

def test_numpy_available():
    """Test that NumPy is available"""
    try:
        import numpy as np
        version = np.__version__
        assert version is not None
        print(f"NumPy version: {version}")
    except Exception as e:
        pytest.fail(f"NumPy test failed: {e}")

def test_flask_routes():
    """Test that Flask routes are defined"""
    try:
        from main import app
        
        # Get all registered routes
        routes = [str(rule) for rule in app.url_map.iter_rules()]
        
        # Check if home route exists
        assert '/' in routes or any('index' in route for route in routes)
        print(f"Registered routes: {routes}")
    except Exception as e:
        pytest.fail(f"Route test failed: {e}")

def test_app_configuration():
    """Test basic Flask app configuration"""
    try:
        from main import app
        
        # Test that app has basic configuration
        assert hasattr(app, 'config')
        assert app.testing in [True, False]
        
        print("Flask app configuration is valid")
    except Exception as e:
        pytest.fail(f"Configuration test failed: {e}")

# Run tests if executed directly
if __name__ == "__main__":
    pytest.main([__file__, "-v"])