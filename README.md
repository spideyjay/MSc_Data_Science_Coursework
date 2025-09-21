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



## ▶️ How to Run the Code

The coursework is divided into three main components:

### Question 1: University Management System
To run the OOP-based university management system, execute the main script:
`python question1_university_system/main.py`

### Question 2: E-commerce Data Analysis
To run the data analysis pipeline, navigate to the directory and run the relevant scripts (e.g., for scraping, processing, and analysis).
`cd question2_social_media_analysis`

*(Note: You will develop these scripts in the next phase. For now, you can leave this section as a placeholder.)*

### Question 3: Data Ethics Report
The report is a markdown file. You can view it in a Markdown viewer or convert it to a PDF for submission.
`open question3_ethics_report/healthcare_ethics_report.md`


## 📂 Project Structure

-   `question1_university_system/`: Contains all Python classes and scripts for the OOP-based university management system.
-   `question2_social_media_analysis/`: Houses the data collection, processing, and analysis scripts for the e-commerce data.
-   `question3_ethics_report/`: Includes the final technical report on data ethics in healthcare.
-   `requirements.txt`: Lists all required Python dependencies.
-   `README.md`: This documentation file.

--------------------------------------------------------------------------

# High-Level Design Document

📂 Question 1: Enhanced OOP - University Management System 

## Design Philosophy

The goal is to build a system that is not only functional but also scalable, maintainable, and robust. This will be achieved by implementing advanced OOP principles beyond the basic requirements.

### High-Level Plan

•	Inheritance Hierarchy: The core of the system will be the Person base class. We will extend this to Student, Faculty, and Staff. To show a deeper understanding, the hierarchy will be further extended to Professor, Lecturer, TA (as subclasses of Faculty), and Undergraduate Student, Graduate Student (as subclasses of Student). This demonstrates a comprehensive grasp of inheritance.
•	Encapsulation and Validation: All class attributes will be private (e.g., _name, _gpa). Public methods (@property getters and @<attribute>.setter setters) will be implemented to control access and enforce data integrity checks. For instance, the gpa setter method will include validation to ensure the value is between 0.0 and 4.0.
•	Polymorphism with Method Overriding: We will demonstrate polymorphism by implementing a get_responsibilities() method in the base Person class and overriding it in each subclass. For example, a Student's get_responsibilities() will return "Attend classes and complete assignments," while a Professor's will return "Teach and conduct research." This will be showcased by iterating through a list of different Person objects and calling the same method, illustrating their distinct behaviours.
•	Advanced Features: To achieve an exceptional grade, we will consider implementing a Factory Pattern for creating Person objects. This design pattern makes the code more flexible for adding new person types in the future without modifying existing code.
•	Testing: We will write a series of unit tests for key functions to demonstrate the correctness of the implementation, which is a bonus point opportunity.

________________________________________
📂 Question 2: E-commerce Data Analysis 

## Design Philosophy
The plan is to create a complete data analysis pipeline that goes beyond a single data source and uses advanced statistical techniques and interactive visualizations to deliver insightful findings.

### High-Level Plan

•	Data Collection: We will use requests and BeautifulSoup to scrape data from http://books.toscrape.com, ensuring proper error handling, retry logic, and delays to be a good "web citizen". For an exceptional mark, we will also research and scrape data from at least one other simple e-commerce demo site to fulfil the "multi-source" requirement. All data will be saved in a structured format like CSV or JSON.
•	Data Cleaning: The data cleaning pipeline will be robust, handling messy, real-world data. This will include text preprocessing, handling missing values and duplicates, and date/time standardization.
•	Advanced Statistical Analysis: We will go beyond basic descriptive statistics. We will perform a hypothesis test, specifically an independent samples t-test, to statistically compare the average prices of books in two different categories (e.g., Fiction vs. Non-Fiction). This shows a deeper understanding of statistical methods.
•	Visualization: We will create a comprehensive analysis report with multiple visualizations. For an outstanding grade, we will use the Plotly library to create interactive plots, which is a bonus feature. These interactive plots will allow for filtering and exploration, which is an innovative approach.

________________________________________
📂 Question 3: AI Ethics in Healthcare Data 

## Design Philosophy
The report will be a well-researched, professional-level document that provides a critical analysis of ethical issues in AI in healthcare. It will go beyond basic definitions and provide real-world examples and practical solutions.

### High-Level Plan
•	Healthcare Data Privacy: We will research and analyze HIPAA (the U.S. healthcare data privacy law) and compare it with the GDPR, highlighting specific challenges that are unique to medical data, such as the difficulty of true anonymization.
•	Algorithmic Bias: The report will identify sources of bias in medical datasets (e.g., demographic, geographic) and provide real-world case studies of how biased AI has led to health disparities. We will suggest concrete mitigation strategies, such as using fairness metrics and incorporating diverse datasets, to address these issues.
•	Ethical Framework: We will develop a practical ethical checklist for healthcare data scientists. This framework will be based on well-known principles like FAccT (Fairness, Accountability, and Transparency) and will discuss critical concepts like the "right to explanation" for AI-driven medical decisions.
•	Stakeholder Analysis: The report will analyze the impact of healthcare AI on different stakeholders (patients, providers, researchers) and propose balanced solutions to address their needs.


## 🟢 Project Status

-   **Question 1: University Management System** - **Complete**.
-   **Question 2: E-commerce Data Analysis** - In Progress.
-   **Question 3: Ethics Report** - In Progress.

### Question 1: University Management System

The `main.py` script demonstrates the full functionality of the OOP-based system. It showcases:
* **Inheritance:** Creation of a hierarchy from `Person` to `Student`, `Faculty`, and their respective subclasses.
* **Polymorphism:** The `get_responsibilities()` method is called on a list of different object types, each returning a unique response.
* **Encapsulation & Validation:** The GPA setter method is demonstrated, showing how invalid input is rejected.

To run the script, use the following command from the `question1_university_system` directory:
`python main.py`


## 🟢 Project Status

-   **Question 1: University Management System** - **Complete**.
-   **Question 2: E-commerce Data Analysis** - **Complete**.
-   **Question 3: Ethics Report** - In Progress.



### Question 2: E-commerce Data Analysis

This component is a full data analysis pipeline that scrapes, cleans, analyzes, and visualizes data from an e-commerce website. The process is broken into four sequential steps, and each script must be run from its respective directory.

**Step 1: Data Collection (Web Scraping)**
The scraper has been enhanced to collect more data points, including book **rating** and **availability**. To run it, navigate to the `question2_social_media_analysis\data_collection` directory and run:
`python scraper.py`

**Step 2: Data Cleaning and Preprocessing**
This script now cleans and converts the new `rating` and `availability` columns. To run it, navigate to the `question2_social_media_analysis\data_processing` directory and run:
`python data_cleaner.py`

**Step 3: Advanced Statistical and Predictive Analysis**
The analysis script now includes new statistical summaries for rating and a **predictive model** that uses both `category` and `rating` to predict price. To run it, navigate to the `question2_social_media_analysis\analysis` directory and run:
`python analysis.py`

**Step 4: Visualizations**
New plots have been added to visualize the distribution of ratings and the relationship between rating and price. To generate the plots, navigate to the `question2_social_media_analysis\visualizations` directory and run:
`python visualizer.py`