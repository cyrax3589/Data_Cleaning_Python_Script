import pandas as pd

df = pd.read_csv("dataset.csv") #read the dataset

df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True) #strip the columns and replace whitespaces with '_'

for col in df.select_dtypes(include=['object']).columns: #selects the text data and removes whitespaces and makes it lowercase
    df[col] = df[col].str.strip().str.lower()

df.fillna(df.mean(numeric_only=True), inplace=True) #it calculates the mode (the most frequently occurring value) for each text column and fills any missing values in that column with its mode
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

df.drop_duplicates(inplace=True) #removes any rows that are exact duplicates

if 'gender' in df.columns:
    gender_map = {'m': 'male', 'f': 'female'} #changes short forms of m,f to male & female
    df['gender'] = df['gender'].map(gender_map).astype('category')

if 'scheduledday' in df.columns: #converts from plain text into a proper datetime format
    df['scheduledday'] = pd.to_datetime(df['scheduledday'], errors='coerce')

if 'appointmentday' in df.columns: #converts from plain text into a proper datetime format
    df['appointmentday'] = pd.to_datetime(df['appointmentday'], errors='coerce')

if 'no-show' in df.columns: #converts 'yes'/'no' column into a numeric binary format (0 or 1)
    df['no-show'] = df['no-show'].map({'no': 0, 'yes': 1}).astype('int8')

if 'patientid' in df.columns: # converts the 'patientid' column to a 64-bit integer
    df['patientid'] = df['patientid'].astype('int64')

if 'age' in df.columns: #removes age with negetive values
    df = df[df['age'] >= 0]
    df['age'] = df['age'].astype('int8')

if 'handcap' in df.columns: #changes handicap value to binary o or 1
    df['handcap'] = df['handcap'].apply(lambda x: 1 if x > 0 else 0).astype('int8')

df.to_csv("cleaned_dataset.csv", index=False) #saves the new file


print("Data Cleaning Done. Cleaned dataset saved to 'cleaned_dataset.csv'.") #prints a confirmation messege
