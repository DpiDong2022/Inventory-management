from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as graph
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from main_ui import *
from newItem.ui_newItem_ui import *
from colorSIDE.choosecolor_ui import *
from inforSIDE.main_ui import *
import sys,os

def resourse_path(relative_path):
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)

class Main_UI(QMainWindow):
    def __init__(self, Inventory_manager):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #default
        self.inventory_manager = Inventory_manager
        self.col_sort_item='Quantity'
        self.col_sort_product='Type'
        self.setuptableProduct()

        #home
        self.ui.label_image.setPixmap(QPixmap(resourse_path("Icons\\background.jpg")).scaled(429,365))
        self.setup_sodo()
        self.ui.button_home.clicked.connect(lambda :self.setup_sodo())

        #search tab
        self.ui.button_previous_2.clicked.connect(lambda :self.ui.main_tab.setCurrentIndex(2))
        self.ui.main_tab.tabBar().setVisible(False)
        self.ui.button_search_tab.clicked.connect(lambda :self.ui.main_tab.setCurrentIndex(2))
        self.ui.button_search_2.clicked.connect(self.setuptableProduct)
        self.ui.tableWidget_item.horizontalHeader().sectionClicked.connect(self.sortTable)
        self.ui.tableWidget_product.horizontalHeader().sectionClicked.connect(self.sortTable)
        
        self.ui.button_add.clicked.connect(lambda :self.ui.main_tab.setCurrentIndex(1))

        self.ui.pushButton_new_item.clicked.connect(lambda: self.setup_slot_add_item())

        self.ui.button_save_product_edit.clicked.connect(self.save_edit_product)
        self.ui.pushButton_save_edit_item.clicked.connect(self.save_edit_item)

        self.cover_pixmap=QPixmap(resourse_path("Icons\\stick.png"))

        # product
        self.list_edit_product_row=[]
        self.list_edit_item_row=[]
        self.product_id = -1

        # item

        #add tab
        self.chooseColor = UI_selectColor(self)
        self.uiInputColor =UI_inputColor(self)
        self.inputINFO= UI_inputInformation(self)
        self.createMODELTABLEVIEW()

        self.ui.pushButton_ADDsize.clicked.connect(lambda:self.increase_size())
        self.ui.pushButton_MINUSsize.clicked.connect(lambda:self.decrease_size())
        self.ui.pushButtonADDColor.clicked.connect(self.increaseColor)
        self.ui.pushButton_MINUScolor.clicked.connect(lambda:self.decreaseColor())
        self.ui.pushButton_ADDColors.clicked.connect(lambda:self.chooseColor.show())

        self.ui.pushButtonClearData.clicked.connect(self.clearDataTable)
        self.ui.tableView.doubleClicked.connect(self.mouseDoubleClickEvent)
        self.ui.pushButtonOK.clicked.connect(self.save_product)

