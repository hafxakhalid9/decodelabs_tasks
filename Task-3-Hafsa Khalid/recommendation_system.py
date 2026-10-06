import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample Item Dataset (Movies/Courses/Products)
dataset = {
    "Title": [
        "Python for Beginners",
        "Data Science Foundations",
        "Machine Learning Mastery",
        "Web Development Bootcamp",
        "Deep Learning Basics",
        "Automate the Boring Stuff with Python"
    ],
    "Tags": [
        "python programming coding automation beginner",
        "data science python statistics analysis machine learning",
        "machine learning python scikit-learn algorithms data",
        "web development html css javascript frontend backend",
        "deep learning neural networks python tensorflow pytorch",
        "python automation scripting beginner coding"
    ]
}

df = pd.DataFrame(dataset)

def recommend(user_interest, top_n=2):
    # Vectorize text tags and user input
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df["Tags"].tolist() + [user_interest])
    
    # Calculate similarity between user input and dataset items
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    scores = cosine_sim.flatten()
    
    # Get top matching indices
    top_indices = scores.argsort()[-top_n:][::-1]
    
    results = df.iloc[top_indices].copy()
    results["Match Score"] = [round(scores[i] * 100, 2) for i in top_indices]
    return results[["Title", "Match Score"]]

# Replace lines 44-50 in your recommendation_system.py with this:
if __name__ == "__main__":
    print("=== Simple Recommendation System ===")
    print("Type 'exit' or 'quit' to end the program.\n")
    
    while True:
        user_input = input("\nEnter your preferences/interests: ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
            
        if not user_input:
            print("Please enter at least one keyword.")
            continue
            
        print("\nRecommended for you:")
        recommendations = recommend(user_input)
        print(recommendations.to_string(index=False))