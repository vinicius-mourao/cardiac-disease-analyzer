# Import the necessary libraries for data manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    """Load the heart disease dataset from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully. {len(df)} rows found.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """Clean the dataset by handling missing values and duplicates."""
    original_len = len(df)
    df = df.drop_duplicates()  # Remove duplicate rows
    df = df[df['Cholesterol'] > 0]  # Remove rows with cholesterol values of 0
    df = df[df['RestingBP'] > 0]  # Remove rows with resting blood pressure values of 0
    df = df[(df['Age'] >= 20) & (df['Age'] <= 100)]  # Keep only reasonable age values (of adults)
    removed = original_len - len(df)
    print(f"Removed {removed} rows with invalid or missing values.")
    return df

def calculate_statistics(df):
    """Calculate and print basic statistics about the dataset."""
    print("Basic Statistics:")
    print(df[['Age', 'RestingBP', 'Cholesterol', 'MaxHR']].describe())

def detect_anomalies(df):
    """Detect anomalies in the dataset using simple thresholding."""
    anomalies_chol = df[(df['Cholesterol'] > 300)]
    anomalies_bp = df[df['RestingBP'] > 180]
    anomalies_hr = df[df['MaxHR'] < 60]
    print(f"High cholesterol (Cholesterol > 300): {len(anomalies_chol)} cases")
    print(f"High resting blood pressure (RestingBP > 180): {len(anomalies_bp)} cases")
    print(f"Low maximum heart rate (MaxHR < 60): {len(anomalies_hr)} cases")

    return anomalies_bp, anomalies_chol, anomalies_hr

def plot_heart_rate(df):
    """Plot heart rate distribution by heart disease status."""
    plt.figure(figsize=(10, 6))
    plt.hist(df[df['HeartDisease'] == 0]['MaxHR'], bins=20, alpha=0.5, label='No Heart Disease')
    plt.hist(df[df['HeartDisease'] == 1]['MaxHR'], bins=20, alpha=0.5, label='Heart Disease')
    plt.title('Maximum Heart Rate Distribution by Heart Disease Status')
    plt.xlabel('Maximum Heart Rate (bpm)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

def plot_cholesterol(df):
    """Plot cholesterol levels by heart disease status."""
    plt.figure(figsize=(10, 6))
    plt.hist(df[df['HeartDisease'] == 0]['Cholesterol'], bins=20, alpha=0.5, label='No Heart Disease')
    plt.hist(df[df['HeartDisease'] == 1]['Cholesterol'], bins=20, alpha=0.5, label='Heart Disease')
    plt.title('Cholesterol Levels by Heart Disease Status')
    plt.xlabel('Cholesterol (mg/dL)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show() 

def plot_age_distribution(df):
    """Plot age distribution by heart disease status."""
    plt.figure(figsize=(10, 6))
    plt.hist(df[df['HeartDisease'] == 0]['Age'], bins=20, alpha=0.5, label='No Heart Disease')
    plt.hist(df[df['HeartDisease'] == 1]['Age'], bins=20, alpha=0.5, label='Heart Disease')
    plt.title('Age Distribution by Heart Disease Status')
    plt.xlabel('Age (years)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

def plot_heart_disease_by_sex(df):
    """Plot heart disease prevalence by sex."""
    grouped = df.groupby(['Sex', 'HeartDisease']).size().unstack()
    grouped.plot(kind = 'bar', color = ['skyblue', 'lightcoral'], edgecolor = 'black', figsize = (10, 6))
    plt.title('Heart Disease Prevalence by sex')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.legend(['No Heart Disease', 'Heart Disease'])
    plt.show()

def main():
    df = load_data('heart_failure_data.csv')
    if df is None: return
    df = clean_data(df)
    calculate_statistics(df)
    detect_anomalies(df)
    plot_heart_rate(df)
    plot_cholesterol(df)
    plot_age_distribution(df)
    plot_heart_disease_by_sex(df)

# Run the main function to execute the heart disease analysis
main()

