# Data Cleaning Project – Medical Appointment No Shows  

This project is all about **cleaning messy datasets** and getting them ready for analysis.  
I started with the **Medical Appointment No Shows dataset** from Kaggle, which contains details about patients in Brazil and whether they showed up for their doctor’s appointments.  

The raw data wasn’t perfect — it had duplicates, inconsistent values, weird data types, and some noisy entries.  
The goal here was simple: **turn it into a clean, reliable dataset** that’s easy to work with.  

---

## What I Did
Here’s a quick breakdown of the cleaning process in `data_cleaner.py`:

-  **Renamed columns** to lowercase and replaced spaces with underscores.  
-  **Handled missing values** → filled numbers with the mean, and text with the most common value.  
-  **Removed duplicates** so every record is unique.  
-  **Cleaned up categorical text** → like gender (`M`, `m`, `Male` → `male`).  
-  **Fixed dates** → converted appointment and scheduling dates into proper datetime format.  
-  **Corrected data types** → IDs as integers, ages as small integers, and “no-show” turned into 0/1.  
-  **Simplified special columns** → `handcap` is now just 0 or 1.  
-  **Removed invalid values** → e.g., negative ages.  

At the end, the dataset was exported as `cleaned_dataset.csv`.

---

## Final Results
- **Rows:** 110,527  
- **Columns:** 14  
- **Missing values:** 0  
- **Duplicates:** 0  
- **Data types:** all fixed and consistent  
- **Categorical values:** standardized and cleaned  

---

## Repo Contents

├── dataset.csv 

├── cleaned_dataset.csv 

├── data_cleaner.py 

├── README.md

├── Requirements.txt
