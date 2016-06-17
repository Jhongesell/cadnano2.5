# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs/preferences.ui'
#
# Created: Fri Jun 17 12:08:54 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(465, 374)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Preferences.sizePolicy().hasHeightForWidth())
        Preferences.setSizePolicy(sizePolicy)
        self.vertical_layout = QtWidgets.QVBoxLayout(Preferences)
        self.vertical_layout.setObjectName("vertical_layout")
        self.tab_widget = QtWidgets.QTabWidget(Preferences)
        self.tab_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_widget.setObjectName("tab_widget")
        self.interface_tab = QtWidgets.QWidget()
        self.interface_tab.setObjectName("interface_tab")
        self.vertical_layout_4 = QtWidgets.QVBoxLayout(self.interface_tab)
        self.vertical_layout_4.setObjectName("vertical_layout_4")
        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.form_layout.setObjectName("form_layout")
        self.zoom_speed_label = QtWidgets.QLabel(self.interface_tab)
        self.zoom_speed_label.setObjectName("zoom_speed_label")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.zoom_speed_label)
        self.zoom_speed_slider = QtWidgets.QSlider(self.interface_tab)
        self.zoom_speed_slider.setMinimumSize(QtCore.QSize(140, 0))
        self.zoom_speed_slider.setMinimum(1)
        self.zoom_speed_slider.setMaximum(100)
        self.zoom_speed_slider.setSingleStep(1)
        self.zoom_speed_slider.setProperty("value", 50)
        self.zoom_speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.zoom_speed_slider.setInvertedControls(False)
        self.zoom_speed_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.zoom_speed_slider.setTickInterval(0)
        self.zoom_speed_slider.setObjectName("zoom_speed_slider")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.zoom_speed_slider)
        self.Grid = QtWidgets.QLabel(self.interface_tab)
        self.Grid.setObjectName("Grid")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Grid)
        self.grid_appearance_type_combo_box = QtWidgets.QComboBox(self.interface_tab)
        self.grid_appearance_type_combo_box.setObjectName("grid_appearance_type_combo_box")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/part/grid_circles"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.grid_appearance_type_combo_box.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/part/grid_lines"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.grid_appearance_type_combo_box.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/part/grid_points"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.grid_appearance_type_combo_box.addItem(icon2, "")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.grid_appearance_type_combo_box)
        self.show_icon_label_text = QtWidgets.QLabel(self.interface_tab)
        self.show_icon_label_text.setObjectName("show_icon_label_text")
        self.form_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.show_icon_label_text)
        self.show_icon_labels = QtWidgets.QCheckBox(self.interface_tab)
        self.show_icon_labels.setChecked(True)
        self.show_icon_labels.setObjectName("show_icon_labels")
        self.form_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.show_icon_labels)
        self.vertical_layout_4.addLayout(self.form_layout)
        self.button_box = QtWidgets.QDialogButtonBox(self.interface_tab)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.button_box.setObjectName("button_box")
        self.vertical_layout_4.addWidget(self.button_box)
        self.tab_widget.addTab(self.interface_tab, "")
        self.plugins_tab = QtWidgets.QWidget()
        self.plugins_tab.setObjectName("plugins_tab")
        self.vertical_layout_5 = QtWidgets.QVBoxLayout(self.plugins_tab)
        self.vertical_layout_5.setObjectName("vertical_layout_5")
        self.label = QtWidgets.QLabel(self.plugins_tab)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.vertical_layout_5.addWidget(self.label)
        self.plugin_table_widget = QtWidgets.QTableWidget(self.plugins_tab)
        self.plugin_table_widget.setObjectName("plugin_table_widget")
        self.plugin_table_widget.setColumnCount(1)
        self.plugin_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.plugin_table_widget.setHorizontalHeaderItem(0, item)
        self.plugin_table_widget.horizontalHeader().setStretchLastSection(True)
        self.vertical_layout_5.addWidget(self.plugin_table_widget)
        self.add_plugin_button = QtWidgets.QPushButton(self.plugins_tab)
        self.add_plugin_button.setObjectName("add_plugin_button")
        self.vertical_layout_5.addWidget(self.add_plugin_button)
        self.tab_widget.addTab(self.plugins_tab, "")
        self.vertical_layout.addWidget(self.tab_widget)
        self.actionClose = QtWidgets.QAction(Preferences)
        self.actionClose.setObjectName("actionClose")

        self.retranslateUi(Preferences)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        _translate = QtCore.QCoreApplication.translate
        Preferences.setWindowTitle(_translate("Preferences", "Preferences"))
        self.zoom_speed_label.setText(_translate("Preferences", "Mousewheel zoom speed:"))
        self.Grid.setText(_translate("Preferences", "Grid Appearance"))
        self.grid_appearance_type_combo_box.setItemText(0, _translate("Preferences", "Circles"))
        self.grid_appearance_type_combo_box.setItemText(1, _translate("Preferences", "Lines"))
        self.grid_appearance_type_combo_box.setItemText(2, _translate("Preferences", "Points"))
        self.show_icon_label_text.setText(_translate("Preferences", "Show Icon Labels:"))
        self.show_icon_labels.setText(_translate("Preferences", "(needs restart)"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.interface_tab), _translate("Preferences", "Interface"))
        self.label.setText(_translate("Preferences", "Plugins allow custom python code execution within cadnano.\n"
"See github.com/cadnano/plugins for examples."))
        item = self.plugin_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("Preferences", "Path"))
        self.add_plugin_button.setText(_translate("Preferences", "Add Plugin"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.plugins_tab), _translate("Preferences", "Plugins"))
        self.actionClose.setText(_translate("Preferences", "Close"))
        self.actionClose.setShortcut(_translate("Preferences", "Ctrl+W"))

import cadnano.gui.ui.dialogs.dialogicons_rc
