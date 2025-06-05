from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

companies = [
    {"Company":"SoftTech Solutions", "Industry":"Software", "Location":"New York, NY", "Employees":150, "Revenue":15, "Email":"contact@softtech.com"},
    {"Company":"DevHub", "Industry":"Software", "Location":"San Francisco, CA", "Employees":300, "Revenue":35, "Email":"hello@devhub.com"},
    {"Company":"HealthPlus Medical", "Industry":"Healthcare", "Location":"New York, NY", "Employees":200, "Revenue":25, "Email":"contact@healthplus.com"},
    {"Company":"Generic Corp", "Industry":"Consulting", "Location":"Chicago, IL", "Employees":50, "Revenue":5, "Email":"contact@genericcorp.com"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    industry = data.get('industry', '').lower()
    location = data.get('location', '').lower()
    emp_min = int(data.get('empMin', 0))
    emp_max = int(data.get('empMax', 100000))
    rev_min = float(data.get('revMin', 0))
    rev_max = float(data.get('revMax', 100000))

    filtered = [c for c in companies if
                industry in c['Industry'].lower() and
                location in c['Location'].lower() and
                emp_min <= c['Employees'] <= emp_max and
                rev_min <= c['Revenue'] <= rev_max]

    return jsonify(filtered)

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
