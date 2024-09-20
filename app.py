from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Initial inventory and unavailable toppings
inventory = ["ham", "pepperoni", "sausage", "anchovies", "mushrooms", "bell peppers", "green onion"]
unavailable_toppings = ["pepperoni"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer', methods=['GET', 'POST'])
def customer():
    if request.method == 'POST':
        if 'toppings' not in session:
            session['toppings'] = []
        
        if request.form.get('action') == 'add':
            topping = request.form.get('topping').lower()
            if topping in inventory and topping not in unavailable_toppings:
                session['toppings'].append(topping)
            return redirect(url_for('customer'))
        
        elif request.form.get('action') == 'remove':
            topping = request.form.get('topping').lower()
            if topping in session['toppings']:
                session['toppings'].remove(topping)
            return redirect(url_for('customer'))
        
        elif request.form.get('action') == 'finish':
            return redirect(url_for('finish'))

    return render_template('customer.html', inventory=inventory, toppings=session.get('toppings', []))

@app.route('/finish')
def finish():
    toppings = session.get('toppings', [])
    return render_template('finish.html', toppings=toppings)

@app.route('/employee', methods=['GET', 'POST'])
def employee():
    if request.method == 'POST':
        if request.form.get('password') == 'employee':
            if request.form.get('action') == 'add_inventory':
                new_item = request.form.get('new_item').lower()
                if new_item not in inventory:
                    inventory.append(new_item)
            elif request.form.get('action') == 'remove_inventory':
                remove_item = request.form.get('remove_item').lower()
                if remove_item in inventory:
                    inventory.remove(remove_item)
                    if remove_item in unavailable_toppings:
                        unavailable_toppings.remove(remove_item)
            elif request.form.get('action') == 'add_unavailable':
                unavailable_item = request.form.get('unavailable_item').lower()
                if unavailable_item in inventory and unavailable_item not in unavailable_toppings:
                    unavailable_toppings.append(unavailable_item)
            elif request.form.get('action') == 'remove_unavailable':
                remove_unavailable_item = request.form.get('remove_unavailable_item').lower()
                if remove_unavailable_item in unavailable_toppings:
                    unavailable_toppings.remove(remove_unavailable_item)
            return redirect(url_for('employee'))

    return render_template('employee.html', inventory=inventory, unavailable_toppings=unavailable_toppings)

if __name__ == '__main__':
    app.run(debug=True)