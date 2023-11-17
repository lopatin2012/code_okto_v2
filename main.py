# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        font = QtGui.QFont()
        font.setKerning(True)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.workshop_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.workshop_frame.setGeometry(QtCore.QRect(680, 20, 301, 361))
        self.workshop_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.workshop_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.workshop_frame.setObjectName("workshop_frame")
        self.workshop_button_1 = QtWidgets.QPushButton(parent=self.workshop_frame)
        self.workshop_button_1.setGeometry(QtCore.QRect(10, 60, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.workshop_button_1.setFont(font)
        self.workshop_button_1.setObjectName("workshop_button_1")
        self.workshop = QtWidgets.QLabel(parent=self.workshop_frame)
        self.workshop.setGeometry(QtCore.QRect(10, 10, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.workshop.setFont(font)
        self.workshop.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.workshop.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.workshop.setObjectName("workshop")
        self.workshop_button_2 = QtWidgets.QPushButton(parent=self.workshop_frame)
        self.workshop_button_2.setGeometry(QtCore.QRect(10, 100, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.workshop_button_2.setFont(font)
        self.workshop_button_2.setObjectName("workshop_button_2")
        self.workshop_button_3 = QtWidgets.QPushButton(parent=self.workshop_frame)
        self.workshop_button_3.setGeometry(QtCore.QRect(10, 140, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.workshop_button_3.setFont(font)
        self.workshop_button_3.setObjectName("workshop_button_3")
        self.workshop_button_4 = QtWidgets.QPushButton(parent=self.workshop_frame)
        self.workshop_button_4.setGeometry(QtCore.QRect(10, 180, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.workshop_button_4.setFont(font)
        self.workshop_button_4.setObjectName("workshop_button_4")
        self.progressBar = QtWidgets.QProgressBar(parent=self.workshop_frame)
        self.progressBar.setGeometry(QtCore.QRect(10, 270, 281, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(parent=self.workshop_frame)
        self.label.setGeometry(QtCore.QRect(10, 225, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.workshop_end_stoping_order = QtWidgets.QPushButton(parent=self.workshop_frame)
        self.workshop_end_stoping_order.setGeometry(QtCore.QRect(10, 310, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.workshop_end_stoping_order.setFont(font)
        self.workshop_end_stoping_order.setObjectName("workshop_end_stoping_order")
        self.settings_frame = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.settings_frame.setGeometry(QtCore.QRect(10, 10, 671, 561))
        self.settings_frame.setObjectName("settings_frame")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.table_workshop_codes = QtWidgets.QTableWidget(parent=self.tab)
        self.table_workshop_codes.setGeometry(QtCore.QRect(0, 60, 661, 411))
        self.table_workshop_codes.setRowCount(0)
        self.table_workshop_codes.setColumnCount(4)
        self.table_workshop_codes.setObjectName("table_workshop_codes")
        item = QtWidgets.QTableWidgetItem()
        self.table_workshop_codes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_workshop_codes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_workshop_codes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_workshop_codes.setHorizontalHeaderItem(3, item)
        self.table_codes_in_file = QtWidgets.QLabel(parent=self.tab)
        self.table_codes_in_file.setGeometry(QtCore.QRect(10, 0, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.table_codes_in_file.setFont(font)
        self.table_codes_in_file.setObjectName("table_codes_in_file")
        self.table_workshop_drop_down_list = QtWidgets.QComboBox(parent=self.tab)
        self.table_workshop_drop_down_list.setGeometry(QtCore.QRect(150, 10, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.table_workshop_drop_down_list.setFont(font)
        self.table_workshop_drop_down_list.setObjectName("table_workshop_drop_down_list")
        self.table_workshop_load_from_file = QtWidgets.QPushButton(parent=self.tab)
        self.table_workshop_load_from_file.setGeometry(QtCore.QRect(500, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.table_workshop_load_from_file.setFont(font)
        self.table_workshop_load_from_file.setObjectName("table_workshop_load_from_file")
        self.table_button_save_changes_in_file = QtWidgets.QPushButton(parent=self.tab)
        self.table_button_save_changes_in_file.setGeometry(QtCore.QRect(220, 480, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.table_button_save_changes_in_file.setFont(font)
        self.table_button_save_changes_in_file.setObjectName("table_button_save_changes_in_file")
        self.settings_frame.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.table_2_settings_push_button_save_settings = QtWidgets.QPushButton(parent=self.tab_2)
        self.table_2_settings_push_button_save_settings.setGeometry(QtCore.QRect(240, 480, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.table_2_settings_push_button_save_settings.setFont(font)
        self.table_2_settings_push_button_save_settings.setObjectName("table_2_settings_push_button_save_settings")
        self.table_2_settings_table_widget_every_days = QtWidgets.QTableWidget(parent=self.tab_2)
        self.table_2_settings_table_widget_every_days.setGeometry(QtCore.QRect(10, 100, 641, 261))
        self.table_2_settings_table_widget_every_days.setRowCount(0)
        self.table_2_settings_table_widget_every_days.setColumnCount(3)
        self.table_2_settings_table_widget_every_days.setObjectName("table_2_settings_table_widget_every_days")
        item = QtWidgets.QTableWidgetItem()
        self.table_2_settings_table_widget_every_days.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_2_settings_table_widget_every_days.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_2_settings_table_widget_every_days.setHorizontalHeaderItem(2, item)
        self.table_2_settings_label_for_table_every_days = QtWidgets.QLabel(parent=self.tab_2)
        self.table_2_settings_label_for_table_every_days.setGeometry(QtCore.QRect(190, 70, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.table_2_settings_label_for_table_every_days.setFont(font)
        self.table_2_settings_label_for_table_every_days.setObjectName("table_2_settings_label_for_table_every_days")
        self.table_2_settings_check_box_for_table_every_days = QtWidgets.QCheckBox(parent=self.tab_2)
        self.table_2_settings_check_box_for_table_every_days.setGeometry(QtCore.QRect(180, 30, 321, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.table_2_settings_check_box_for_table_every_days.setFont(font)
        self.table_2_settings_check_box_for_table_every_days.setObjectName("table_2_settings_check_box_for_table_every_days")
        self.settings_frame.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.json_products = QtGui.QAction(parent=MainWindow)
        self.json_products.setObjectName("json_products")
        self.auto_order = QtGui.QAction(parent=MainWindow)
        self.auto_order.setObjectName("auto_order")

        self.retranslateUi(MainWindow)
        self.settings_frame.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Заказ кодов"))
        self.workshop_button_1.setText(_translate("MainWindow", "Пустая кнопка"))
        self.workshop.setText(_translate("MainWindow", "Цеха"))
        self.workshop_button_2.setText(_translate("MainWindow", "Пустая кнопка"))
        self.workshop_button_3.setText(_translate("MainWindow", "Пустая кнопка"))
        self.workshop_button_4.setText(_translate("MainWindow", "Пустая кнопка"))
        self.label.setText(_translate("MainWindow", "Прогресс заказа кодов"))
        self.workshop_end_stoping_order.setText(_translate("MainWindow", "Остановить заказ"))
        item = self.table_workshop_codes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код продукта"))
        item = self.table_workshop_codes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Наименование"))
        item = self.table_workshop_codes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Статус"))
        item = self.table_workshop_codes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Количество"))
        self.table_codes_in_file.setText(_translate("MainWindow", "Выберите цех"))
        self.table_workshop_load_from_file.setText(_translate("MainWindow", "Отобразить"))
        self.table_button_save_changes_in_file.setText(_translate("MainWindow", "Сохранить"))
        self.settings_frame.setTabText(self.settings_frame.indexOf(self.tab), _translate("MainWindow", "Коды цеха"))
        self.table_2_settings_push_button_save_settings.setText(_translate("MainWindow", "Сохранить"))
        item = self.table_2_settings_table_widget_every_days.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Цех"))
        item = self.table_2_settings_table_widget_every_days.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "День недели"))
        item = self.table_2_settings_table_widget_every_days.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Заказ"))
        self.table_2_settings_label_for_table_every_days.setText(_translate("MainWindow", "Автоматический заказ кодов для цехов"))
        self.table_2_settings_check_box_for_table_every_days.setText(_translate("MainWindow", "Статус автоматического заказа кодов"))
        self.settings_frame.setTabText(self.settings_frame.indexOf(self.tab_2), _translate("MainWindow", "Настройки приложения"))
        self.json_products.setText(_translate("MainWindow", "Изменить заказ"))
        self.auto_order.setText(_translate("MainWindow", "Изменить авто-заказ"))


if __name__ == "__main__":
    import sys
    import order
    import json
    import threading
    import time
    from PyQt6.QtWidgets import QTableWidgetItem, QComboBox


    def re_translate_ui(MainWindow):
        _translate = QtCore.QCoreApplication.translate
        with open("lk.json", "r", encoding="UTF-8") as file_lk:
            name_workshop = list(json.load(file_lk))
        try:
            ui.workshop_button_1.setText(_translate("MainWindow", name_workshop[0]))
            ui.workshop_button_2.setText(_translate("MainWindow", name_workshop[1]))
            ui.workshop_button_3.setText(_translate("MainWindow", name_workshop[2]))
            ui.workshop_button_4.setText(_translate("MainWindow", name_workshop[3]))
        except Exception:
            pass


    def size_column_table_with_codes():
        # Изменение размеров колонок в таблице с кодами.
        # Код продукта.
        ui.table_workshop_codes.setColumnWidth(0, 80)
        # Наименование продукта.
        ui.table_workshop_codes.setColumnWidth(1, 400)
        # Статус заказа.
        ui.table_workshop_codes.setColumnWidth(2, 50)
        # Количество кодов в заказе.
        ui.table_workshop_codes.setColumnWidth(3, 75)

    def size_column_table_with_auto_order() -> None:
        """
        Изменение размеров колонок в таблице с автоматическим заказом кодов.
        :return:
        """
        # Цех.
        ui.table_2_settings_table_widget_every_days.setColumnWidth(0, 370)
        # День недели.
        ui.table_2_settings_table_widget_every_days.setColumnWidth(1, 150)
        # Статус.
        ui.table_2_settings_table_widget_every_days.setColumnWidth(2, 100)


    def update_from_json_in_table_with_workshop():
        """
        Обновление содержимого таблицы с цехами в таблице автоматического заказа кодов.
        :return:
        """
        data = order.load_settings()
        status_order_every_days = data["status_order_every_days"]
        ui.table_2_settings_check_box_for_table_every_days.setChecked(status_order_every_days)
        count_row = len(data["workshops"])
        ui.table_2_settings_table_widget_every_days.setRowCount(count_row)
        print(count_row)
        for workshop in data["workshops"]:
            print(data["workshops"][workshop])


    def update_from_json_in_table_with_codes(workshop: str):
        # Заполнение таблицы данными из json-файла по цеху.
        products = order.load_products()[workshop]
        count_row = len(products)
        if count_row >= 1:
            ui.table_workshop_codes.setRowCount(count_row)
            for index, row in enumerate(products, 0):
                combo_box = QComboBox()
                combo_box.addItem("True")
                combo_box.addItem("False")
                ui.table_workshop_codes.setItem(index, 0, QTableWidgetItem(row))
                ui.table_workshop_codes.setItem(index, 1, QTableWidgetItem(products[row]["name"]))
                ui.table_workshop_codes.setCellWidget(index, 2, combo_box)
                if products[row]["order"]:
                    ui.table_workshop_codes.setCellWidget(index, 2, combo_box)
                else:
                    combo_box.setCurrentText("False")
                    ui.table_workshop_codes.setCellWidget(index, 2, combo_box)
                # ui.table_workshop_codes.setItem(index, 2, QTableWidgetItem(str(products[row]["order"])))
                ui.table_workshop_codes.setItem(index, 3, QTableWidgetItem(str(products[row]["quantity"])))


    def update_combox_in_table_with_codes():
        # Обновление выпадающего списка в таблице с кодами.
        for workshop in order.load_workshops():
            ui.table_workshop_drop_down_list.addItem(workshop)

    def update_json_file_products():
        row = ui.table_workshop_codes.rowCount()
        workshop = ui.table_workshop_drop_down_list.currentText()
        data = order.load_products()
        for index in range(0, row):
            combo_box = ui.table_workshop_codes.cellWidget(index, 2)
            combo_box_text = combo_box.currentText()
            if combo_box_text == "False":
                data[workshop][ui.table_workshop_codes.item(index, 0).text()]["order"] = False
            else:
                data[workshop][ui.table_workshop_codes.item(index, 0).text()]["order"] = True
            data[workshop][ui.table_workshop_codes.item(index, 0).text()]["quantity"] = \
                ui.table_workshop_codes.item(index, 3).text()
        with open("products.json", "w", encoding="UTF-8") as file_products:
            json.dump(data, file_products, indent=4, ensure_ascii=False)


    def get_current_value_from_table_with_codes():
        # Получение название цеха из выпадающего списка в таблице с кодами.
        update_from_json_in_table_with_codes(ui.table_workshop_drop_down_list.currentText())


    def update_progress_bar():
        while order.status_order_threading:
            time.sleep(10)
            print(order.progress)
            ui.progressBar.setValue(order.progress)
            if order.progress == 100:
                ui.workshop_button_1.setEnabled(True)
                ui.workshop_button_2.setEnabled(True)
                ui.workshop_button_3.setEnabled(True)
                ui.workshop_button_4.setEnabled(True)


    def start_order_codes_by_clicking():
        name_workshop = MainWindow.sender().text()
        threading_progress = threading.Thread(target=lambda: update_progress_bar())
        threading_progress.start()
        if name_workshop != "Пустая кнопка":
            ui.workshop_button_1.setEnabled(False)
            ui.workshop_button_2.setEnabled(False)
            ui.workshop_button_3.setEnabled(False)
            ui.workshop_button_4.setEnabled(False)
            order.status_order_threading = True
            thread = threading.Thread(target=lambda: order.actions_on_the_site(name_workshop))
            thread.start()


    def stop_order_codes():
        order.status_order_threading = False
        ui.workshop_button_1.setEnabled(True)
        ui.workshop_button_2.setEnabled(True)
        ui.workshop_button_3.setEnabled(True)
        ui.workshop_button_4.setEnabled(True)

    # UI приложения.
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Переименовывание кнопок.
    re_translate_ui(MainWindow)
    # Изменение размеров колонок в таблице с кодами.
    size_column_table_with_codes()
    # Изменение размеров колонок в таблице с цехами.
    size_column_table_with_auto_order()
    # Обновление выпадающего списка с цехами.
    update_combox_in_table_with_codes()
    # Подключение сигналов для получения названия кнопок.
    ui.workshop_button_1.clicked.connect(start_order_codes_by_clicking)
    ui.workshop_button_2.clicked.connect(start_order_codes_by_clicking)
    ui.workshop_button_3.clicked.connect(start_order_codes_by_clicking)
    ui.workshop_button_4.clicked.connect(start_order_codes_by_clicking)
    # Подключение кнопки для получения названия цеха из выпадающего списка.
    ui.table_workshop_load_from_file.clicked.connect(get_current_value_from_table_with_codes)
    # Подключение кнопки для истановка заказа кодов.
    ui.workshop_end_stoping_order.clicked.connect(stop_order_codes)
    # Обновление данных в json-файлах.
    ui.table_button_save_changes_in_file.clicked.connect(update_json_file_products)
    # Установить прогресс бар на нулевое значение.
    ui.progressBar.setValue(0)
    update_from_json_in_table_with_workshop()

    MainWindow.show()
    sys.exit(app.exec())