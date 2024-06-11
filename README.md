# Food Recipes Rating System Based on Sentiment Analysis

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project is a Food Recipes Rating System that utilizes sentiment analysis to rate reviews. Reviews are analyzed using an LSTM model to determine their sentiment, which then translates into a numerical rating from 1 to 5. The system is built using Django for the backend, and it incorporates NLTK and Scikit-learn for natural language processing and machine learning.

## Features
- User authentication using GitHub OAuth
- Recipe posting with detailed descriptions and images
- Review submission with sentiment-based rating (1 to 5)
- Sentiment analysis using a custom LSTM model
- Email notifications through Google API

## Tech Stack
- **Backend:** Django
- **Natural Language Processing:** NLTK, Scikit-learn
- **Machine Learning Model:** LSTM (Long Short-Term Memory)
- **Authentication:** GitHub OAuth
- **Email Service:** Google API
- **Database:** SQLite (default Django setup)

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/food-recipes-rating-system.git
    cd food-recipes-rating-system
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage
1. **Navigate to the homepage:**
    Open your web browser and go to `http://127.0.0.1:8000/`.

2. **Sign in using GitHub:**
    Use GitHub OAuth to authenticate and access the platform.

3. **Post a recipe:**
    Create a new recipe by filling out the form with the required details.

4. **Submit a review:**
    Leave a review for any recipe. The sentiment of your review will be analyzed, and a rating from 1 to 5 will be assigned based on the sentiment score.


## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

1. **Fork the repository**
2. **Create your feature branch (`git checkout -b feature/your-feature`)**
3. **Commit your changes (`git commit -am 'Add some feature'`)**
4. **Push to the branch (`git push origin feature/your-feature`)**
5. **Open a pull request**

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
