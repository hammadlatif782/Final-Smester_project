
#Verification Script for OOP Analysis Project
#=============================================
# final smester project
#This script verifies that all project components are working correctly.
#Run this before submission to ensure everything is in order.

#Usage:
    #python verify_project.py


import os
import sys
from pathlib import Path


class ProjectVerifier:
    #Verify all components of the OOP analysis project
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.successes = []
        self.base_dir = Path(__file__).parent
    
    def check_files_exist(self):
        #Verify all required files exist
        print("\n" + "="*60)
        print("1. Checking for Required Files")
        print("="*60)
        
        required_files = [
            "README.md",
            "PILLOW_OOP_ANALYSIS.md",
            "custom_filters.py",
            "PRESENTATION_GUIDE.md",
            "verify_project.py",
        ]
        
        for filename in required_files:
            filepath = self.base_dir / filename
            if filepath.exists():
                size_kb = filepath.stat().st_size / 1024
                print(f" {filename} ({size_kb:.1f} KB)")
                self.successes.append(f"Found {filename}")
            else:
                print(f" {filename} - NOT FOUND")
                self.errors.append(f"Missing {filename}")
    
    def check_pillow_installed(self):
        """Verify Pillow library is installed."""
        print("\n" + "="*60)
        print("2. Checking Pillow Installation")
        print("="*60)
        
        try:
            import PIL
            from PIL import Image, ImageDraw, ImageFilter
            print(f" Pillow installed (version {PIL.__version__})")
            self.successes.append("Pillow is installed and importable")
        except ImportError as e:
            print(f" Pillow not installed: {e}")
            self.errors.append(f"Pillow import failed: {e}")
    
    def check_custom_filters(self):
        """Verify custom filters module works."""
        print("\n" + "="*60)
        print("3. Checking Custom Filters Module")
        print("="*60)
        
        try:
            from custom_filters import VignetteFilter, SepiaToneFilter, InvertFilter
            print("yes VignetteFilter class found")
            print("yes SepiaToneFilter class found")
            print("yes InvertFilter class found")
            self.successes.append("All custom filter classes importable")
            
            # Test instantiation
            try:
                vignette = VignetteFilter(strength=0.5, radius=1.5)
                print("yes VignetteFilter instantiated successfully")
                
                sepia = SepiaToneFilter(intensity=0.8)
                print(" SepiaToneFilter instantiated successfully")
                
                invert = InvertFilter()
                print("yes InvertFilter instantiated successfully")
                
                self.successes.append("All custom filters instantiate correctly")
            except Exception as e:
                print(f" Filter instantiation failed: {e}")
                self.errors.append(f"Filter instantiation error: {e}")
        
        except ImportError as e:
            print(f" Custom filters import failed: {e}")
            self.errors.append(f"Custom filters import error: {e}")
    
    def check_filter_inheritance(self):
        """Verify custom filters properly inherit from Filter."""
        print("\n" + "="*60)
        print("4. Checking OOP Principles")
        print("="*60)
        
        try:
            from custom_filters import VignetteFilter, SepiaToneFilter
            from PIL import ImageFilter
            
            # Check inheritance
            if issubclass(VignetteFilter, ImageFilter.Filter):
                print("yes VignetteFilter inherits from ImageFilter.Filter")
                self.successes.append("VignetteFilter inheritance correct")
            else:
                print(" VignetteFilter doesn't inherit from ImageFilter.Filter")
                self.errors.append("VignetteFilter inheritance incorrect")
            
            if issubclass(SepiaToneFilter, ImageFilter.Filter):
                print("yes SepiaToneFilter inherits from ImageFilter.Filter")
                self.successes.append("SepiaToneFilter inheritance correct")
            else:
                print(" SepiaToneFilter doesn't inherit from ImageFilter.Filter")
                self.errors.append("SepiaToneFilter inheritance incorrect")
            
            # Check method implementation
            vignette = VignetteFilter()
            if hasattr(vignette, 'filter'):
                print("yes VignetteFilter implements filter() method")
                self.successes.append("VignetteFilter.filter() exists")
            else:
                print("VignetteFilter missing filter() method")
                self.errors.append("VignetteFilter.filter() not implemented")
        
        except Exception as e:
            print(f"✗ OOP verification failed: {e}")
            self.errors.append(f"OOP verification error: {e}")
    
    def check_filter_functionality(self):
        """Test that filters actually work."""
        print("\n" + "="*60)
        print("5. Testing Filter Functionality")
        print("="*60)
        
        try:
            from PIL import Image
            from custom_filters import VignetteFilter, SepiaToneFilter, InvertFilter
            
            # Create test image
            print("Creating test image...")
            test_img = Image.new('RGB', (50, 50), color='blue')
            
            # Test VignetteFilter
            try:
                vignette = VignetteFilter(strength=0.5)
                result = test_img.filter(vignette)
                if isinstance(result, Image.Image):
                    print("yes VignetteFilter.filter() returns Image object")
                    self.successes.append("VignetteFilter produces valid output")
                else:
                    print("yes VignetteFilter.filter() didn't return Image")
                    self.errors.append("VignetteFilter output type incorrect")
            except Exception as e:
                print(f" VignetteFilter failed: {e}")
                self.errors.append(f"VignetteFilter execution error: {e}")
            
            # Test SepiaToneFilter
            try:
                sepia = SepiaToneFilter(intensity=0.5)
                result = test_img.filter(sepia)
                if isinstance(result, Image.Image):
                    print("yes SepiaToneFilter.filter() returns Image object")
                    self.successes.append("SepiaToneFilter produces valid output")
                else:
                    print(" SepiaToneFilter.filter() didn't return Image")
                    self.errors.append("SepiaToneFilter output type incorrect")
            except Exception as e:
                print(f" SepiaToneFilter failed: {e}")
                self.errors.append(f"SepiaToneFilter execution error: {e}")
            
            # Test InvertFilter
            try:
                invert = InvertFilter()
                result = test_img.filter(invert)
                if isinstance(result, Image.Image):
                    print(" InvertFilter.filter() returns Image object")
                    self.successes.append("InvertFilter produces valid output")
                else:
                    print(" InvertFilter.filter() didn't return Image")
                    self.errors.append("InvertFilter output type incorrect")
            except Exception as e:
                print(f" InvertFilter failed: {e}")
                self.errors.append(f"InvertFilter execution error: {e}")
        
        except Exception as e:
            print(f" Functionality test failed: {e}")
            self.errors.append(f"Functionality test error: {e}")
    
    def check_parameter_validation(self):
        """Test parameter validation."""
        print("\n" + "="*60)
        print("6. Testing Parameter Validation (Encapsulation)")
        print("="*60)
        
        try:
            from custom_filters import VignetteFilter, SepiaToneFilter
            
            # Test invalid strength
            try:
                bad_filter = VignetteFilter(strength=1.5)
                print(" VignetteFilter accepted invalid strength (1.5)")
                self.errors.append("VignetteFilter validation missing")
            except ValueError:
                print("yes VignetteFilter rejected invalid strength")
                self.successes.append("VignetteFilter validates strength parameter")
            
            # Test invalid intensity
            try:
                bad_filter = SepiaToneFilter(intensity=-0.5)
                print(" SepiaToneFilter accepted invalid intensity (-0.5)")
                self.errors.append("SepiaToneFilter validation missing")
            except ValueError:
                print("yes SepiaToneFilter rejected invalid intensity")
                self.successes.append("SepiaToneFilter validates intensity parameter")
        
        except Exception as e:
            print(f" Validation test failed: {e}")
            self.errors.append(f"Validation test error: {e}")
    
    def check_documentation(self):
        """Verify documentation files."""
        print("\n" + "="*60)
        print("7. Checking Documentation Quality")
        print("="*60)
        
        # Check README
        try:
            with open(self.base_dir / "README.md", "r") as f:
                content = f.read()
                size = len(content)
                if size > 1000:
                    print(f"yes README.md is substantial ({size} bytes)")
                    self.successes.append("README.md has good content")
                else:
                    print(f"warning README.md might be too short ({size} bytes)")
                    self.warnings.append("README.md might need more content")
                
                if "Pillow" in content and "OOP" in content:
                    print("yes README.md contains expected keywords")
                else:
                    print("warning README.md might be missing key content")
        except Exception as e:
            self.errors.append(f"README.md check failed: {e}")
        
        # Check Analysis document
        try:
            with open(self.base_dir / "PILLOW_OOP_ANALYSIS.md", "r") as f:
                content = f.read()
                size = len(content)
                if size > 5000:
                    print(f"yes PILLOW_OOP_ANALYSIS.md is substantial ({size} bytes)")
                    self.successes.append("PILLOW_OOP_ANALYSIS.md has good content")
                else:
                    print(f"warning: Analysis document might be too short ({size} bytes)")
                    self.warnings.append("Analysis document might need expansion")
                
                # Check for OOP principles
                principles = ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"]
                found = sum(1 for p in principles if p in content)
                if found >= 3:
                    print(f"yes Analysis covers OOP principles ({found}/4)")
                    self.successes.append("OOP principles documented")
        except Exception as e:
            self.errors.append(f"Analysis check failed: {e}")
    
    def print_summary(self):
        """Print verification summary."""
        print("\n" + "="*60)
        print("VERIFICATION SUMMARY")
        print("="*60)
        
        print(f"\n Successes: {len(self.successes)}")
        for success in self.successes[:5]:
            print(f"  • {success}")
        if len(self.successes) > 5:
            print(f"  ... and {len(self.successes) - 5} more")
        
        if self.warnings:
            print(f"\n Warnings: {len(self.warnings)}")
            for warning in self.warnings:
                print(f"  • {warning}")
        
        if self.errors:
            print(f"\n Errors: {len(self.errors)}")
            for error in self.errors:
                print(f"  • {error}")
        
        print("\n" + "="*60)
        if not self.errors:
            print("ALL CHECKS PASSED - PROJECT READY FOR SUBMISSION")
            return 0
        else:
            print(" SOME CHECKS FAILED - PLEASE FIX ISSUES ABOVE")
            return 1
    
    def run_all_checks(self):
        """Run all verification checks."""
        print("\n" + "█"*60)
        print("OOP ANALYSIS PROJECT VERIFICATION")
        print("█"*60)
        
        self.check_files_exist()
        self.check_pillow_installed()
        self.check_custom_filters()
        self.check_filter_inheritance()
        self.check_filter_functionality()
        self.check_parameter_validation()
        self.check_documentation()
        
        return self.print_summary()


def main():
    """Main entry point."""
    verifier = ProjectVerifier()
    exit_code = verifier.run_all_checks()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
