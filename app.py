from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Dummy Data
SPEAKERS = [
    {"id": 1, "first_name": "Alice", "last_name": "Johnson", "linkedin": "https://www.linkedin.com/in/alicejohnson"},
    {"id": 2, "first_name": "Bob", "last_name": "Smith", "linkedin": "https://www.linkedin.com/in/bobsmith"},
    {"id": 3, "first_name": "Charlie", "last_name": "Davis", "linkedin": "https://www.linkedin.com/in/charliedavis"},
    {"id": 4, "first_name": "Diana", "last_name": "Evans", "linkedin": "https://www.linkedin.com/in/dianaevans"},
    {"id": 5, "first_name": "Evan", "last_name": "Wright", "linkedin": "https://www.linkedin.com/in/evanwright"},
    {"id": 6, "first_name": "Fiona", "last_name": "Green", "linkedin": "https://www.linkedin.com/in/fionagreen"},
    {"id": 7, "first_name": "George", "last_name": "Hall", "linkedin": "https://www.linkedin.com/in/georgehall"},
    {"id": 8, "first_name": "Hannah", "last_name": "Lee", "linkedin": "https://www.linkedin.com/in/hannahlee"},
]

TALKS = [
    {
        "id": 101,
        "title": "Welcome & Keynote: Future of Google Cloud",
        "speakers": [SPEAKERS[0]],
        "category": "Keynote",
        "description": "Kickoff the event with an overview of the latest innovations in Google Cloud Platform.",
        "time": "09:00 - 10:00"
    },
    {
        "id": 102,
        "title": "Mastering Kubernetes on GKE",
        "speakers": [SPEAKERS[1], SPEAKERS[2]],
        "category": "Infrastructure",
        "description": "Deep dive into managing containerized applications with Google Kubernetes Engine.",
        "time": "10:15 - 11:15"
    },
    {
        "id": 103,
        "title": "BigQuery for Data Warehousing",
        "speakers": [SPEAKERS[3]],
        "category": "Data & Analytics",
        "description": "Learn how to store and analyze petabytes of data using BigQuery.",
        "time": "11:30 - 12:30"
    },
    {
        "id": 104,
        "title": "Lunch Break",
        "speakers": [],
        "category": "Break",
        "description": "Enjoy a networking lunch.",
        "time": "12:30 - 13:30"
    },
    {
        "id": 105,
        "title": "Building Serverless Apps with Cloud Run",
        "speakers": [SPEAKERS[4]],
        "category": "App Development",
        "description": "Deploy scalable containerized applications without managing infrastructure.",
        "time": "13:30 - 14:30"
    },
    {
        "id": 106,
        "title": "Introduction to Vertex AI",
        "speakers": [SPEAKERS[5], SPEAKERS[6]],
        "category": "AI & ML",
        "description": "Get started with building and deploying machine learning models on Vertex AI.",
        "time": "14:45 - 15:45"
    },
    {
        "id": 107,
        "title": "Security Best Practices in GCP",
        "speakers": [SPEAKERS[7]],
        "category": "Security",
        "description": "Protect your cloud resources with Google Cloud's security tools and best practices.",
        "time": "16:00 - 17:00"
    },
    {
        "id": 108,
        "title": "Closing Remarks & Networking",
        "speakers": [SPEAKERS[0]],
        "category": "Keynote",
        "description": "Wrap up the day with key takeaways and networking opportunities.",
        "time": "17:15 - 18:00"
    }
]

@app.route("/")
def index():
    today = datetime.date.today().strftime("%B %d, %Y")
    location = "Google Tech Hub, San Francisco, CA"
    return render_template("index.html", talks=TALKS, date=today, location=location)

if __name__ == "__main__":
    app.run(debug=True)
