# 🎮 Game Analytics Dashboard — Product Performance Insights

**Author:** Apple Uwaifo  
**Role:** Product Management & Analytics  
**Institution:** University of Alberta  
**Contact:** [LinkedIn](https://www.linkedin.com/in/appleuwaifo) | [GitHub](https://github.com/appleuwaifo)

---

## 🧭 Overview

This project replicates a simplified version of a **Product Manager’s analytics workflow at Electronic Arts (EA)** — focusing on player engagement, retention, and monetization insights.

The objective was to **simulate gameplay data**, identify key metrics such as **DAU (Daily Active Users)** and **D1/D7 Retention**, and visualize these KPIs through an interactive **Power BI dashboard**.

The goal is to demonstrate the ability to connect **technical execution (data analytics)** with **strategic decision-making (product insights)** — the foundation of great Product Management.

---

## 🎯 Product Goals

| Objective | Measurement | Tools Used |
|------------|--------------|-------------|
| Understand player engagement | Daily Active Users (DAU) | Python (pandas) |
| Quantify monetization | Revenue & ARPDAU | Power BI |
| Evaluate retention health | D1 / D7 Retention Rates | Python (pandas, datetime) |
| Communicate findings effectively | Visual dashboard and product narrative | Power BI + Markdown |

---

## 🧩 Methodology

### 1. Data Generation  
Simulated 3,000 players across 60 days of gameplay using Python.  
Generated:
- **User data:** install date, country, device  
- **Event data:** gameplay sessions, purchases, in-game actions  

### 2. KPI Computation  
- **DAU:** daily unique players  
- **Revenue & ARPDAU:** total and average revenue per daily active user  
- **Retention (D1/D7):** proportion of players returning 1 and 7 days after install  

### 3. Visualization  
- **Power BI Dashboard** for trend exploration (DAU, Revenue, Retention)  
- **Python (matplotlib)** for static charts embedded in reports  

---

## 📈 Key Insights

> As a Product Manager, I focused on identifying signals that inform both player experience and business health.

### Engagement  
- DAU stabilized after week 2 — suggesting onboarding friction or novelty decay.  
- Weekend DAU was 15 % higher, indicating an opportunity for event-based engagement.  

### Retention  
- D1 retention averaged **42 %**, D7 retention **35 %**, showing a solid early hook but weaker mid-term re-engagement.  
- Opportunity: introduce a **“Day 5 Reward Event”** to extend the player lifecycle.  

### Monetization  
- ARPDAU spiked 20 % after mid-month content drops — confirming that **content refreshes directly influence revenue**.  
- Next step: test **timed in-game bundles** alongside content updates.  

---

## 🧮 Example KPIs

| Metric | Average | Observation |
|---------|----------|--------------|
| DAU | ~2,000 | Stabilizes after 2 weeks |
| Revenue | \$3,500 / day | Follows DAU trend |
| ARPDAU | \$1.64 | Consistent after Day 15 |
| D1 Retention | 42 % | Healthy early engagement |
| D7 Retention | 35 % | Opportunity to improve |

---

## 🛠️ Tools & Tech Stack

| Purpose | Tool |
|----------|------|
| Data Simulation | Python (NumPy, pandas) |
| Metric Analysis | pandas, datetime |
| Visualization | matplotlib, Power BI Desktop |
| Environment | VS Code |
| Version Control | GitHub |

---

## 📊 Dashboard Preview

**Power BI Highlights**
- DAU trend visualization  
- D1/D7 retention curves  
- Revenue and ARPDAU cards  
- Country / device filters for segmentation  

🖼️ *Example Charts (from Python outputs)*  
- ![DAU Trend](outputs/charts/dau_trend.png)  
- ![Revenue Trend](outputs/charts/revenue_trend.png)  
- ![Retention Curves](outputs/charts/retention_curves.png)

---

## 💡 Recommendations

| Insight | Proposed Action | Expected Impact |
|----------|------------------|-----------------|
| D7 retention decline | Add “Day 5 Reward” re-engagement event | +3 pp D7 retention |
| Stable weekend DAU | Introduce weekend tournaments | +10 % DAU on weekends |
| ARPDAU tied to content drops | Align bundle releases with content updates | +15 % ARPDAU |
---

## 🗣️ Product Manager’s Reflection

> Building this project helped me apply analytical thinking to product outcomes — balancing metrics with user empathy.  
> Every number represents a player’s story, and great Product Management connects data and experience to deliver meaningful play.

---

## 📬 Contact
- **LinkedIn:** [linkedin.com/in/appleuwaifo](https://www.linkedin.com/in/appleuwaifo)  
- **Email:** apple.uwaifo@gmail.com  
- **GitHub:** [github.com/appleuwaifo](https://github.com/appleuwaifo)

---

### 🔖 Tags
`#ProductManagement` `#GameAnalytics` `#PowerBI` `#Python` `#EA` `#DataDrivenPM`
