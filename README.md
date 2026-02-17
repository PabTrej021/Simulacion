# Google Cloud Tech Conference Website

This is a simple Flask-based website for a 1-day Google Cloud technical conference.

## Features
- Displays event date, location, and schedule.
- Lists 8 talks with speaker details.
- Search functionality by Title, Speaker, or Category.
- Responsive design.

## Prerequisites
- Python 3.x
- Flask

## Setup & Run

1.  **Clone or Download** the project.
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

## Project Structure
- `app.py`: Backend logic and data.
- `templates/index.html`: Frontend HTML.
- `static/style.css`: Styling.
- `static/script.js`: Search logic.