#---------------------------------------------------------------------------
    def sort_list_items(self,items):
        col=self.col_sort_item
        if col == 'Price':
            return sorted(items, key=lambda object: object.price)
        elif col == 'Quantity':
            return sorted(items, key=lambda object: object.quantity)
        elif col == 'Color':
            return sorted(items, key=lambda object: object.color)
        elif col == 'Size':
            return sorted(items, key=lambda object: object.size)
        else:
            return sorted(items, key=lambda object: object.quantity)
    
    def sort_list_products(self,products):
        col=self.col_sort_product
        if col=='Name':
            return sorted(products, key=lambda object: object.name)
        elif col=='Type':
            return sorted(products, key=lambda object: object.typee)
        elif col=='Category':
            return sorted(products, key=lambda object: object.category)
        elif col=='Brand':
            return sorted(products, key=lambda object: object.brand)
        elif col=='Description':
            return sorted(products, key=lambda object: object.description)
        elif col=='Material':
            return sorted(products, key=lambda object: object.material)
        else:
            pass

    def sortTable(self, col):
        name= self.sender().parent().objectName()
        if name == 'tableWidget_item':
            self.col_sort_item = self.ui.tableWidget_item.horizontalHeaderItem(col).text()
            self.setupTableItem(self.product_id,True)
        else:
            self.col_sort_product = self.ui.tableWidget_product.horizontalHeaderItem(col).text()
            
            self.setuptableProduct()

    def setup_sodo(self):
        count_all_of_product,count_all_of_stock=self.inventory_manager.two_infor_home()
        self.ui.label_count_products.setText(str(count_all_of_product))
        self.ui.label_count_out_stock.setText(str(count_all_of_stock))
        
        self.ui.main_tab.setCurrentIndex(0)
        infor = self.inventory_manager.infor_char()
        try:
            self.ui.layout_sodo.removeWidget(self.canvas) #remove the old bar chart before setting for new
        except:
            pass
        
        fig = graph.figure()
        self.canvas = FigureCanvas(fig)

        category = [el[0] for el in infor]
        quantity = [el[1] for el in infor]
        ax = fig.add_subplot(111)
        ax.bar(category, quantity)
        ax.set_xlabel('Accessories')
        ax.set_ylabel('Quantity')
        ax.set_title('Quantity over time')
        ax.tick_params(axis='x', labelsize=10)
        self.canvas.draw()

        self.ui.layout_sodo.addWidget(self.canvas)

    def save_edit_product(self):
        combodata=[]
        for (id,row) in self.list_edit_product_row:
            edit_product=[]
            name = self.ui.tableWidget_product.item(row,0).text()
            typee = self.ui.tableWidget_product.item(row,1).text()
            category = self.ui.tableWidget_product.item(row,2).text()
            brand = self.ui.tableWidget_product.item(row,3).text()
            material = self.ui.tableWidget_product.item(row,4).text()
            description = self.ui.tableWidget_product.item(row,5).text()
            edit_product.extend([id,name,typee,category,brand,material,description])
            combodata.append(edit_product)
        
        self.inventory_manager.update_product(combodata)
        self.setuptableProduct()
    
    def save_edit_item(self):
        message= QMessageBox(parent=self)
        message.setWindowTitle("Confirmation")
       
        combodata_item=[]
        for (id,row) in self.list_edit_item_row:
            quantity=self.ui.tableWidget_item.item(row,1).text()
            try:
                quan= int(quantity)
                edit_item = []
                price = self.ui.tableWidget_item.item(row,0).text()
                color =self.ui.tableWidget_item.item(row,2).text()
                size=self.ui.tableWidget_item.item(row,3).text()
                label = self.ui.tableWidget_item.cellWidget(row,4).layout().itemAt(0).widget()
                pixmap = label.pixmap()
                byte_iamge=self.convertPixmapToBinaryArray(pixmap)
                edit_item.extend([id,price,quantity,color,size,byte_iamge])
                combodata_item.append(edit_item)
            except:
                message.setText(f"Can not update row {row} due to quantity can't be a float number({quantity})")
                message.exec_()
        
        self.inventory_manager.update_item(combodata_item)
        self.setupTableItem(self.product_id,True)

    def get_vertical_labels(self):
        vertical_header = self.ui.tableView.verticalHeader()
        # Get the model associated with the vertical header
        model = vertical_header.model()
        # Get the vertical header labels as a list
        vertical_labels = [model.headerData(i, QtCore.Qt.Vertical) for i in range(model.rowCount())]
        return vertical_labels
    
    def get_horizontal_labels(self):
        horizontal_header = self.ui.tableView.verticalHeader()
        # Get the model associated with the vertical header
        model = horizontal_header.model()
        # Get the vertical header labels as a list
        horizontal_labels = [model.headerData(i, QtCore.Qt.Horizontal) for i in range(model.columnCount())]
        return horizontal_labels

