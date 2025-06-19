# A/B Test Analysis: Marketing Campaign Funnel Optimization
  
**Tools Used:** Python, Pandas, StatsModels, Matplotlib  

## Overview

This project compared two digital marketing campaigns using an A/B testing framework to evaluate performance across the full purchase funnel. Data preprocessing included text parsing, type conversion, and missing value handling to ensure clean metrics.

---

## Key Funnel Metrics Analyzed

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
- **Conclusion:** The **Test campaign outperformed** the Control campaign with overwhelming confidence.

Optional tests explored:
- Alternative hypotheses (`two-sided`, `smaller`)
- Confidence intervals
- Custom funnel metrics (CTR, Add-to-Cart, etc.)

---

## Conclusion

The test campaign demonstrated a significant uplift in purchases versus the control. This result supports a full rollout of the new marketing approach. Funnel-based analysis highlighted which stages drove this improvement, enabling further targeted optimizations.