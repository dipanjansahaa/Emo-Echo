import numpy as np
import pandas as pd

# Set the number of samples
num_samples = 100000

# Define emotion categories with ranges for emotion score, heart rate, and depression score
emotion_data = {
    "Happy": {"Score_Range": (0.0, 0.1), "HR_Range": (60, 80), "Depression_Range": (0, 5)},
    "Angry": {"Score_Range": (0.7, 0.9), "HR_Range": (90, 120), "Depression_Range": (10, 20)},
    "Sad": {"Score_Range": (0.6, 0.8), "HR_Range": (70, 90), "Depression_Range": (15, 25)},
    "Cry": {"Score_Range": (0.8, 1.0), "HR_Range": (100, 130), "Depression_Range": (20, 30)},
    "Surprise": {"Score_Range": (0.4, 0.6), "HR_Range": (80, 110), "Depression_Range": (5, 15)},
    "Disgust": {"Score_Range": (0.5, 0.7), "HR_Range": (80, 100), "Depression_Range": (10, 20)},
    "Fear": {"Score_Range": (0.8, 1.0), "HR_Range": (100, 140), "Depression_Range": (20, 30)},
}

# List of all emotions
emotions = list(emotion_data.keys())

# Generate random data for 10,000 samples
emotion_scores = []
heart_rates = []
depression_scores = []

for _ in range(num_samples):
    emotion = np.random.choice(emotions)
    score_min, score_max = emotion_data[emotion]["Score_Range"]
    hr_min, hr_max = emotion_data[emotion]["HR_Range"]
    dep_min, dep_max = emotion_data[emotion]["Depression_Range"]

    # Generate random emotion score, heart rate, and depression score within their respective ranges
    if np.random.rand() < 0.9:  # 95% normal cases
        emotion_score = float(f"{np.random.uniform(score_min, score_max):.2f}")
        heart_rate = np.random.randint(hr_min, hr_max + 1)
        depression_score = np.random.randint(dep_min, dep_max + 1)
    else:  # 10% extraordinary cases
        emotion_score = float(f"{np.random.uniform(0.8, 1.0) if np.random.rand() > 0.5 else np.random.uniform(0.0, 0.1):.2f}")
        heart_rate = np.random.choice([np.random.randint(60, 65), np.random.randint(135, 150)])
        depression_score = np.random.choice([np.random.randint(0, 3), np.random.randint(28, 31)])

    emotion_scores.append(emotion_score)
    heart_rates.append(heart_rate)
    depression_scores.append(depression_score)

# Create DataFrame with the generated data
data_set = pd.DataFrame({
    'Emotion_Score': emotion_scores,
    'Heart_Rate': heart_rates,
    'Depression_Score': depression_scores
})

# Save the dataset to a CSV file
file_path = 'synthetic_anxiety_dataset_100000_1.csv'
data_set.to_csv(file_path, index=False)

print(f"Dataset saved to {file_path}")
