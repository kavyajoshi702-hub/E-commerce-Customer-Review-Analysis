# E-Commerce Customer Review Sentiment Analysis Using Machine Learning and AI

A Python desktop application for classifying e-commerce customer reviews into positive, negative, and neutral sentiment categories. The interface is built with Tkinter and the project uses a scikit-learn model and text-processing workflow.

## Features
- Desktop interface built with Tkinter
- Customer review sentiment prediction
- Login, signup, and password-reset screens
- Dataset and model-training script included
- Supporting charts and model evaluation scripts

## Technologies
Python, Tkinter, Pandas, scikit-learn, joblib, Matplotlib, Pillow, SQLite, NLP / TF-IDF.

## Project files
- `Home_Screen.py`: application home screen
- `Login_Screen.py`, `Signup_Screen.py`: authentication screens
- `Forget_Screen.py`: password reset by email (requires configuration; see below)
- `Main_Screen.py`: sentiment-analysis interface
- `Dashboard_Screen.py`: dashboard interface
- `train_model.py`: trains and saves the model
- `Customer_Sentiment_30000.csv`: dataset used by the training script
- `Pictures/`: UI images

## Setup
1. Install Python 3.10 or later (Python 3.12 is a reasonable choice for compatibility with scientific packages).
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure `sentiment_model.pkl` is present in the project folder. If it is not included or you want to retrain it, run:
   ```bash
   python train_model.py
   ```
5. Start the application by running the appropriate entry-point screen, for example:
   ```bash
   python Home_Screen.py
   ```

## Password-reset email configuration
For security, no email app password is included in this repository. To enable Gmail password-reset email, set the environment variable `SENTIMENT_GMAIL_APP_PASSWORD` to a Gmail App Password on your own machine before running the app. Never commit credentials to GitHub.

## Notes
- SQLite creates a local `test1.db` database when the application runs. The database is intentionally not included because it may contain user information.
- Image and dataset paths have been changed to project-relative paths where applicable.
- Verify all screens and model predictions in your environment before relying on the application.
- Do not claim a specific model accuracy unless it is supported by a reproducible evaluation.

## Author
Kavya

## License
This project is distributed under the MIT License.
