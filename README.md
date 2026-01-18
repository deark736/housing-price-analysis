# Housing Price Data Analysis

## Overview

As a software engineer developing data analysis skills, this project explores a real-world housing dataset to identify meaningful patterns and relationships between property features and housing prices. The goal of this software is to practice working with structured data, applying statistical operations, and visualizing trends using Python.

The dataset analyzed in this project comes from Kaggle and contains information about housing prices along with features such as house area, number of bedrooms, and whether the house has air conditioning.

Dataset source:
https://www.kaggle.com/datasets/yasserh/housing-prices-dataset

The purpose of this software is to strengthen my ability to use Python data analysis libraries to extract insights from data and to clearly communicate those findings through both numerical output and graphical visualization.

A short demonstration video showing the program running and explaining the code can be found here:

[Software Demo Video](https://youtu.be/szwzT0t85W8)

---

## Data Analysis Results

### Question 1: How does house area relate to price?

The analysis shows a clear positive relationship between house area and price. Larger houses generally cost more, although the scatter plot reveals increasing variability for larger homes. This suggests that while size is an important factor, other variables such as amenities and layout also influence price.

### Question 2: How does the number of bedrooms affect average house price?

The average price increases as the number of bedrooms increases from one to five bedrooms. However, six-bedroom houses show a lower average price, which is likely due to a smaller sample size or differing characteristics of those properties.

### Question 3: Does air conditioning impact housing prices?

Homes with air conditioning have a significantly higher average price compared to homes without air conditioning. This indicates that air conditioning is a strong value-adding feature in this dataset.

---

## Development Environment

This software was developed using the following tools and technologies:

- **Operating System:** Windows 11
- **Editor:** Visual Studio Code
- **Programming Language:** Python 3.14
- **Libraries:**
  - pandas (data loading and analysis)
  - matplotlib (data visualization)

---

## Useful Websites

The following resources were helpful during development:

- https://pandas.pydata.org/docs/
- https://matplotlib.org/stable/tutorials/index.html
- https://www.kaggle.com/
- https://www.python.org/

---

## Future Work

There are several ways this project could be expanded in the future:

- Add additional visualizations such as box plots or bar charts
- Explore correlations between more features in the dataset
- Perform data cleaning and outlier removal
- Add basic predictive modeling to estimate house prices
