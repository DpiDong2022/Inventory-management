import sqlite3
import random
import datetime
from call_main_UI import resourse_path

def connectDB():
    con = sqlite3.connect(resourse_path('INVENTORY_DB.db'))
    return con, con.cursor()

def closeDB(connect):
    connect.commit()
    connect.close()

def take_all_id_product():
    con, cur = connectDB()
    cur.execute('SELECT ID FROM PRODUCTS WHERE DATE_UPDATE > DATE_DELETE')
    result = cur.fetchall()
    closeDB(con)
    return result

def take_all_id_item():
    con, cur = connectDB()
    cur.execute('SELECT ID FROM ITEMS WHERE DATE_UPDATE > DATE_DELETE')
    result = cur.fetchall()
    closeDB(con)
    return result



class PRODUCT:
    listID = take_all_id_product()
    def __init__(self, id,name, typee, category, brand, material, description,date_update=datetime.date.today(),date_delete=datetime.date(2000,1,1)):
        self.id = self.generate_random_ID() if id =='' else id
        self.name = name
        self.typee = typee
        self.category = category
        self.brand = brand
        self.material = material
        self.description = description
        self.date_update = date_update
        self.date_delete = date_delete

    def to_tuple(self):
        return (self.id, self.name, self.typee, self.category,self.brand, self.material, 
                self.description, self.date_update, self.date_delete)
    
    @classmethod
    def count_all_of_stock(cls):
        con,cur = connectDB()
        cur.execute("SELECT COUNT(*) FROM ITEMS WHERE DATE_UPDATE > DATE_DELETE AND QUANTITY=0")
        COUNT = cur.fetchone()[0]

        closeDB(con)
        return COUNT

    @classmethod 
    def count_all_of_product(cls):
        con,cur = connectDB()
        cur.execute("SELECT SUM(QUANTITY) FROM ITEMS WHERE DATE_UPDATE > DATE_DELETE")
        COUNT = cur.fetchone()[0]

        closeDB(con)
        return COUNT
    
    @staticmethod
    def sodo_quantity():
        con, cur = connectDB()
        result=[]
        cur.execute('''SELECT CATEGORY, SUM(ITEMS.QUANTITY) FROM PRODUCTS 
                        JOIN ITEMS WHERE PRODUCTS.ID = ITEMS.PRODUCT_ID 
						AND PRODUCTS.DATE_UPDATE > PRODUCTS.DATE_DELETE
						AND ITEMS.DATE_UPDATE > ITEMS.DATE_DELETE
                        GROUP BY(CATEGORY)''')
        result=cur.fetchall()
        closeDB(con)
        return result
    @staticmethod
    def generate_random_ID():
        while True:
            randomID = random.randint(0,1000000)
            if randomID not in PRODUCT.listID:
                return randomID
    
    @staticmethod
    def add_product(product):
        con, cur = connectDB()
        cur.execute('INSERT INTO PRODUCTS VALUES(?,?,?,?,?,?,?,?,?)',product.to_tuple())
        closeDB(con)

    @staticmethod
    def search(keyword):
        little_key=keyword.split(' ')
        little_key.append(keyword)

        con, cur = connectDB()
        result = set()

        for i in little_key:
            cur.execute('''SELECT * FROM PRODUCTS
                                    WHERE name LIKE ?
                                ''',('%'+i+'%',))
            result.update(cur.fetchall())

        closeDB(con)
        return [PRODUCT(product[0],product[1],product[2],product[3],product[4],product[5],
                        product[6],product[7],product[8]) for product in result]

    @staticmethod
    def delete(id):
        con, cur = connectDB()
        cur.execute('UPDATE PRODUCTS SET DATE_DELETE =? WHERE id = ?',(datetime.date.today(),id))
        closeDB(con)

    @staticmethod
    def update(id, name, typee, category, brand, material, description):
        con, cur = connectDB()
        cur.execute('UPDATE PRODUCTS SET NAME =?, TYPE=?, CATEGORY=?, BRAND=?, MATERIAL=?, DESCRIPTION=? WHERE ID = ?',
                    (name, typee, category, brand, material, description, id))
        closeDB(con)
    
    @staticmethod
    def get_all_product():
        con, cur = connectDB()
        cur.execute("select * from PRODUCTS")
        products = cur.fetchall()
        closeDB(con)
        return [PRODUCT(product[0],product[1],product[2],product[3],product[4],product[5],
                        product[6],product[7],product[8]) for product in products]
    @staticmethod
    def search_product(key):
        little_key=key.split(' ')
        little_key.append(key)

        con, cur = connectDB()
        result = set()

        for i in little_key:
            cur.execute('''SELECT NAME, TYPE, CATEGORY, BRAND, MATERIAL, DATE_DELETE, DATE_UPDATE, DESCRIPTION FROM PRODUCTS
                                    WHERE  (name LIKE ?)''',('%'+i+'%',))
            result.update(cur.fetchall())

        closeDB(con)
        return result

