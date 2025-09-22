import pandas as pd

df = pd.read_csv("dataset.csv")

df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip().str.lower()

df.fillna(df.mean(numeric_only=True), inplace=True)
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

df.drop_duplicates(inplace=True)

if 'gender' in df.columns:
    gender_map = {'m': 'male', 'f': 'female', 'male': 'male', 'female': 'female'}
    df['gender'] = df['gender'].map(gender_map).astype('category')

if 'scheduledday' in df.columns:
    df['scheduledday'] = pd.to_datetime(df['scheduledday'], errors='coerce')

if 'appointmentday' in df.columns:
    df['appointmentday'] = pd.to_datetime(df['appointmentday'], errors='coerce')

if 'no-show' in df.columns:
    df['no-show'] = df['no-show'].map({'no': 0, 'yes': 1}).astype('int8')

if 'patientid' in df.columns:
    df['patientid'] = df['patientid'].astype('int64')

if 'age' in df.columns:
    df = df[df['age'] >= 0]
    df['age'] = df['age'].astype('int8')

if 'handcap' in df.columns:
    df['handcap'] = df['handcap'].apply(lambda x: 1 if x > 0 else 0).astype('int8')

df.to_csv("cleaned_dataset.csv", index=False)

print("Data Cleaning Done. Cleaned dataset saved to 'cleaned_dataset.csv'.")