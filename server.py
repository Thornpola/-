"""
Pola Entertainment - Flask Development Server
Run: python server.py
"""

from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime
import json

app = Flask(__name__, static_folder='public', static_url_path='')
CORS(app)

# Configuration
PORT = 3000
HOST = 'localhost'
DEBUG = True

# Portfolio data
PORTFOLIO_DATA = [
    {
        "id": 0,
        "title": "ការណែនាំអំពីកម្មវិធី SPSS",
        "description": "SPSS គឺជាសំណុំ ប្រើដើម្បីវិភាគទិន្នន័យប្រកបដោយប្រសិទ្ធភាព",
        "image": "/images/Jpg.jpg",
        "pdf": "/pdfs/ការណែនាំអំពីកម្មវិធី_SPSS.pdf"
    },
    {
        "id": 1,
        "title": "គំរូប្លង់ RCBD",
        "description": "ការវិភាគទិន្នន័យតាមកម្មវិធីSPSSគំរូប្លង់ RCBD",
        "image": "/images/2.jpg",
        "pdf": "/pdfs/RCBD.pdf"
    },
    {
        "id": 2,
        "title": "ការរៀបចំផែនការពិសោធន៍",
        "description": "ការរៀបចំផែការសាកល្បងដោយចៃដន្យនៅក្នុងប្លុងពេញលេញ",
        "image": "/images/3.jpg",
        "pdf": "/pdfs/RCB.pdf"
    },
    {
        "id": 3,
        "title": "Structural Beauty",
        "description": "Modern lines and timeless designs",
        "image": "https://picsum.photos/id/104/500/600",
        "pdf": ""
    },
    {
        "id": 4,
        "title": "Style & Elegance",
        "description": "High fashion and editorial shoots",
        "image": "https://picsum.photos/id/30/500/600",
        "pdf": ""
    },
    {
        "id": 5,
        "title": "Wild Kingdom",
        "description": "Nature's magnificent creatures",
        "image": "https://picsum.photos/id/107/500/600",
        "pdf": ""
    },
    {
        "id": 6,
        "title": "Timeless Classics",
        "description": "The art of black and white",
        "image": "https://picsum.photos/id/42/500/600",
        "pdf": ""
    },
    {
        "id": 7,
        "title": "Special Moments",
        "description": "Weddings and celebrations",
        "image": "https://picsum.photos/id/169/500/600",
        "pdf": ""
    },
    {
        "id": 8,
        "title": "Creative Vision",
        "description": "Artistic and experimental works",
        "image": "https://picsum.photos/id/96/500/600",
        "pdf": ""
    }
]

# API Routes

@app.route('/api/config')
def get_config():
    """Return server configuration"""
    env = os.getenv('FLASK_ENV', 'development')
    base_url = f'http://{HOST}:{PORT}'
    
    return jsonify({
        'environment': env,
        'baseUrl': base_url,
        'apiUrl': f'{base_url}/api',
        'contactEmail': 'thornpola6@gmail.com',
        'phone': '+855 88 455 4566'
    })

@app.route('/api/portfolio')
def get_portfolio():
    """Return portfolio items"""
    return jsonify({
        'success': True,
        'data': PORTFOLIO_DATA
    })

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        
        # Validation
        if not data.get('name') or not data.get('email') or not data.get('message'):
            return jsonify({
                'success': False,
                'message': 'Missing required fields: name, email, message'
            }), 400
        
        # Log the contact
        contact_log = {
            'timestamp': datetime.now().isoformat(),
            'name': data.get('name'),
            'email': data.get('email'),
            'subject': data.get('subject', 'No subject'),
            'message': data.get('message')
        }
        
        print(f"\n📧 New Contact Message:")
        print(json.dumps(contact_log, indent=2, ensure_ascii=False))
        
        # TODO: In production, send email here using smtplib or service
        
        return jsonify({
            'success': True,
            'message': 'Message received! We will get back to you soon.'
        })
    
    except Exception as e:
        print(f"❌ Error processing contact: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Error processing your message'
        }), 500

@app.route('/')
def index():
    """Serve the main HTML file"""
    return send_from_directory('public', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files from public directory"""
    return send_from_directory('public', filename)

@app.errorhandler(404)
def not_found(error):
    """Serve index.html for all unknown routes (SPA support)"""
    return send_from_directory('public', 'index.html')

if __name__ == '__main__':
    print(f"""
╔══════════════════════════════════════════════════════════╗
║         🎬 Pola Entertainment Server Started             ║
╠══════════════════════════════════════════════════════════╣
║ Server URL:  http://{HOST}:{PORT}
║ Environment: {os.getenv('FLASK_ENV', 'development')}
║ Port:        {PORT}
║ Host:        {HOST}
║ Debug:       {DEBUG}
╚══════════════════════════════════════════════════════════╝
    """)
    
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
        use_reloader=True
    )
