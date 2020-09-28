from app import app


#Getting api key
api_key = api key['QUOTES_API_KEY']

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', title='TechNess')


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', title='TechNess')
