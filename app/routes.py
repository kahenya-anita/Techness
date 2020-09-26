from app import app

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', title='TechNess')


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', title='TechNess')