#---------------------------------------------------------------------------add tab
    def save_product(self):
        vertical_labels = self.get_vertical_labels()
        horizontal_labels = self.get_horizontal_labels()
        check_non_value=self.check_none_info_input()

        if check_non_value==1:
            allItems = []
            for row in range(self.table_model.rowCount()):
                for col in range(self.table_model.columnCount()):
                    itemdata= []
                    item = self.table_model.item(row,col)
                    if item is not None and item.text()!='':
                        text = item.text().split()
                        price,quantity = text[1],text[3]
                        color = vertical_labels[row]
                        size = horizontal_labels[col]
                        pixmap = item.icon().pixmap(QSize(200,200))
                        byte_image=self.convertPixmapToBinaryArray(pixmap)

                        itemdata.extend([price,quantity,color, size,byte_image])
                        allItems.append(itemdata)
            #alldata[name, brand, category, description, material, type, allItem[]]
            alldata=[]
            alldata.append(self.ui.lineEditName.text())
            alldata.append(self.ui.lineEdit_type.text())
            alldata.append(self.ui.comboBox_category.currentText())
            alldata.append(self.ui.lineEdit_Brand.text())
            alldata.append(self.ui.lineEdit_Material.text())
            alldata.append(self.ui.lineEdit_Description.text())
            alldata.append(allItems)

            if alldata[6] !=[]:
                message= QMessageBox(parent=self)
                self.inventory_manager.process_add_data(alldata)
                message.setWindowTitle("Confirmation")
                message.setText('Saved')
                message.exec_()
            else:
                message= QMessageBox(parent=self)
                message.setWindowTitle("Confirmation")
                message.setText('Your data have not saved \nYou must enter one or more than one item before save product')
                message.exec_()
    
    def check_name_exist(self,name):
        check = self.inventory_manager.checkname(name)
        return check

    def check_none_info_input(self):
        check=1
        valid_style='''border-radius: 3px;
                        border-style: solid;
                                border-width: 1px;
                                border-color: rgb(0, 0, 0);'''
        invalid_style='''border-radius: 3px;
                        border-style: solid;
                                border-width: 1px;
                                border-color: rgb(255,0,0);'''
        if self.ui.lineEditName.text()=='' or len(self.ui.lineEditName.text())<10:
            self.ui.lineEditName.setStyleSheet(invalid_style)
            check=0
        else:
            self.ui.lineEditName.setStyleSheet(valid_style)
            if self.check_name_exist(self.ui.lineEditName.text())==0:
                check=0
                self.ui.lineEditName.setStyleSheet(invalid_style)
                message = QMessageBox(parent=self,text='The name product have been existed in system')
                message.setWindowTitle("Confirmation")
                message.exec_()
            else:
                self.ui.lineEditName.setStyleSheet(valid_style)

        if self.ui.lineEdit_type.text()=='':
            self.ui.lineEdit_type.setStyleSheet(invalid_style)
            check=0
        else:
            self.ui.lineEdit_type.setStyleSheet(valid_style)

        if self.ui.lineEdit_Description.text()=='':
            check=0
            self.ui.lineEdit_Description.setStyleSheet(invalid_style)
        else:
            self.ui.lineEdit_Description.setStyleSheet(valid_style)

        if self.ui.lineEdit_Material.text()=='':
            check=0
            self.ui.lineEdit_Material.setStyleSheet(invalid_style)
        else:
            self.ui.lineEdit_Material.setStyleSheet(valid_style)

        if self.ui.lineEdit_Brand.text()=='':
            check=0
            self.ui.lineEdit_Brand.setStyleSheet(invalid_style)
        else:
            self.ui.lineEdit_Brand.setStyleSheet(valid_style)
            
        if self.ui.comboBox_category.currentText()=='---select accessory---':
            check=0
            self.ui.comboBox_category.setStyleSheet(invalid_style)
        else:
            self.ui.comboBox_category.setStyleSheet(valid_style)
        
        return check
    
    def mouseDoubleClickEvent(self, event):
        if isinstance(event, QtCore.QModelIndex): # if not check that, when we click out site the table view, erroe!!!
            #take index
            row = event.row()
            column = event.column()
            #show dialog
            price, quantity, pixmap = self.inputINFO.getInfor()

            item = QtGui.QStandardItem(f"price: {price} quantity: {quantity}")
            item.setIcon(QtGui.QIcon(pixmap))

            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable) # make item only be read
            self.table_model.setItem(row, column, item)

    def clearDataTable(self):
            num_rows = self.table_model.rowCount()
            num_cols = self.table_model.columnCount()

            for row in range(num_rows):
                for col in range(num_cols):
                    self.table_model.clearItemData(self.table_model.index(row,col))
            
            self.ui.lineEditName.setText('')
            self.ui.lineEdit_Brand.setText('')
            self.ui.lineEdit_type.setText('')
            self.ui.lineEdit_Description.setText('')
            self.ui.lineEdit_Material.setText('')
            self.ui.comboBox_category.setCurrentIndex(0)

    def arrange_space_column(self):
        # lam cho size dung voi do dai, tu can chinh
            header = self.ui.tableView.horizontalHeader()
            for i in range(header.count()):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)    

    def increase_size(self):
        list_of_size = ['UNISIZE','S','M','L','XL','XXL']
        len_of_H_labels=len(self.get_horizontal_labels()) # coloumn
        if len_of_H_labels<6:
            self.table_model.setHorizontalHeaderItem(len_of_H_labels,QStandardItem(list_of_size[len_of_H_labels]))
            self.arrange_space_column()

    def decrease_size(self):
        self.table_model.removeColumn(self.table_model.columnCount()-1)
        self.arrange_space_column()

    def createMODELTABLEVIEW(self):
        self.table_model = QtGui.QStandardItemModel()
        self.ui.tableView.setModel(self.table_model)
    
    def increaseColor(self):
        new_color=self.uiInputColor.getColor().lower()
        if new_color not in self.get_vertical_labels():
            self.chooseColor.inORdecreaseIcon(new_color,True) ######
            self.table_model.setVerticalHeaderItem(self.table_model.rowCount(),QStandardItem(new_color))
        self.uiInputColor.input_color.setText('')

    def decreaseColor(self):
        if self.table_model.rowCount() >0:
            self.chooseColor.inORdecreaseIcon(self.get_vertical_labels()[-1],False)
            self.table_model.removeRow(self.table_model.rowCount()-1)###########
            
