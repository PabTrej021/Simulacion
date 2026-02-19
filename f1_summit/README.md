# Formula 1 Technical Summit 2026

A Flask-based informational website for a 1-day F1 technical conference.

## Features
- **Event Info**: Displays current date, Silverstone location, and schedule.
- **Schedule**: 8 technical sessions including "Physics of Ground Effect" and "2026 Engine Regulations".
- **Speakers**: List of speakers including Adrian Newey, Ross Brawn, and Toto Wolff.
- **Search**: Filter talks by Category (e.g., Aerodynamics), Speaker, or Title.
- **Internationalization**: Support for English and Spanish languages.
- **Theme**: Responsive design with F1-inspired Red, Black, and White styling.

## Prerequisites
- Python 3.x
- Flask

## Setup & Run

1.  **Navigate to the project directory**:
    ```bash
    cd f1_summit
    ```
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Application**:
    ```bash
    python app.py
    ```
4.  **Open in Browser**:
    Go to `http://127.0.0.1:5000`
    - For Spanish: `http://127.0.0.1:5000/?lang=es`

## Project Structure
- `app.py`: Backend logic, data models, and translations.
- `templates/index.html`: Main HTML template with dynamic text.
- `static/style.css`: F1 themed styles.
- `static/script.js`: Client-side search logic.
