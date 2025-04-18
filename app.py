from flask import Flask, render_template, url_for, redirect

from customer import Customer
from customer_dao import CustomerDao
from customer_form import CustomerForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

title_app = 'Fit Zone Gym'


@app.route('/')
@app.route('/index.html')
def index():
    app.logger.debug('Navigated to main')
    # Get customers form DB
    customers_db = CustomerDao.get_all_customers()
    app.logger.debug('DB loaded')
    # Create an empty customer for form
    customer = Customer()
    customer_form = CustomerForm(obj=customer)
    return render_template('index.html', title=title_app, customers=customers_db, form=customer_form)


@app.route('/save', methods=['POST'])
def save():
    app.logger.debug('Navigated to save')
    customer = Customer()
    customer_form = CustomerForm(obj=customer)
    app.logger.debug('Check form')
    if customer_form.validate_on_submit():
        app.logger.debug('Form is valid')
        # If data is valid, populate the customer object
        customer_form.populate_obj(customer)
        # If id = None is a new customer, else update the existing one
        if customer.id is "":
            # Save the customer
            CustomerDao.add_customer(customer)
            app.logger.debug('New customer saved')
        else:
            # Update the customer
            CustomerDao.update_customer(customer)
            app.logger.debug('Customer updated')
        return redirect(url_for('index'))


@app.route('/clear')
def clear():
    app.logger.debug('Navigated to clear')
    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    app.logger.debug('Editing customer id: %s', id)
    customer = CustomerDao.get_customer_by_id(id)
    customer_form = CustomerForm(obj=customer)
    customers_db = CustomerDao.get_all_customers()
    return render_template('index.html', title=title_app, customers=customers_db, form=customer_form)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    app.logger.debug('Deleting customer id: %s', id)
    customer = CustomerDao.get_customer_by_id(id)
    CustomerDao.delete_customer(customer)
    customer_form = CustomerForm(obj=Customer())
    customers_db = CustomerDao.get_all_customers()
    return render_template('index.html', title=title_app, customers=customers_db, form=customer_form)


if __name__ == '__main__':
    app.run(debug=True)
