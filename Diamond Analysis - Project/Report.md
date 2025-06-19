# 💎 MSBA – 210 Business Analytics  
**Instructor:** Dr. Chong Huang, Ph.D.  
**Project:** Diamond Project (Group 4)  
**Focus:** Round Shape, 0.70 CT - 0.89 CT

### 👥 Group Members
- Taruniben Atodariya  
- Aditi Kadam  
- Preet Sanandiya  

---

## 📑 Table of Contents

1. Cover Page  
2. Table of Contents  
3. Introduction  
4. Background  
5. Data Analysis  
6. Conclusion  
7. Appendix  

---

## 📘 Introduction

The diamond trade has a very important place in the world economy. Traders and investors must have simple, reliable information about the prices and qualities of diamonds. 

In this project, we analyzed diamond prices in relation to the **4Cs**:
- Carat weight  
- Cut  
- Color  
- Clarity  

We used data from reliable B2B and B2C online vendors, including:
- Blue Nile  
- With Clarity  
- James Allen  
- Brilliant Earth  
- Rare Carat  

### Project Goals
- Build a regression equation for diamond price based on the 4Cs  
- Establish key factors affecting price  
- Develop a **Rapaport-style report** for diamonds sized between **0.70 and 0.89 carats**

Carat (equal to 200 milligrams) is a key value determinant. Beyond carat, **cut**, **clarity**, and **color** significantly affect pricing. Thus, selecting a carat weight that balances desirability and affordability is crucial.

---

## 🔍 Background

This project involves comparing prices of **AA-grade diamonds** from the five major online vendors mentioned above. The aim is to assess what influences diamond prices based on the 4Cs.

### The 4Cs Explained:
- **Carat weight:** Refers to diamond size; larger diamonds are more valuable.  
- **Cut:** Affects how well the diamond reflects light; better cuts result in greater brilliance.  
- **Color:** The closer to colorless, the higher the price.  
- **Clarity:** Measures internal flaws or inclusions; fewer flaws increase value.

---

## 📊 Pivot Table Analysis

We created Pivot Tables to simplify analysis and visually interpret data.

### 🔹 Natural Diamond (0.7–0.89 Ct) – Average Price/Carat

| Color | IF     | VVS1   | VVS2   | VS1    | VS2    | SI1    | SI2    | Grand Total |
|-------|--------|--------|--------|--------|--------|--------|--------|--------------|
| D     | 4868.71| 5264.18| 4265.10| 3500.74| 3213.71| 2646.72| 2200.36| 3564.06       |
| E     | 5365.65| 4733.25| 3627.13| 2886.09| 3253.33| 2772.57| 2184.76| 3435.47       |
| F     | 4057.45| 4498.35| 3438.85| 3242.64| 2914.83| 2455.71| 2207.49| 3205.86       |
| G     | 3502.61| 3847.20| 2922.89| 2906.37| 2940.84| 2397.20| 1987.49| 2885.59       |
| H     | 3226.50| 3141.42| 2622.92| 2354.30| 2561.27| 2411.02| 1808.28| 2593.48       |
| I     | 3005.03| 2701.70| 2386.04| 2479.46| 2282.64| 2055.68| 1780.55| 2393.36       |
| J     | 2472.59| 2278.69| 1907.70| 1834.43| 2114.57| 1650.02| 1902.93| 2018.85       |
| K     | 2203.88| 1929.22| 2025.22| 1546.89| 1631.26| 1371.35| 1429.30| 1720.79       |

---

### 🔹 Lab-Grown Diamond (0.7–0.89 Ct) – Average Price/Carat

| Color | IF     | VVS1   | VVS2   | VS1    | VS2    | SI1    | SI2    | Grand Total |
|-------|--------|--------|--------|--------|--------|--------|--------|--------------|
| D     | 972.90 | 953.61 | 851.23 | 593.67 | 615.44 | 790.32 | 763.62 | 799.00       |
| E     | 987.73 | 945.21 | 672.20 | 601.45 | 616.69 | 539.34 | 660.25 | 721.55       |
| F     | 697.56 | 874.82 | 631.11 | 608.45 | 658.34 | 460.06 | 169.86 | 585.74       |
| G     | 875.93 | 184.20 | 517.81 | 425.49 | 255.87 | 0.00   | 0.00   | 316.46       |
| H     | 0.00   | 535.03 | 465.03 | 541.53 | 201.88 | 180.95 | 0.00   | 274.92       |
| I     | 0.00   | 0.00   | 0.00   | 355.76 | 377.34 | 0.00   | 0.00   | 104.73       |
| J     | 0.00   | 237.50 | 210.53 | 0.00   | 187.79 | 195.24 | 0.00   | 118.72       |
| K     | 0.00   | 0.00   | 0.00   | 0.00   | 0.00   | 0.00   | 0.00   | 0.00         |

---

## 🌡️ Heatmap Comparisons

