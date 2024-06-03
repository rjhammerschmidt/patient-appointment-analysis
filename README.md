# Patient Appointment Analysis

## Project Overview
This project aims to analyze patient appointment data to identify patterns, no-show rates, and factors affecting appointment adherence.

## Data Analytics Process
1. Data Collection: Collecting the data from a public dataset.
2. Data Cleaning: Cleaning and preprocessing the data to ensure it is suitable for analysis.
3. Exploratory Data Analysis (EDA): Analyzing the data to uncover  patterns and insights.
4. Modeling: Building models to predict no-shows.
5. Visualization & Presentation: Visualizing the findings and presenting actionable insights.

## Repository Structure
- `data/`: Contains the dataset and related documentation.
- `notebooks/`: Jupyter notebooks for each step of the data analytics process.
- `scripts/`: Python scripts used in the notebooks.
- `visualizations/`: Visual outputs of the analysis.
- `README.md`: Project overview and instructions.
- `requirements.txt`: Required Python packages.

## Getting Started
1. Clone the repository: `git clone https://github.com/yourusername/patient-appointment-analysis.git` 
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Jupyter notebooks in order.

## Dataset
The dataset used in this project is from the [Kaggle Medical Appointment No Shows dataset](https://www.kaggle.com/datasets/joniarroba/noshowappointments).

## Results
In this project we analyzed patient appointment data to identify factors that influence no-show rates. The key findings are summarized below:

Days Difference vs. No-Show Rate:

A significant correlation was found between the number of days between scheduling and the appointment date and the likelihood of no-shows. As the days difference increases, the no-show rate generally increases up until about 25 days, then plateaus until about 75 days. The days difference then begins increasing after about 112 days, indicating that patients are more likely to miss appointments scheduled very far in advance.

Impact of Age Group on No-Show Rate:

No-show rates vary across different age groups. Younger patients (particularly those aged 18-24) show higher no-show rates compared to other age groups. This finding suggests that targeted interventions may be necessary for this age group to reduce no-show rates.

Impact of SMS Received on No-Show Rate by Age Group:

Receiving an SMS reminder significantly reduces the no-show rate across all age groups. The reduction is particularly notable among younger patients (18-24). This underscores the effectiveness of SMS reminders in improving patient attendance, especially for age groups with higher no-show tendencies.

These findings highlight the importance of timely appointment scheduling and the effectiveness of SMS reminders in reducing no-show rates. By implementing strategies such as sending SMS reminders and possibly adjusting scheduling practices, healthcare providers can improve patient attendance and optimize appointment management.