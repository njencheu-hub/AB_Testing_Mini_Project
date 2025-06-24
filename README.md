# A/B Test Analysis: Marketing Campaign Funnel Optimization
  
**Tools Used:** Python, Pandas, StatsModels, Matplotlib  

---

## 📚 Table of Contents

- [Overview](#overview)
- [Real-World Use Cases](#real-world-use-cases)
- [Features](#features)
- [Key Funnel Metrics Analyzed](#key-funnel-metrics-analyzed)
- [Statistical Test Results](#statistical-test-results)
- [Conclusion](#conclusion)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This analysis compared two digital marketing campaigns using an A/B testing framework to evaluate performance across the full purchase funnel. Data preprocessing included text parsing, type conversion, and missing value handling to ensure clean metrics.

---

## 🌍 Real-World Use Cases

- **Digital Marketing Teams**: Optimize campaign strategy by identifying underperforming funnel stages.
- **Product Teams**: Understand how changes to ad content or landing pages influence user engagement.
- **Growth Analysts**: Validate campaign effectiveness before full rollout.
- **E-commerce Teams**: Identify which campaigns lead to more purchases and better ROI.

---

## ✨ Features

- Cleans and preps funnel data from both control and test campaigns
- Calculates engagement and conversion metrics for each funnel stage
- Applies Z-tests for statistical comparison of purchase conversion rates
- Optional configurations for testing direction (`two-sided`, `smaller`)
- Generates summary statistics for visualization and reporting

---

## Key Funnel Metrics Analyzed

This project computes and compares the following key performance indicators (KPIs) across control and test groups:

- **CTR (Click-Through Rate)**
- **Search Rate**
- **View Content Rate**
- **Add to Cart Rate**
- **Purchase Rate**
- **Overall Conversion Rate**

Each stage was computed and averaged across both groups to diagnose drop-off points and performance differences.

---

## Statistical Test Results

A **Z-test** was conducted on the purchase conversion rates:

- **Z-statistic:** 33.77  
- **P-value:** 2.3e-250 → Statistically significant  
- **Results**: The **Test campaign outperformed** the Control campaign with overwhelming confidence.

**Optional tests explored:**
- Alternative hypotheses (`two-sided`, `smaller`)
- Confidence intervals
- Custom funnel metrics (CTR, Add-to-Cart, etc.)

---

## Conclusion

The test campaign demonstrated a significant uplift in purchases versus the control. This result supports a full rollout of the new marketing approach. Funnel-based analysis highlighted which stages drove this improvement, enabling further targeted optimizations.

---

## Installation


To install the required Python packages:

pip install -r requirements.txt

## Usage

To run the analysis:

python ab_test_analysis.py

## Contributing

We welcome community contributions!

1. Fork the repository

2. Create a new branch:

git checkout -b feature/your-feature

3. Make your changes

4. Push to your branch:

git push origin feature/your-feature

5. Submit a Pull Request

## License
This project is licensed under the MIT License.
