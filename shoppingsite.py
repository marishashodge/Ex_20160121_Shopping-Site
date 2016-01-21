"""Ubermelon shopping application Flask server.

Provides web interface for browsing melons, seeing detail about a melon, and
put melons in a shopping cart.

Authors: Joel Burton, Christian Fernandez, Meggie Mahnken.
"""


from flask import Flask, render_template, redirect, flash, session, request
import jinja2

import melons


app = Flask(__name__)

# Need to use Flask sessioning features

app.secret_key = 'fjakjdfafkjddkfj375'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.

app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/melons")
def list_melons():
    """Return page showing all the melons ubermelon has to offer"""

    melon_list = melons.get_all()
    return render_template("all_melons.html",
                           melon_list=melon_list)


@app.route("/melon/<int:melon_id>")
def show_melon(melon_id):
    """Return page showing the details of a given melon.

    Show all info about a melon. Also, provide a button to buy that melon.
    """

    melon = melons.get_by_id(melon_id)
    return render_template("melon_details.html",
                           display_melon=melon)


@app.route("/cart")
def shopping_cart():
    """Display content of shopping cart."""

    # TODO: Display the contents of the shopping cart.

    # The logic here will be something like:
    #find a secret key, and once everything is set up, try to put something in the session and then print it out).
    # - get the list-of-ids-of-melons from the session cart
    # - loop over this list:
    #   - keep track of information about melon types in the cart
    #   - keep track of the total amt ordered for a melon-type
    #   - keep track of the total amt of the entire order
    # - hand to the template the total order cost and the list of melon types


    # melon_ids_in_cart = sessions['cart']
    # total = 0
    # for i in range(len(melon_ids_in_cart)):
    #
    # loop over list and create dict with id = key and qty = value
    # loop through this list to extract melon data
    # make a new dict with melon id as key; value is name, qty, price

    # total += _____

    return render_template("cart.html", session=session)


@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    """Add a melon to cart and redirect to shopping cart page.

    When a melon is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Successfully added to cart'.
    """
    qty = int(request.args.get("qty"))
    print '\n\n\n',qty,'\n\n\n'

    print "session is ", session
    if 'cart' in session:
        if qty > 1:
            for i in range(qty-1):
                session['cart'].append(id)
        session['cart'].append(id)
    else:
        session["cart"] = [id]

    print "session is ", session
    print "Cart: ", session['cart']

    # Need to eventually add flash message here "successfully added to cart"

    #melon_list = melons.get_all()
    
    
    
    return redirect("/cart")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    # TODO: Need to implement this!

    return "Oops! This needs to be implemented"


@app.route("/checkout")
def checkout():
    """Checkout customer, process payment, and ship melons."""

    # For now, we'll just provide a warning. Completing this is beyond the
    # scope of this exercise.

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/melons")


if __name__ == "__main__":
    app.run(debug=True)
