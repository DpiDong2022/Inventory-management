#from inventoryObjectData import PRODUCT, ITEM

class inventory_manager:
    def __init__(self, PRODUCT, ITEM) -> None:
        self.PRODUCT = PRODUCT
        self.ITEM = ITEM

    def process_data_tableitemview(self,id):
        raw_data = self.ITEM.search(id)
        return [row for row in raw_data if row.date_update>row.date_delete]
    
    def proccess_delete_product(self,id):
        self.PRODUCT.delete(id)

    def proccess_delete_item(self,id):
        self.ITEM.delete(id)
    
    def process_add_data(self, all_data):

        new_product = self.PRODUCT('',all_data[0], all_data[1],all_data[2],all_data[3], all_data[4],all_data[5])
        id_new_product=new_product.id
        self.PRODUCT.add_product(new_product)

        for i in all_data[6]:
        #     new_item=ITEM('',id_new_product, i[0], i[1],i[2],i[3],i[4])
        #     self.ITEM.add_item(new_item)
            self.add_item([id_new_product,i[0], i[1],i[2],i[3],i[4]])
    
    def update_product(self, combodata):#id,name,typee,category,brand,material,description
        for data in combodata:
            self.PRODUCT.update(data[0],data[1],data[2],data[3].capitalize(),data[4],data[5],data[6])
        
    def update_item(self,combodata):
        for data in combodata:
             # if that is float at price and int at quantity, not letters
            try:
                self.ITEM.update(data[0],float(data[1]),int(data[2]),data[3].lower(),data[4].upper(),data[5])
            except:
                pass
        
        
    def process_search_product(self,key):
        data=self.PRODUCT.search(key)
        return [row for row in data if row.date_update>row.date_delete]
    
    def add_item(self,data):
        new_item=self.ITEM('', data[0], data[1],data[2],data[3],data[4],data[5])
        self.ITEM.add_item(new_item)
    
    def infor_char(self):
        data = self.PRODUCT.sodo_quantity()
        return data

    def checkname(self,name):
        products= self.PRODUCT.get_all_product()
        for product in products:
            if product.name ==name:
                return 0
        return 1 
    
    def two_infor_home(self):
        return self.PRODUCT.count_all_of_product(), self.PRODUCT.count_all_of_stock()