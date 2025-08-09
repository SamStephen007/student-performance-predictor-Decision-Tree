from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open('student_performance_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['hours']),
            float(request.form['scores']),
            1 if request.form['extra'] == 'Yes' else 0,
            float(request.form['sleep']),
            float(request.form['papers'])
        ]
        prediction = model.predict([features])[0]
        label_map = {0: 'Low', 1: 'Medium', 2: 'High'}
        result = label_map[prediction]
        return render_template('index.html', prediction_text=f'Predicted Performance: {result}')
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
