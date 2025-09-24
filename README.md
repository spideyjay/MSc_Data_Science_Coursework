# MSc Data Science Coursework: Programming for Data Science

This repository contains the coursework submission for the "Programming for Data Science" module, covering topics in Object-Oriented Programming (OOP), web scraping, data analysis, and data ethics.

## ⚙️ Setup and Installation

To run this project, follow these steps:

1.  **Clone the Repository:**
    `git clone <your-repository-url>`

2.  **Navigate to the Project Directory:**
    `cd <your-repository-name>`

3.  **Create a Virtual Environment:**
    `python -m venv venv`

4.  **Activate the Virtual Environment:**
    * **On Windows (PowerShell):** `& .\venv\Scripts\Activate.ps1`
    * **On macOS/Linux (Bash):** `source venv/bin/activate`

5.  **Install Dependencies:**
    `pip install -r requirements.txt`



## 📂 Project Structure

project-root/
│
├── question1_university_system/ # Enhanced OOP University Management System
│ ├── person.py # Abstract Person class with validation
│ ├── student.py # Student classes with GPA calculation
│ ├── faculty.py # Faculty hierarchy with workload management
│ ├── course.py # Course with waitlist system
│ ├── department.py # Department management
│ ├── main.py # Demonstration script
│ └── University_Management_System_report.md # Technical documentation
│
├── question2_ecommerce_analysis/ # E-commerce Data Analysis Pipeline
│ ├── data_collection/
│ │ └── scraper.py # Multi-source web scraper
│ ├── data_processing/
│ │ └── data_cleaner.py # Data cleaning and preprocessing
│ ├── analysis/
│ │ └── analysis.py # Statistical analysis & ML models
│ ├── visualizations/
│ │ └── visualizer.py # Interactive Plotly visualizations
│ └── data/
│ ├── books_data.csv # Scraped books data
│
│
├── question3_ethics_report/ # Healthcare Data Ethics Analysis
│ └── healthcare_ethics_report.md # Comprehensive ethics report
│
├── requirements.txt # Python dependencies
└── README.md # This file

--------------------------------------------------------------------------

## ▶️ How to Run the Code

### Question 1: Enhanced University Management System ✅ **COMPLETE**

The OOP-based university management system demonstrates exceptional implementation of advanced programming concepts:

**Key Features:**
- Advanced inheritance hierarchy with abstract base classes
- Credit-based GPA calculation with academic status tracking
- Waitlist system for course enrollment
- Comprehensive data validation and security
- Polymorphic method overriding

**To run the demonstration:**
cd question1_university_system
python main.py


## Expected Output:

Course enrollment with prerequisite checking

GPA calculation and academic status determination

Waitlist management demonstration

Polymorphic behavior across different person types

Department statistics and analytics


### Question 2: E-commerce Data Analysis Pipeline ✅ **COMPLETE**

A comprehensive data analysis pipeline scraping and analyzing multi-source e-commerce data:

# Step 1: Data Collection (Web Scraping)
cd question2_ecommerce_analysis/data_collection
python scraper.py

Scrapes book data from books.toscrape.com and additional e-commerce sources

# Step 2: Data Cleaning and Preprocessing
cd question2_ecommerce_analysis/data_processing
python data_cleaner.py

Cleans, transforms, and merges datasets with advanced preprocessing

# Step 3: Statistical and Predictive Analysis
cd question2_ecommerce_analysis/analysis
python analysis.py

Performs hypothesis testing, correlation analysis, and machine learning predictions

# Step 4: Interactive Visualizations
cd question2_ecommerce_analysis/visualizations
python visualizer.py

Generates interactive Plotly charts and comprehensive analysis reports


## Question 3: Data Ethics in Healthcare Report ✅ **COMPLETE**

# View the comprehensive ethics report:
cd question3_ethics_report
open healthcare_ethics_report.md

# Report Highlights:

- Critical analysis of healthcare data privacy (HIPAA/GDPR comparison)

- Algorithmic bias mitigation strategies in medical AI

- Ethical framework for healthcare data scientists

- Stakeholder impact analysis and balanced solutions



🎯 Advanced Features Implemented


# Question 1: Exceptional OOP Implementation

- Factory Pattern for object creation

- Credit-weighted GPA calculation system

- Audit logging for sensitive data access

- Comprehensive unit tests for all major components

- Professional documentation with type hints throughout


# Question 2: Advanced Data Analysis

- Multi-source data collection from different e-commerce platforms

- Hypothesis testing (t-tests, ANOVA) for price comparisons

- Machine learning models for price prediction

- Interactive Plotly dashboards with filtering capabilities

- Statistical significance analysis and confidence intervals


# Question 3: Comprehensive Ethics Framework

- Real-world case studies of healthcare AI implementations

- Practical ethical checklist for data scientists

- FAccT principles application in healthcare context

- Regulatory compliance analysis across jurisdictions


📊 Project Status

- Question 1: University Management System - ✅ Complete 

- Question 2: E-commerce Data Analysis - ✅ Complete 

- Question 3: Ethics Report - ✅ Complete 


🔧 Technical Stack

- Python 3.8+ with type hints and modern syntax

- OOP Principles: Inheritance, Polymorphism, Encapsulation, Abstraction

- Data Analysis: pandas, numpy, scikit-learn, scipy

- Visualization: Plotly, matplotlib, seaborn

- Web Scraping: BeautifulSoup4, requests

- Testing: pytest (comprehensive test suite)


📈 Learning Outcomes Demonstrated

This coursework showcases advanced proficiency in:

Object-Oriented Programming with enterprise-level design patterns

Data Pipeline Development from collection to visualization

Statistical Analysis and hypothesis testing methodologies

Ethical Considerations in data science applications

Professional Documentation and code quality standards


🤝 Contributing
This is a coursework submission. For questions or suggestions regarding the implementation, please refer to the technical documentation in each question's directory.


📄 License