### 🔸 Lab-Grown vs Natural Diamonds

| Color | IF | VVS1 | VVS2 | VS1 | VS2 | SI1 | SI2 |
|-------|----|------|------|-----|-----|-----|-----|
| D     | 20%| 18%  | 20%  | 17% | 19% | 30% | 35% |
| E     | 18%| 20%  | 19%  | 21% | 19% | 19% | 30% |
| F     | 17%| 19%  | 18%  | 19% | 23% | —   | —   |
| G     | 9% | —    | —    | —   | —   | —   | —   |
| H     | 8% | —    | —    | —   | —   | —   | —   |

---

### 🔸 Natural Diamond vs Rapaport Report

| Color | IF  | VVS1 | VVS2 | VS1 | VS2 | SI1 | SI2 |
|-------|-----|------|------|-----|-----|-----|-----|
| D     | 91% | 87%  | 80%  | 85% | 80% | 76% |
| E     | 91% | 88%  | 79%  | 70% | 93% | 89% | 81% |
| F     | 90% | 80%  | 85%  | 88% | 85% | 88% |
| G     | 78% | 92%  | 77%  | 83% | 95% | 89% | 83% |
| H     | 85% | 90%  | 82%  | 78% | 91% | 92% | 82% |

---

## 📉 Regression Equations

### 🔹 Natural Diamonds

#### 📈 Color vs. Average Price/Carat
- Regression Equation: `y = -270.42x + 3944.1`
- R² = 0.9907

#### 📈 Clarity vs. Average Price/Carat
- Regression Equation: `y = -270.44x + 3837.7`
- R² = 0.9604

---

### 🔹 Lab-Grown Diamonds

#### 📈 Color vs. Average Price/Carat
- Regression Equation: `y = -120.14x + 905.77`
- R² = 0.9527

#### 📈 Clarity vs. Average Price/Carat
- Regression Equation: `y = -42.07x + 543.99`
- R² = 0.9113

---

## 📈 Descriptive Analysis (Natural Diamonds – 30 Samples)

### 📊 Price/Carat Values (Sample)
Examples include:
- 3140.85, 3361.11, 3750.00, 3994.73, 4962.50

### 📊 Summary Statistics
- Mean: 3994.73  
- Median: 3967.65  
- Mode: N/A  
- Standard Deviation: 486.47  
- Variance: 236657.38  
- Range: 1821.65  
- Minimum: 3140.85  
- Maximum: 4962.50  
- Skewness: 0.13  
- Kurtosis: -0.52  
- Confidence Interval (95%): 181.65  

---

## 📈 Descriptive Analysis (Lab-Grown Diamonds – 30 Samples)

### 📊 Price/Carat Values (Sample)
Examples include:
- 639.24, 655.56, 715.07, 763.38, 1323.94

### 📊 Summary Statistics
- Mean: 821.76  
- Median: 763.63  
- Mode: N/A  
- Standard Deviation: 176.66  
- Variance: 31209.32  
- Range: 685.05  
- Minimum: 638.89  
- Maximum: 1323.94  
- Skewness: 0.99  
- Kurtosis: 0.47  

---

## ✅ Conclusion

In summary, our studies on diamond quality and pricing have uncovered significant insights from data collected via:

- [Bluenile.com](https://www.bluenile.com)
- [Withclarity.com](https://www.withclarity.com)
- [Jamesallen.com](https://www.jamesallen.com)
- [Brilliantearth.com](https://www.brilliantearth.com)
- [Rarecarat.com](https://www.rarecarat.com)

### 🔍 Key Findings:
- **Carat weight** has the largest impact on price.
- Other factors in descending order of importance: **Cut**, **Color**, and **Clarity**.
- **Lab-grown diamonds** are significantly cheaper than natural ones, though this gap is narrowing.

We used **descriptive statistics**, including:
- Heat maps  
- Scatter plots  
- Pivot tables  

### 📊 Dashboard:
- Includes **bar charts** and **cluster column charts**
- Enables side-by-side comparison of **natural vs. lab-grown diamonds** across **color and clarity**

This study is especially relevant to:
- Investors
- Diamond dealers
- Researchers  
...who seek data-driven insights for smarter market decisions.

---

## 📎 Appendix

### 🔗 Data Sources:
- [Blue Nile](https://www.bluenile.com/)
- [With Clarity](https://www.withclarity.com/)
- [Brilliant Earth](https://www.brilliantearth.com/)
- [James Allen](https://www.jamesallen.com/)
- [Rare Carat](https://www.rarecarat.com/)

### 📂 Excel Workbook:
- [Excel Workbook Link](https://pacificedu-my.sharepoint.com/:x:/g/personal/t_atodariya_u_pacific_edu/EdMjTItekYBCnu4oVeprU2AB_1TTNd6DmQH67CHdSJnjGg?e=QBSHfX)

---

