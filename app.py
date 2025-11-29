from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Временное хранилище результатов
results = {
    'option1': 0,
    'option2': 0,
    'option3': 0
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    selected_option = request.form.get('option')
    if selected_option in results:
        results[selected_option] += 1
    return redirect(url_for('results'))

@app.route('/results')
def show_results():
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
