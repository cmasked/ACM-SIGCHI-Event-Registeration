from flask import render_template, redirect, url_for, flash
from event import app
from event.forms import RegistrationForm
import json
import os

JSON_FILE = 'registrations.json'

# Ensure JSON file exists
if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, 'w') as f:
        json.dump([], f)


@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Read existing registrations
        with open(JSON_FILE, 'r') as f:
            registrations = json.load(f)

        # Append new registration
        registrations.append({
            'name': form.name.data,
            'email': form.email.data
        })

        # Write back to JSON
        with open(JSON_FILE, 'w') as f:
            json.dump(registrations, f, indent=4)

        flash('Registration successful!', 'success')
        return redirect(url_for('view_registrations'))

    if form.errors != {}:
        for err in form.errors.values():
            flash(f'Error: {err[0]}', 'danger')

    return render_template('register.html', form=form)


@app.route('/registrations')
def view_registrations():
    # Load all registrations
    with open(JSON_FILE, 'r') as f:
        registrations = json.load(f)

    return render_template('registrations.html', registrations=registrations)
