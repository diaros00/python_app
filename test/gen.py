import ui_my_viewlogs
import os
from PyQt4 import QtCore, QtGui


class my_viewlogs(QtGui.QDialog, ui_my_viewlogs.Ui_viewlogs):
    def __init__(self):
        super(my_viewlogs, self).__init__()
        self.setupUi(self)
        self.model = QtGui.QStandardItemModel()
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.header_names = ['abc', 'def', 'ghi', 'kjl', 'mno', 'pqr']
        self.model.setHorizontalHeaderLabels(self.header_names)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setShowGrid(False)
        self.selectionModel = self.tableView.selectionModel()
        self.tableView.customContextMenuRequested.connect(self.open_menu)
        self.tableView.setModel(self.model)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

    def open_menu(self, position):
        menu = QtGui.QMenu()
        remove_selected_item_icon = QtGui.QIcon()
        remove_selected_item_icon.addPixmap(QtGui.QPixmap(
            ":/images      /Images/deleteSelected.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        remove_selected_item = menu.addAction(
            remove_selected_item_icon, "Remove selected item(s) ")
        if action == remove_selected_item:
            model = self.model
            indices = self.tableView.selectionModel().selectedRows()
            for index in sorted(indices):
                model.removeRow(index.row(), QtCore.QModelIndex())
