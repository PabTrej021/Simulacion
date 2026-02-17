from flask import Flask, render_template
import datetime

app = Flask(__name__)

# --- Data Models & Dummy Data ---

# Speakers
SPEAKERS = [
    {"id": 1, "first_name": "Adrian", "last_name": "Newey", "linkedin": "https://www.linkedin.com/in/adriannewey-unofficial"},
    {"id": 2, "first_name": "Ross", "last_name": "Brawn", "linkedin": "https://www.linkedin.com/in/rossbrawn"},
    {"id": 3, "first_name": "James", "last_name": "Allison", "linkedin": "https://www.linkedin.com/in/jamesallison"},
    {"id": 4, "first_name": "Toto", "last_name": "Wolff", "linkedin": "https://www.linkedin.com/in/toto-wolff"},
    {"id": 5, "first_name": "Christian", "last_name": "Horner", "linkedin": "https://www.linkedin.com/in/christianhorner"},
    {"id": 6, "first_name": "Mario", "last_name": "Isola", "linkedin": "https://www.linkedin.com/in/marioisola"},
    {"id": 7, "first_name": "Hannah", "last_name": "Schmitz", "linkedin": "https://www.linkedin.com/in/hannahschmitz"},
    {"id": 8, "first_name": "Rob", "last_name": "Smedley", "linkedin": "https://www.linkedin.com/in/robsmedley"},
]

# Talks
# Translations
UI_TEXT = {
    "en": {
        "title": "Formula 1 Technical Summit 2026",
        "search_placeholder": "Search strategy, aerodynamics, speakers...",
        "search_btn": "Please Box (Search)",
        "schedule_title": "Race Schedule",
        "presented_by": "Presented by:",
        "no_results": "No telemetry found matching your query.",
        "footer": "© 2026 F1 Technical Summit. Not officially affiliated with Formula One World Championship Limited.",
        "lang_switch": "Español",
        "lang_link": "?lang=es"
    },
    "es": {
        "title": "Cumbre Técnica de Fórmula 1 2026",
        "search_placeholder": "Buscar estrategia, aerodinámica, oradores...",
        "search_btn": "Box Box (Buscar)",
        "schedule_title": "Horario de Carrera",
        "presented_by": "Presentado por:",
        "no_results": "No se encontró telemetría para su búsqueda.",
        "footer": "© 2026 F1 Technical Summit. No afiliado oficialmente con Formula One World Championship Limited.",
        "lang_switch": "English",
        "lang_link": "?lang=en"
    }
}