#--------------------------------------------------------------------------- search tab
    def setup_slot_add_item(self):
        ui_add_item = UI_input_new_item(self)
        ui_add_item.show()

        try:
            color, size, price, quantity, pixmap = ui_add_item.getInfor()
            byte_image = self.convertPixmapToBinaryArray(pixmap)
            if color !='':
                self.inventory_manager.add_item([self.product_id,price,quantity,color,size,byte_image])
                self.setupTableItem(self.product_id,True)
            else:
                message= QMessageBox(parent=self)
                message.setWindowTitle("Confirmation")
                message.setText('Can not save new item due to non-color')
                message.exec_()
        except:
            pass

    def setuptableProduct(self):
        self.ui.main_tab.setCurrentIndex(2)
        self.buttonStyle="""
                                            QPushButton{
                                                border-style: solid;
                                                    border-width: 1px;
                                                    border-color: rgb(0, 0, 0);
                                            background-color: rgb(255, 170, 0);
                                                    border-radius:4px
                                            }
                                            QPushButton:hover:!pressed
                                            {
                                                background-color: rgb(170, 170, 255);
                                            }

                                            QPushButton:pressed
                                            {
                                                background-color: rgb(255, 255, 255);
                                            }
                                            """
        self.list_edit_product_row=[]
        data=self.inventory_manager.process_search_product(self.ui.lineEdit_keysearch.text())
        #data after sort
        data = self.sort_list_products(products=data)
        
        self.ui.tableWidget_product.setRowCount(len(data))
        for row,product in enumerate(data):
                #display data
                self.ui.tableWidget_product.setItem(row, 0, QTableWidgetItem(product.name))
                self.ui.tableWidget_product.setItem(row, 1, QTableWidgetItem(product.typee))
                self.ui.tableWidget_product.setItem(row, 2, QTableWidgetItem(product.category))
                self.ui.tableWidget_product.setItem(row, 3, QTableWidgetItem(product.brand))
                self.ui.tableWidget_product.setItem(row, 4, QTableWidgetItem(product.material))
                self.ui.tableWidget_product.setItem(row, 5, QTableWidgetItem(product.description))
            
                # display 3 button
                widget = QWidget()
                horizontalLayout=QHBoxLayout()

                edit_button = QPushButton("Edit")
                edit_button.setFixedSize(QSize(28,35))
                edit_button.setStyleSheet(self.buttonStyle)
                edit_button.clicked.connect(lambda _,id=product.id,button=edit_button, roww= row: self.make_editable(id,button,roww,"product"))

                editItem_button = QPushButton("Edit item")
                edit_button.setToolTip(str(product.id))
                editItem_button.clicked.connect(lambda _,id =product.id: self.setupTableItem(id))
                editItem_button.setFixedSize(QSize(55,35))
                editItem_button.setStyleSheet(self.buttonStyle)
                

                delete_button = QPushButton("Delete")
                delete_button.clicked.connect(lambda _,id=product.id: self.delete_product(id))
                delete_button.setFixedSize(QSize(44,35))
                delete_button.setStyleSheet(self.buttonStyle)

                horizontalLayout.addWidget(edit_button)
                horizontalLayout.addWidget(editItem_button)
                horizontalLayout.addWidget(delete_button)

                widget.setLayout(horizontalLayout)
                self.ui.tableWidget_product.setCellWidget(row,6,widget)
    
    def delete_product(self,product_id):
        reply = QMessageBox.question(self,'Confirmation', "Are you sure you want to delete this?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.inventory_manager.proccess_delete_product(product_id)
        self.setuptableProduct()

    def delete_item(self,item_id,product_id):
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete this?', QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:                    
            self.inventory_manager.proccess_delete_item(item_id)
        self.setupTableItem(product_id,True)

    def make_editable(self,id, button, row, mode):
        if button.property("stick_edit"):
            # If the button is already covered, remove the cover and update the property
            button.setIcon(QtGui.QIcon())
            button.setFixedSize(QSize(28,35))
            button.setProperty("stick_edit", False)
            button.style().unpolish(button)
            button.style().polish(button)

        else:
            # If the button is not covered, add the cover and update the property
            button.setIcon(QtGui.QIcon(self.cover_pixmap))
            button.setFixedSize(QSize(48,35))
            button.setProperty("stick_edit", True)
            button.style().unpolish(button)
            button.style().polish(button)

        self.tick_to_update(id,row,mode)

    def tick_to_update(self,id, row,mode):
        if mode=='product':
            if (id,row) not in self.list_edit_product_row:
                self.list_edit_product_row.append((id,row))
            else:
                self.list_edit_product_row.remove((id,row))
        
        else:
            if (id,row) not in self.list_edit_item_row:
                self.list_edit_item_row.append((id,row))
            else:
                self.list_edit_item_row.remove((id,row))

    def setupTableItem(self,product_id,save_delete=False):
        self.ui.main_tab.setCurrentIndex(3)
        if save_delete == False:
            if self.product_id==product_id:
                return
            
        self.list_edit_item_row=[]
        self.product_id = product_id
        #self.clear_table_item()
        items = self.inventory_manager.process_data_tableitemview(product_id)
        #sort list
        items = self.sort_list_items(items)
        
        self.ui.tableWidget_item.setRowCount(len(items))

        for row,item in enumerate(items):
                self.ui.tableWidget_item.setItem(row, 0, QTableWidgetItem(str(item.price)))
                self.ui.tableWidget_item.setItem(row, 1, QTableWidgetItem(str(item.quantity)))
                self.ui.tableWidget_item.setItem(row, 2, QTableWidgetItem(item.color))
                self.ui.tableWidget_item.setItem(row, 3, QTableWidgetItem(item.size))
                widget_image = QWidget()
                layout = QVBoxLayout()
                pixmap = self.convertByteImageToPixmap(item.image)
                labelpixmap = QLabel()
                labelpixmap.setPixmap(pixmap)

                layout.addWidget(labelpixmap)
                widget_image.setLayout(layout)
                self.ui.tableWidget_item.setCellWidget(row, 4, widget_image)

                widget = QWidget()
                horizontalLayout=QHBoxLayout()

                edit_button = QPushButton("Edit")
                edit_button.clicked.connect(lambda _,id=item.id,button=edit_button,roww=row: self.make_editable_for_item(id,button,roww,"item"))
                edit_button.setFixedSize(QSize(35,35))
                edit_button.setStyleSheet(self.buttonStyle)

                delete_button = QPushButton("Delete")
                delete_button.clicked.connect(lambda _,id=item.id,id_pro=product_id: self.delete_item(id,id_pro))
                delete_button.setFixedSize(QSize(55,35))
                delete_button.setStyleSheet(self.buttonStyle)

                horizontalLayout.addWidget(edit_button)
                horizontalLayout.addWidget(delete_button)

                widget.setLayout(horizontalLayout)
                self.ui.tableWidget_item.setCellWidget(row,5,widget)
    
    def make_editable_for_item(self,id,button,row,mode):
        if button.property("stick_edit"):
            # If the button is already covered, remove the cover and update the property
            button.setIcon(QtGui.QIcon())
            button.setFixedSize(QSize(28,35))
            button.setProperty("stick_edit", False)
            
            #take widget
            button_select_image = self.ui.tableWidget_item.cellWidget(row,4).layout().itemAt(1).widget()
            #take layout that contains widget we want to delete
            layoutt = self.ui.tableWidget_item.cellWidget(row,4).layout()
            #delete that widget
            layoutt.removeWidget(button_select_image)

        else:
            # If the button is not covered, add the cover and update the property
            button.setIcon(QtGui.QIcon(self.cover_pixmap))
            button.setFixedSize(QSize(48,35))
            button.setProperty("stick_edit", True)
            button_select_image= QPushButton(text='select image')
            button_select_image.setStyleSheet(self.buttonStyle)
            button_select_image.setMinimumHeight(30)
            #take layout that contain a label-pixmap
            layout = self.ui.tableWidget_item.cellWidget(row,4).layout()
            #add button2
            layout.addWidget(button_select_image)
            button_select_image.clicked.connect(lambda : self.chooseImage(row))

        self.tick_to_update(id,row,mode)
    
    def chooseImage(self,row):
        layout = self.ui.tableWidget_item.cellWidget(row,4).layout()
        file_path,_= QFileDialog.getOpenFileName(caption='select image', filter='Image Files (*.png *.jpg)')
        if file_path:
            new_pixmap = QPixmap(file_path).scaled(180,110)
            old_label_pixmap = layout.itemAt(0).widget()
            new_label_pixmap = QLabel()
            new_label_pixmap.setPixmap(new_pixmap)
            layout.replaceWidget(old_label_pixmap,new_label_pixmap)
           
    @staticmethod
    def convertPixmapToBinaryArray(pixmap):
        # convert the QPixmap to a QImage
        image = pixmap.toImage()

        # create a QBuffer object to store the bytes
        buffer = QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)

        # save the QImage to the buffer as PNG
        image.save(buffer, "PNG")

        # get the bytes from the buffer and convert to bytes object
        image_bytes = bytes(buffer.data())

        # close the buffer
        buffer.close()

        return image_bytes

    @staticmethod                
    def convertByteImageToPixmap(byte_array):# Create a QPixmap object from the QByteArray
        q_pixmap = QtGui.QPixmap()
        q_pixmap.loadFromData(byte_array)
        return q_pixmap

