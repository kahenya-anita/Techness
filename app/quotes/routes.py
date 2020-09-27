from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from app import db
from app.models import Quote
from app.quotes.forms import PostForm

quotes = Blueprint('quotes', __name__)


@quotes.route("/quote/new", methods=['GET', 'POST'])
@login_required
def new_quote():
    form = QuoteForm()
    if form.validate_on_submit():
        quote = Quote(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your quote has been created!', 'success')
        return redirect(url_for('main.about'))
    return render_template('create_quote.html', title='New Quote',
                           form=form, legend='New Quote')


@quotes.route("/quote/<int:post_id>")
def quote(quote_id):
    quote = Quote.query.get_or_404(quote_id)
    return render_template('quote.html', title=quote.title, quote=quote)


@quotes.route("/quote/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_quote(post_id):
    quote = Quote.query.get_or_404(post_id)
    if quote.author != current_user:
        abort(403)
    form = QuoteForm()
    if form.validate_on_submit():
        quote.title = form.title.data
        quote.content = form.content.data
        db.session.commit()
        flash('Your quote has been updated!', 'success')
        return redirect(url_for('main.about', quote_id=quote.id))
    elif request.method == 'GET':
        form.title.data = quote.title
        form.content.data = quote.content
    return render_template('create_quote.html', title='Update Quote',
                           form=form, legend='Update Quote')


@quotes.route("/quote/<int:quote_id>/delete", methods=['POST'])
@login_required
def delete_quote(quote_id):
    quote = Quote.query.get_or_404(quote_id)
    if quote.author != current_user:
        abort(403)
    db.session.delete(quote)
    db.session.commit()
    flash('Your quote has been deleted!', 'success')
    return redirect(url_for('main.about'))