TALKS = {
    "en": [
        {
            "id": 101,
            "title": "Opening Keynote: The Future of F1 Engineering",
            "speakers": [SPEAKERS[1]], # Ross Brawn
            "category": "Regulations",
            "description": "A look ahead at the 2026 technical regulations and beyond.",
            "time": "09:00 - 10:00"
        },
        {
            "id": 102,
            "title": "The Physics of Ground Effect",
            "speakers": [SPEAKERS[0]], # Adrian Newey
            "category": "Aerodynamics",
            "description": "Understanding the complexities of underfloor aerodynamics and porpoising mitigation.",
            "time": "10:15 - 11:15"
        },
        {
            "id": 103,
            "title": "Undercut vs. Overcut Strategies",
            "speakers": [SPEAKERS[6]], # Hannah Schmitz
            "category": "Strategy",
            "description": "Data-driven decision making on the pit wall: when to box and why.",
            "time": "11:30 - 12:30"
        },
        {
            "id": 104,
            "title": "Paddock Lunch Break",
            "speakers": [],
            "category": "Break",
            "description": "Networking lunch with fellow engineers and enthusiasts.",
            "time": "12:30 - 13:30"
        },
        {
            "id": 105,
            "title": "2026 Engine Regulations: The Hybrid Challenge",
            "speakers": [SPEAKERS[3], SPEAKERS[4]], # Toto & Christian (Fun duo)
            "category": "Power Units",
            "description": "Discussing the shift to 50% electrical power and sustainable fuels.",
            "time": "13:30 - 14:30"
        },
        {
            "id": 106,
            "title": "Tire Degradation Analysis",
            "speakers": [SPEAKERS[5]], # Mario Isola
            "category": "Tires",
            "description": "Understanding thermal degradation, graining, and blistering.",
            "time": "14:45 - 15:45"
        },
        {
            "id": 107,
            "title": "CFD vs. Wind Tunnel Correlation",
            "speakers": [SPEAKERS[2]], # James Allison
            "category": "Aerodynamics",
            "description": "Bridging the gap between simulation and reality in car development.",
            "time": "16:00 - 17:00"
        },
        {
            "id": 108,
            "title": "Data Telemetry & Real-time Analytics",
            "speakers": [SPEAKERS[7]], # Rob Smedley
            "category": "Data Science",
            "description": "How teams process terabytes of data during a race weekend.",
            "time": "17:15 - 18:00"
        }
    ],
    "es": [
        {
            "id": 101,
            "title": "Discurso de Apertura: El Futuro de la Ingeniería en F1",
            "speakers": [SPEAKERS[1]],
            "category": "Regulaciones",
            "description": "Una mirada a las regulaciones técnicas de 2026 y más allá.",
            "time": "09:00 - 10:00"
        },
        {
            "id": 102,
            "title": "La Física del Efecto Suelo",
            "speakers": [SPEAKERS[0]],
            "category": "Aerodinámica",
            "description": "Entendiendo las complejidades de la aerodinámica del suelo y la mitigación del marsopeo.",
            "time": "10:15 - 11:15"
        },
        {
            "id": 103,
            "title": "Estrategias de Undercut vs. Overcut",
            "speakers": [SPEAKERS[6]],
            "category": "Estrategia",
            "description": "Toma de decisiones basada en datos en el muro de boxes: cuándo parar y por qué.",
            "time": "11:30 - 12:30"
        },
        {
            "id": 104,
            "title": "Almuerzo en el Paddock",
            "speakers": [],
            "category": "Descanso",
            "description": "Almuerzo de networking con compañeros ingenieros y entusiastas.",
            "time": "12:30 - 13:30"
        },
        {
            "id": 105,
            "title": "Regulaciones de Motores 2026: El Desafío Híbrido",
            "speakers": [SPEAKERS[3], SPEAKERS[4]],
            "category": "Unidad de Potencia",
            "description": "Discutiendo el cambio al 50% de energía eléctrica y combustibles sostenibles.",
            "time": "13:30 - 14:30"
        },
        {
            "id": 106,
            "title": "Análisis de Degradación de Neumáticos",
            "speakers": [SPEAKERS[5]],
            "category": "Neumáticos",
            "description": "Entendiendo la degradación térmica, el graining y el blistering.",
            "time": "14:45 - 15:45"
        },
        {
            "id": 107,
            "title": "Correlación CFD vs. Túnel de Viento",
            "speakers": [SPEAKERS[2]],
            "category": "Aerodinámica",
            "description": "Puenteando la brecha entre la simulación y la realidad en el desarrollo del coche.",
            "time": "16:00 - 17:00"
        },
        {
            "id": 108,
            "title": "Telemetría de Datos y Analítica en Tiempo Real",
            "speakers": [SPEAKERS[7]],
            "category": "Ciencia de Datos",
            "description": "Cómo los equipos procesan terabytes de datos durante un fin de semana de carrera.",
            "time": "17:15 - 18:00"
        }
    ]
}

from flask import request

@app.route("/")
def index():
    today = datetime.date.today().strftime("%B %d, %Y")
    location = "Silverstone Circuit Conference Center"
    
    lang = request.args.get('lang', 'en')
    if lang not in ['en', 'es']:
        lang = 'en'
        
    talks_data = TALKS[lang]
    ui_data = UI_TEXT[lang]
    
    return render_template("index.html", talks=talks_data, ui=ui_data, date=today, location=location)

if __name__ == "__main__":
    app.run(debug=True)