class UI_input_new_item(QDialog):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.pixmap=  QtGui.QPixmap(resourse_path('Icons\\white.png'))
        self.pixmap = self.pixmap.scaled(20, 20, aspectRatioMode = QtCore.Qt.KeepAspectRatio)

        self.ui.pushButton_selectImage.clicked.connect(self.chooseImage)
    
    def getInfor(self):
        if self.exec_() == QtWidgets.QDialog.Accepted:
            return self.ui.lineEdit_color.text(),self.ui.comboBox_size.currentText(),self.ui.doubleSpinBox_price.value(),self.ui.spinBox_quantity.value(),self.pixmap
    
    def chooseImage(self):
        image_file, _= QFileDialog.getOpenFileName(caption='select image', directory='',filter= 'Image Files (*.png *.jpg)')
        self.pixmap = QtGui.QPixmap(image_file).scaled(180,180)
    
class UI_inputColor(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        self.setWindowTitle("Color")
        self.resize(151,149)
        self.setModal(True)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        # Create input fields
        self.input_color = QtWidgets.QLineEdit()
        self.input_color.setFocus()
        
        # Create button
        self.button = QtWidgets.QPushButton("OK")
        self.button.setEnabled(False)
        self.button.clicked.connect(self.accept)

        self.input_color.textChanged.connect(self.setbutton)
        
        # Add input fields and button to layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.input_color)
        layout.addWidget(self.button)
        
        # Set dialog layout
        self.setLayout(layout)
    
    def setbutton(self, text):
        if text !="":
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)
    
    def getColor(self):
        # Return input value when button is clicked
        if self.exec_() == QtWidgets.QDialog.Accepted:
            return self.input_color.text()
    
    # def closeEvent(self, event):
    #     event.ignore()

