from customer import Customer
from customer_dao import CustomerDao


class FitZone:

    def __init__(self):
        self.customer_dao = CustomerDao()

    def fit_zone(self):
        operation_ended: bool = False
        print('*** Welcome to Fit Zone customers management ***')
        for customer in CustomerDao.get_all_customers():
            print(customer)
        while not operation_ended:
            option = self.show_menu()
            operation_ended = self.execute_operation(option)

    def show_menu(self):
        print('Operations: (1-5)')
        print('1. Add a customer')
        print('2. Update a customer')
        print('3. Delete a customer')
        print('4. Show all customers')
        print('5. Exit')
        try:
            return int(input('Select an option: '))
        except ValueError:
            print('Invalid option')

    def execute_operation(self, option):
        if option == 1:
            self.add_customer()
        elif option == 2:
            self.update_customer()
        elif option == 3:
            self.delete_customer()
        elif option == 4:
            self.show_all_customers()
        elif option == 5:
            return True
        else:
            print('Option not available')
        return False

    def add_customer(self):
        try:
            print('New customer info')
            name = input('Name: ')
            if len(name) == 0:
                raise ValueError('Name cannot be empty')
            surname = input('Surname: ')
            if len(surname) == 0:
                raise ValueError('Surname cannot be empty')
            membership = int(input('Membership: '))
            if membership is None:
                raise ValueError('Membership cannot be empty')
            customer = Customer(name=name, surname=surname, membership=membership)
            CustomerDao.add_customer(customer)
        except ValueError as e:
            print(f'Invalid value: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')

    def update_customer(self):
        try:
            print('Update customer info')
            name = input('Name: ')
            if len(name) == 0:
                raise ValueError('Name cannot be empty')
            surname = input('Surname: ')
            if len(surname) == 0:
                raise ValueError('Surname cannot be empty')
            membership = int(input('Membership: '))
            if membership is None:
                raise ValueError('Membership cannot be empty')
            id = int(input('Id: '))
            if id is None:
                raise ValueError('Id cannot be empty')
            customer = Customer(id = id, name=name, surname=surname, membership=membership)
            CustomerDao.update_customer(customer)
        except ValueError as e:
            print(f'Invalid value: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')

    def delete_customer(self):
        try:
            id = int(input('Id: '))
            if id is None:
                raise ValueError('Id cannot be empty')
            customer = Customer(id = id)
            CustomerDao.delete_customer(customer)
        except ValueError as e:
            print(f'Invalid value: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')

    def show_all_customers(self):
        for customer in CustomerDao.get_all_customers():
            print(customer)

if __name__ == '__main__':
    fit_zone = FitZone()
    fit_zone.fit_zone()
