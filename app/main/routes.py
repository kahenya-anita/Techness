from flask import render_template, request, Blueprint
from app.models import Quote

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', title='TechNess')


@main.route("/about")
def about():
    page = request.args.get('page', 1, type=int)
    quotes = quote.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('about.html', quotes=quotes)