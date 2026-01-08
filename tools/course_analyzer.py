#!/usr/bin/env python3
"""
Course Quality and Completeness Analyzer

This script analyzes courses in the Courses folder and provides detailed reports
about quality, completeness, and balance of educational materials.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Any
from statistics import mean, stdev
from collections import defaultdict
import argparse

# Import our metrics and data
from metrics import *
from data import get_expected_files, get_expected_module_count, get_all_course_names


class CourseAnalyzer:
    """Main class for course analysis"""
    
    def __init__(self, courses_dir: str):
        self.courses_dir = Path(courses_dir)
        self.results = {}
        
    def analyze_all_courses(self) -> Dict[str, Any]:
        """Analyzes all courses in the directory"""
        print("🔍 Starting course analysis...")
        
        course_dirs = [d for d in self.courses_dir.iterdir() 
                      if d.is_dir() and d.name in get_all_course_names()]
        
        for course_dir in course_dirs:
            print(f"📚 Analyzing course: {course_dir.name}")
            self.results[course_dir.name] = self.analyze_course(course_dir)
            
        return self.results
    
    def analyze_course(self, course_dir: Path) -> Dict[str, Any]:
        """Analyzes a single course"""
        course_name = course_dir.name
        result = {
            'course_name': course_name,
            'modules': [],
            'structure_score': 0.0,
            'content_score': 0.0,
            'balance_score': 0.0,
            'readme_score': 0.0,
            'overall_score': 0.0,
            'red_flags': [],
            'recommendations': [],
            'stats': {}
        }
        
        # Analyze course README
        readme_path = course_dir / 'README.md'
        if readme_path.exists():
            result['readme_score'] = self.analyze_readme(readme_path)
        else:
            result['red_flags'].append("❌ Missing course README.md")
        
        # Find course modules
        modules = self.find_modules(course_dir)
        result['stats']['module_count'] = len(modules)
        result['stats']['expected_modules'] = get_expected_module_count(course_name)
        
        if len(modules) != get_expected_module_count(course_name):
            result['red_flags'].append(
                MESSAGES['module_count_mismatch'].format(
                    len(modules), get_expected_module_count(course_name)
                )
            )
        
        # Analyze each module
        module_sizes = []
        for module_dir in modules:
            module_analysis = self.analyze_module(module_dir, course_name)
            result['modules'].append(module_analysis)
            module_sizes.append(module_analysis['total_size'])
        
        # Calculate metrics
        result['structure_score'] = self.calculate_structure_score(result['modules'])
        result['content_score'] = self.calculate_content_score(result['modules'])
        result['balance_score'] = self.calculate_balance_score(module_sizes)
        
        # Overall score
        result['overall_score'] = (
            result['structure_score'] * SCORE_WEIGHTS['structure_completeness'] +
            result['content_score'] * SCORE_WEIGHTS['content_quality'] +
            result['balance_score'] * SCORE_WEIGHTS['module_balance'] +
            result['readme_score'] * SCORE_WEIGHTS['readme_quality']
        )
        
        # Statistics
        if module_sizes:
            result['stats']['avg_module_size'] = mean(module_sizes)
            result['stats']['module_size_stdev'] = stdev(module_sizes) if len(module_sizes) > 1 else 0
            result['stats']['min_module_size'] = min(module_sizes)
            result['stats']['max_module_size'] = max(module_sizes)
        
        # Generate recommendations based on analysis
        result['recommendations'] = self.generate_recommendations(result)
        
        return result
    
    def find_modules(self, course_dir: Path) -> List[Path]:
        """Finds all course modules (directories with numbers)"""
        modules = []
        for item in course_dir.iterdir():
            if item.is_dir() and re.match(r'^\d+_', item.name):
                modules.append(item)
        return sorted(modules, key=lambda x: x.name)
    
    def analyze_module(self, module_dir: Path, course_name: str) -> Dict[str, Any]:
        """Analyzes a single course module"""
        expected_files = get_expected_files(course_name)
        
        result = {
            'module_name': module_dir.name,
            'files': {},
            'total_size': 0,
            'missing_files': [],
            'unexpected_files': [],
            'small_files': [],
            'quality_indicators': {'good': 0, 'concerning': 0}
        }
        
        # Check each expected file
        for expected_file in expected_files:
            file_path = module_dir / expected_file
            if file_path.exists():
                size = file_path.stat().st_size
                content = self.read_file_safely(file_path)
                
                result['files'][expected_file] = {
                    'exists': True,
                    'size': size,
                    'quality_score': self.analyze_file_content(content)
                }
                result['total_size'] += size
                
                # File size check
                if size < MIN_FILE_SIZES.get(expected_file, 0):
                    result['small_files'].append({
                        'file': expected_file,
                        'size': size,
                        'min_expected': MIN_FILE_SIZES.get(expected_file, 0)
                    })
                    
                # Content analysis
                quality = self.analyze_file_content(content)
                result['quality_indicators']['good'] += quality['good']
                result['quality_indicators']['concerning'] += quality['concerning']
                    
            else:
                result['missing_files'].append(expected_file)
                result['files'][expected_file] = {'exists': False}
        
        # Check for unexpected files
        for file_path in module_dir.iterdir():
            if file_path.is_file() and file_path.name not in expected_files:
                result['unexpected_files'].append(file_path.name)
        
        return result
    
    def analyze_readme(self, readme_path: Path) -> float:
        """Analyzes README file quality"""
        content = self.read_file_safely(readme_path)
        if not content:
            return 0.0
            
        size = readme_path.stat().st_size
        score = 0.0
        
        # File size (20% of score)
        if size >= RECOMMENDED_FILE_SIZES['README.md']:
            score += 0.2
        elif size >= MIN_FILE_SIZES['README.md']:
            score += 0.1
            
        # Mandatory patterns (50% of score)
        must_have_found = 0
        for pattern in README_PATTERNS['must_have']:
            if re.search(pattern, content, re.MULTILINE):
                must_have_found += 1
        score += 0.5 * (must_have_found / len(README_PATTERNS['must_have']))
        
        # Additional patterns (30% of score)
        good_to_have_found = 0
        for pattern in README_PATTERNS['good_to_have']:
            if re.search(pattern, content, re.MULTILINE):
                good_to_have_found += 1
        score += 0.3 * (good_to_have_found / len(README_PATTERNS['good_to_have']))
        
        return min(score, 1.0)
    
    def analyze_file_content(self, content: str) -> Dict[str, int]:
        """Analyzes file content quality"""
        good_indicators = 0
        concerning_indicators = 0
        
        for indicator in QUALITY_INDICATORS['good']:
            good_indicators += content.count(indicator)
            
        for indicator in QUALITY_INDICATORS['concerning']:
            concerning_indicators += content.count(indicator)
            
        return {'good': good_indicators, 'concerning': concerning_indicators}
    
    def calculate_structure_score(self, modules: List[Dict]) -> float:
        """Calculates structural completeness score"""
        if not modules:
            return 0.0
            
        total_completeness = 0
        for module in modules:
            expected_count = len([f for f in module['files'].keys()])
            existing_count = len([f for f in module['files'].values() if f.get('exists')])
            if expected_count > 0:
                total_completeness += existing_count / expected_count
                
        return total_completeness / len(modules) if modules else 0
    
    def calculate_content_score(self, modules: List[Dict]) -> float:
        """Calculates content quality score"""
        if not modules:
            return 0.0
            
        total_good = sum(m['quality_indicators']['good'] for m in modules)
        total_concerning = sum(m['quality_indicators']['concerning'] for m in modules)
        
        if total_good + total_concerning == 0:
            return 0.5  # Neutral score if no indicators
            
        return total_good / (total_good + total_concerning * 2)  # Weight negative indicators more
    
    def calculate_balance_score(self, module_sizes: List[int]) -> float:
        """Calculates module balance score"""
        if len(module_sizes) < 2:
            return 1.0
            
        avg_size = mean(module_sizes)
        if avg_size == 0:
            return 0.0
            
        # Coefficient of variation (ratio of standard deviation to mean)
        cv = stdev(module_sizes) / avg_size
        
        # The lower the coefficient of variation, the better the balance
        # CV < 0.3 = excellent balance
        # CV < 0.5 = good balance  
        # CV < 0.8 = fair balance
        # CV >= 0.8 = poor balance
        
        if cv < 0.3:
            return 1.0
        elif cv < 0.5:
            return 0.8
        elif cv < 0.8:
            return 0.6
        else:
            return 0.3
    
    def generate_recommendations(self, course_result: Dict) -> List[str]:
        """Generates recommendations for course improvement"""
        recommendations = []
        
        # Structure recommendations
        if course_result['structure_score'] < 0.8:
            missing_count = sum(len(m['missing_files']) for m in course_result['modules'])
            if missing_count > 0:
                recommendations.append(
                    f"🔧 Add missing files ({missing_count} files)"
                )
        
        # File size recommendations
        small_files_count = sum(len(m['small_files']) for m in course_result['modules'])
        if small_files_count > 0:
            recommendations.append(
                f"📝 Expand content of small files ({small_files_count} files)"
            )
        
        # Content recommendations
        if course_result['content_score'] < 0.6:
            recommendations.append(
                "✨ Improve content quality: add examples, structure text"
            )
        
        # Balance recommendations
        if course_result['balance_score'] < 0.6:
            recommendations.append(
                "⚖️ Balance modules: align content volume between modules"
            )
        
        # README recommendations
        if course_result['readme_score'] < 0.7:
            recommendations.append(
                "📋 Improve course README: add description, structure, learning objectives"
            )
        
        return recommendations
    
    def read_file_safely(self, file_path: Path) -> str:
        """Safely reads file with encoding error handling"""
        try:
            return file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            try:
                return file_path.read_text(encoding='latin1')
            except:
                return ""
        except:
            return ""


class ReportGenerator:
    """Report generator"""
    
    def __init__(self, analysis_results: Dict):
        self.results = analysis_results
    
    def generate_summary_report(self) -> str:
        """Generates summary report"""
        report = []
        report.append("=" * 80)
        report.append("📊 COURSE ANALYSIS SUMMARY REPORT")
        report.append("=" * 80)
        report.append("")
        
        # General statistics
        total_courses = len(self.results)
        avg_score = mean([r['overall_score'] for r in self.results.values()])
        
        report.append(f"🎯 General statistics:")
        report.append(f"   Total courses: {total_courses}")
        report.append(f"   Average score: {avg_score:.2f}")
        report.append(f"   Status: {self.get_score_status(avg_score)}")
        report.append("")
        
        # Course ranking
        sorted_courses = sorted(self.results.items(), 
                              key=lambda x: x[1]['overall_score'], 
                              reverse=True)
        
        report.append("🏆 Course quality ranking:")
        for i, (course_name, course_data) in enumerate(sorted_courses, 1):
            score = course_data['overall_score']
            status = self.get_score_status(score)
            report.append(f"   {i}. {course_name}: {score:.2f} {status}")
        report.append("")
        
        return "\n".join(report)
    
    def generate_detailed_report(self, course_name: str) -> str:
        """Generates detailed course report focused on issues"""
        if course_name not in self.results:
            return f"Course {course_name} not found in analysis results"
        
        course = self.results[course_name]
        report = []
        
        report.append(f"📚 DETAILED REPORT: {course_name}")
        report.append("="*60)
        report.append("")
        
        # Overall score and status
        score = course['overall_score']
        report.append(f"🎯 Overall score: {score:.2f} {self.get_score_status(score)}")
        report.append("")
        
        # Problems first - what needs attention
        has_issues = False
        
        # Critical issues
        if course['red_flags']:
            has_issues = True
            report.append("🚨 CRITICAL ISSUES:")
            for flag in course['red_flags']:
                report.append(f"   {flag}")
            report.append("")
        
        # Recommendations - what to do
        if course['recommendations']:
            has_issues = True
            report.append("💡 IMPROVEMENTS NEEDED:")
            for recommendation in course['recommendations']:
                report.append(f"   {recommendation}")
            report.append("")
        
        # Module issues
        modules_with_issues = []
        for module in course['modules']:
            module_issues = []
            
            if module['missing_files']:
                module_issues.append(f"Missing: {', '.join(module['missing_files'])}")
            
            if module['small_files']:
                small_file_names = [f"{sf['file']} ({sf['size']}b)" for sf in module['small_files']]
                module_issues.append(f"Too small: {', '.join(small_file_names)}")
            
            if module['unexpected_files']:
                module_issues.append(f"Unexpected: {', '.join(module['unexpected_files'])}")
            
            if module_issues:
                modules_with_issues.append((module['module_name'], module_issues))
        
        if modules_with_issues:
            has_issues = True
            report.append("📋 MODULE ISSUES:")
            for module_name, issues in modules_with_issues:
                report.append(f"   📁 {module_name}:")
                for issue in issues:
                    report.append(f"      ⚠️  {issue}")
            report.append("")
        
        # If no major issues, show brief stats
        if not has_issues:
            report.append("✅ NO MAJOR ISSUES FOUND")
            report.append("")
            stats = course['stats']
            report.append("📈 Quick stats:")
            report.append(f"   • Modules: {stats['module_count']}/{stats['expected_modules']}")
            if 'avg_module_size' in stats:
                report.append(f"   • Avg module size: {stats['avg_module_size']:.0f} bytes")
        
        return "\n".join(report)
    
    def get_score_status(self, score: float) -> str:
        """Returns status based on score"""
        if score >= SCORE_THRESHOLDS['excellent']:
            return MESSAGES['excellent']
        elif score >= SCORE_THRESHOLDS['good']:
            return MESSAGES['good']
        elif score >= SCORE_THRESHOLDS['fair']:
            return MESSAGES['fair']
        else:
            return MESSAGES['poor']
    

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Course Quality Analyzer')
    parser.add_argument('--courses-dir', '-d', 
                       default='../Courses', 
                       help='Path to courses folder')
    parser.add_argument('--course', '-c', 
                       help='Course name for detailed analysis')
    parser.add_argument('--summary', '-s', 
                       action='store_true',
                       help='Show summary only (skip detailed module analysis)')
    
    args = parser.parse_args()
    
    # Determine path to courses
    courses_dir = Path(__file__).parent / args.courses_dir
    if not courses_dir.exists():
        print(f"❌ Courses folder not found: {courses_dir}")
        sys.exit(1)
    
    # Run analysis
    analyzer = CourseAnalyzer(str(courses_dir))
    results = analyzer.analyze_all_courses()
    
    # Generate report
    generator = ReportGenerator(results)
    
    # Always show summary
    print(generator.generate_summary_report())
    
    # Detailed analysis
    if args.course:
        # Specific course
        if args.course in results:
            print("\n" + "=" * 80)
            print(generator.generate_detailed_report(args.course))
        else:
            print(f"\n❌ Course '{args.course}' not found")
            print(f"Available courses: {', '.join(results.keys())}")
    elif not args.summary:
        # All courses detailed (default behavior)
        for course_name in results.keys():
            print("\n" + "=" * 80)
            print(generator.generate_detailed_report(course_name))


if __name__ == "__main__":
    main()