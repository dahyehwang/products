from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
        self.db = self._app.db
   
    def index(self):
        data = self.models['Product'].all_products()
        return self.load_view('index.html', data=data)

    def new(self):
        return self.load_view('new.html')

    def show(self, id):
        data = self.models['Product'].all_products_by_id(id)
        return self.load_view('show.html', data=data)

    def edit(self, id):
        data = self.models['Product'].all_products_by_id(id)
        return self.load_view('edit.html', data=data, id=id)

    def add_submit(self):
        item = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price']
        }
        data = self.models['Product'].add_product(item)
        flash("New product is added")
        return self.load_view('new.html', data=data)

    def edit_submit(self, id):
        item = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price']
        }
        self.models['Product'].update_product(item, id)
        flash("Product information is updated")
        return redirect('/products/edit/'+str(id))

    def delete_submit(self, id):
        item = request.form['delete']
        self.models['Product'].delete_product(item, id)
        return redirect('/')






