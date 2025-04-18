from mysql.connector import Error

from connection import Connection
from customer import Customer


class CustomerDao:
    SELECT = 'SELECT * FROM customers ORDER BY id'
    SELECT_ID = 'SELECT * FROM customers WHERE id = %s'
    INSERT = 'INSERT INTO customers (name, surname, membership) VALUES (%s, %s, %s)'
    UPDATE = 'UPDATE customers SET name = %s, surname = %s, membership = %s WHERE id = %s'
    DELETE = 'DELETE FROM customers WHERE id = %s'

    @classmethod
    def get_all_customers(cls):
        try:
            with Connection.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(cls.SELECT)
                    customers_in_db = []
                    for register in cursor.fetchall():
                        new_customer = Customer(register[0], register[1], register[2], register[3])
                        customers_in_db.append(new_customer)
                    return customers_in_db
        except Error as e:
            print(f'Error getting all customers: {e}')

    @classmethod
    def add_customer(cls, customer):
        try:
            with Connection.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(cls.INSERT, (customer.name, customer.surname, customer.membership))
                    connection.commit()
        except Error as e:
            print(f'Error adding customer: {e}')

    @classmethod
    def update_customer(cls, customer):
        try:
            with Connection.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(cls.UPDATE, (customer.name, customer.surname, customer.membership, customer.id))
                    connection.commit()
        except Error as e:
            print(f'Error updating customer: {e}')

    @classmethod
    def delete_customer(cls, customer):
        try:
            with Connection.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(cls.DELETE, (customer.id,))
                    connection.commit()
        except Error as e:
            print(f'Error deleting customer: {e}')

    @classmethod
    def get_customer_by_id(cls, customer_id):
        try:
            with Connection.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(cls.SELECT_ID, (customer_id,))
                    register = cursor.fetchone()
                    return Customer(register[0], register[1], register[2], register[3])
        except Error as e:
            print(f'Error getting customer by id: {e}')