class UI_selectColor(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        self.ui = Ui_Dialog_chooseColor()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.ui.pushButton_black.clicked.connect(self.configurationIcon)
        self.ui.pushButton_red.clicked.connect(self.configurationIcon)
        self.ui.pushButton_blue.clicked.connect(self.configurationIcon)
        self.ui.pushButton_white.clicked.connect(self.configurationIcon)
        self.ui.pushButton_gray.clicked.connect(self.configurationIcon)
        self.ui.pushButton_orange.clicked.connect(self.configurationIcon)
        self.ui.pushButton_brown.clicked.connect(self.configurationIcon)
        self.ui.pushButton_pink.clicked.connect(self.configurationIcon)
        self.ui.pushButton_yellow.clicked.connect(self.configurationIcon)
        self.ui.pushButton_silver.clicked.connect(self.configurationIcon)
        self.ui.pushButton_cyan.clicked.connect(self.configurationIcon)
        self.ui.pushButton_magenta.clicked.connect(self.configurationIcon)
        self.ui.pushButton_olive.clicked.connect(self.configurationIcon)
        self.ui.pushButton_maroon.clicked.connect(self.configurationIcon)
        self.ui.pushButton_navy.clicked.connect(self.configurationIcon)
        self.ui.pushButton_purple.clicked.connect(self.configurationIcon)
        self.ui.pushButton_teal.clicked.connect(self.configurationIcon)
        self.ui.pushButton_gold.clicked.connect(self.configurationIcon)
        self.ui.pushButton_bronze.clicked.connect(self.configurationIcon)
        self.ui.pushButton_green.clicked.connect(self.configurationIcon)
        
        self.ui.pushButton.clicked.connect(self.accept)
    
    def configurationIcon(self):
        vertical_labels=mywindow.get_vertical_labels()
        buttonicon = self.sender()

        if buttonicon.iconSize()==QtCore.QSize(2,2):
            buttonicon.setIconSize(QtCore.QSize(16,16))
            if buttonicon.text() not in vertical_labels:
                mywindow.table_model.setVerticalHeaderItem(mywindow.table_model.rowCount(),QStandardItem(buttonicon.text()))
        else:
            buttonicon.setIconSize(QtCore.QSize(2,2))
            index_row_to_delete = vertical_labels.index(buttonicon.text())
            mywindow.table_model.removeRow(index_row_to_delete)
    
    def inORdecreaseIcon(self, color:str, mode:bool):
        object = self.findChild(QPushButton,'pushButton_'+color)
        if object:
            if mode==True:
                object.setIconSize(QtCore.QSize(16,16))
            else: object.setIconSize(QtCore.QSize(2,2)) 

class UI_inputInformation(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        self.ui= Ui_Dialog_inputInforItem()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.pixmap= None
        
        self.ui.buttoSelectIamge.clicked.connect(self.chooseImage)
        self.ui.buttonOK.clicked.connect(self.accept)

    def chooseImage(self):
        image_file, _= QFileDialog.getOpenFileName(caption='select image', directory='',filter= 'Image Files (*.png *.jpg)')
        if image_file:
            self.pixmap = QtGui.QPixmap(image_file)
            self.pixmap.scaled(20, 20, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
            self.ui.buttonOK.setEnabled(True)
        else:
            self.chooseImage()

    def getInfor(self):
        if self.exec_() == QtWidgets.QDialog.Accepted:
            return self.ui.boxPrice.value(), self.ui.boxQuantity.value(), self.pixmap

if __name__ =="__main__":
    from inventory_management import inventory_manager
    from inventoryObjectData import PRODUCT, ITEM
    app = QApplication([])
    mywindow = Main_UI(inventory_manager(PRODUCT,ITEM))
    mywindow.show()
    app.exec_()