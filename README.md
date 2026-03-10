# rowing-session
Small script to record row session data and calculate kcal burned

# RowMetric: Power-Based Physiological Tracker

RowMetric is a Python-based analytical tool designed to provide high-fidelity metabolic tracking for indoor rowing. Unlike standard trackers that use static MET tables, RowMetric utilizes real-time Power (Watts) and Body Composition data to derive accurate energy expenditure.

## 🚀 Overview
The project was developed to bridge the gap between raw mechanical work and biological effort. It specifically addresses the "under-reporting" issues common in generic rowing calculators by implementing a modular, object-oriented approach to metabolic modeling.

## 🔬 Scientific Logic & Formulae
The application calculates the **Metabolic Equivalent of Task (MET)** using a calibrated $VO_2$ consumption model.

### 1. Power Calculation (Cubic Watts)
To account for the non-linear relationship between rowing pace and resistance, the system derives Watts using the standard physics model:
$$Watts = 2.8 / (PacePer500m / 500)^3$$

### 2. Calibrated MET Formula
Standard ACSM formulae often under-report the cost of full-body rowing. This system applies a **4.0x Mechanical Efficiency Multiplier** to align output with clinical moderate-to-vigorous intensity standards:

$$VO_2 = \left( \frac{2.8 \times \text{Watts}}{\text{Weight in kg}} \right) + 3.5$$
$$\text{Adjusted MET} = \left( \frac{VO_2}{3.5} \right) \times 4.0$$

## 🛠️ Technical Implementation (OOP)
The project is built using a modular Class-based structure, ensuring a strict **Separation of Concerns**:
* **Encapsulation:** All physiological calculations are contained within the `RowingSession` class methods.
* **Data Persistence:** Workouts are logged to a persistent CSV storage system.
* **Hardware Integration:** Supports formatted reporting to local print hardware (Canon).

## 📈 Performance Milestones
- **Weight Management:** Successfully utilized to track a 10lb loss journey (Maintained < 218 lbs).
- **Volume Goal:** Designed to facilitate a consistent 12,000m weekly volume target.