from flask import Flask, render_template, request, jsonify, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        
        # Extract form data
        first_name = data.get('firstName', '')
        last_name = data.get('lastName', '')
        email = data.get('email', '')
        interest = data.get('interest', '')
        message = data.get('message', '')
        
        # Basic validation
        if not all([first_name, last_name, email, message]):
            return jsonify({'success': False, 'message': 'Please fill in all required fields.'}), 400
        
        # In a real application, you would:
        # 1. Save to database
        # 2. Send email notification
        # 3. Log the contact request
        
        # For now, we'll just return success
        return jsonify({
            'success': True, 
            'message': 'Thank you for your message! I\'ll get back to you soon.'
        })
        
    except Exception as e:
        return jsonify({'success': False, 'message': 'An error occurred. Please try again.'}), 500

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(debug=True) 