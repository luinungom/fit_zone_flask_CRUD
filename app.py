from flask import Flask, render_template

from customer_dao import CustomerDao

app = Flask(__name__)

title_app = 'Fit Zone Gym'


@app.route('/')
@app.route('/index.html')
def index():
    app.logger.debug('Navigated to main')
    # Get customers form DB
    customers_db = CustomerDao.get_all_customers()
    app.logger.debug('DB loaded')
    return render_template('index.html', title=title_app, customers=customers_db)

if __name__ == '__main__':
    app.run(debug=True)
