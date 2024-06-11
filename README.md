Food Recipes Rating System Based on Sentiment Analysis
Overview
This project is a comprehensive food recipes rating system that utilizes sentiment analysis to rate reviews. Built using Django, it leverages Natural Language Toolkit (NLTK) and Scikit-Learn for natural language processing and sentiment analysis, along with a Long Short-Term Memory (LSTM) model for accurate sentiment prediction. The system also integrates with the Google API for email functionalities and GitHub OAuth for user authentication. Users can post recipes, leave reviews, and see review ratings ranging from 1 to 5 based on the sentiment determined by our custom-built LSTM model.

Features
Recipe Posting: Users can post their food recipes.
Review Rating: Reviews are rated from 1 to 5 based on sentiment analysis.
Sentiment Analysis: Uses NLTK and Scikit-Learn for text processing and an LSTM model for sentiment prediction.
Email Integration: Utilizes Google API for sending emails.
User Authentication: GitHub OAuth for secure user authentication.
Technologies Used
Backend Framework: Django
Natural Language Processing: NLTK, Scikit-Learn
Machine Learning: Custom LSTM Model
APIs: Google API for email, GitHub OAuth
Database: SQLite (default with Django, can be configured to use other databases)
Frontend: HTML, CSS, JavaScript
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/food-recipes-rating-system.git
cd food-recipes-rating-system
Create and Activate Virtual Environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables
Create a .env file in the root directory and add your Google API and GitHub OAuth credentials:

env
Copy code
GOOGLE_API_KEY=your_google_api_key
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
Run Migrations

bash
Copy code
python manage.py migrate
Run the Development Server

bash
Copy code
python manage.py runserver
Usage
Sign Up/Login: Use GitHub OAuth to sign up or log in.
Post Recipes: Navigate to the "Post Recipe" section to add your food recipes.
Leave Reviews: Leave reviews for posted recipes.
View Ratings: Reviews will be rated from 1 to 5 based on their sentiment as determined by the LSTM model.
Sentiment Analysis
The sentiment analysis component uses NLTK and Scikit-Learn for initial text processing, and an LSTM model for determining the sentiment of the reviews. The ratings are as follows:

1: Very Negative
2: Negative
3: Neutral
4: Positive
5: Very Positive
Contributing
We welcome contributions! Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/your-feature-name).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions or suggestions, please feel free to contact me at your-email@example.com.

