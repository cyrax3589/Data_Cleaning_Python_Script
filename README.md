# 🩺 Medical Appointment No-Shows – Data Cleaning

This project focuses on cleaning the **Medical Appointment No-Shows Dataset** from Kaggle.  
The dataset contains information about patients in Brazil and whether they showed up for their scheduled medical appointments.  

👉 Dataset source: [Kaggle – Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments)

---

## 📌 Project Overview
The raw dataset contains missing values, inconsistent formatting, incorrect data types, and noisy entries.  
The goal of this project is to **clean and preprocess the dataset** so it can be reliably used for **exploratory data analysis (EDA) and machine learning models**.

---

## 🛠 Data Cleaning Steps
The following operations were performed in `data_cleaner.py`:

1. **Standardized column names**  
   - Converted to lowercase, replaced spaces with underscores.

2. **Handled categorical text**  
   - Stripped spaces, converted to lowercase.  
   - Normalized `gender` values (`m`, `f` → `male`, `female`).  
   - Converted `no-show` column to binary (0 = no, 1 = yes).

3. **Missing values treatment**  
   - Numeric columns: filled with mean.  
   - Categorical columns: filled with mode.

4. **Duplicate removal**  
   - Dropped all duplicate rows.

5. **Date parsing**  
   - Converted `scheduledday` and `appointmentday` to `datetime`.

6. **Data type corrections**  
   - `patientid` → int64  
   - `age` → int8 (removed invalid ages < 0)  
   - `handcap` → binary (0 = no, 1 = yes)  
   - `no-show` → int8  

7. **Exported final dataset**  
   - Cleaned data saved as `cleaned_dataset.csv`.

---

## 📊 Data Quality Report (After Cleaning)
- **Shape:** 110,527 rows × 14 columns  
- **No missing values** ✅  
- **No duplicate rows** ✅  
- **All columns properly typed** ✅  
- **Categorical values standardized** ✅  

---

## 📂 Repository Structure

├── dataset.csv # Original raw dataset
├── cleaned_dataset.csv # Cleaned dataset (output)
├── data_cleaner.py # Python script for cleaning
├── README.md # Project documentation