class ITEM():
    listID= take_all_id_item()
    def __init__(self, id, product_ID, price, quantity, color, size, image = '',date_update=datetime.date.today(),date_delete=datetime.date(2000,1,1)):
        self.id = self.generate_random_ID() if id=='' else id
        self.product_ID = product_ID
        self.price = price
        self.quantity = quantity
        self.color = color
        self.size = size
        self.image = image
        self.date_update = date_update
        self.date_delete = date_delete
    
    @staticmethod
    def generate_random_ID():
        while True:
            randomID = random.randint(0,1000000)
            if randomID not in ITEM.listID:
                return randomID
    
    def to_tuple(self):
        return (self.id, self.product_ID, self.price, self.quantity,self.color,self.size, self.image, 
                self.date_update, self.date_delete)
    
    @staticmethod
    def add_item(item):
        con, cur = connectDB()
        cur.execute('INSERT INTO ITEMS VALUES(?,?,?,?,?,?,?,?,?)',item.to_tuple())
        closeDB(con)
    
    @staticmethod
    def search(product_ID):
        con, cur = connectDB()

        cur.execute('''SELECT * FROM ITEMS
                                WHERE PRODUCT_ID=?
                            ''',(product_ID,))
        result = cur.fetchall()

        closeDB(con)
        return [ITEM(item[0],item[1],item[2],item[3],item[4],item[5],
                     item[6],item[7],item[8]) for item in result]

    @staticmethod
    def delete(id):
        con, cur = connectDB()
        cur.execute('UPDATE ITEMS SET DATE_DELETE =? WHERE id = ?',(datetime.date.today(),id))
        closeDB(con)

    @staticmethod
    def update(id, price, quantity, color, size, image):
        con, cur = connectDB()
        cur.execute('UPDATE ITEMS SET PRICE =?, QUANTITY=?, COLOR=?, SIZE=?, IMAGE=? WHERE ID = ?',
                    (price, quantity, color, size, image,id))
        closeDB(con)
    
    @staticmethod
    def get_all_item():
        con, cur = connectDB()
        cur.execute("select * from ITEMS")
        items = cur.fetchall()
        closeDB(con)
        return [ITEM(item[0],item[1],item[2],item[3],item[4],item[5],
                     item[6],item[7],item[8]) for item in items]
    
if __name__=="__main__":

    # while True:
    #     name = input("name:")
    #     typee = input("type:")
    #     category = input("category:")
    #     brand = input("brand:")
    #     material = input("material:")
    #     description = input("description:")

    #     product1 = PRODUCT('',name, typee, category, brand, material, description)
    #     product1.add_product(product1)

    #     print("add item")
    #     while True:
    #         product_ID = product1.id
    #         price=float(input("price:"))
    #         quantity=int(input("quantity:"))
    #         color=input("color:")
    #         size=input("size:")
    #         image=''

    #         item1 = ITEM('',product_ID, price,quantity, color, size, image)
    #         item1.add_item(item1)

    #         if input('add more item(yes/no):')!='yes':
    #             break
        
    #     if input('add more product(yes/no):')!='yes':
    #         break
    pass