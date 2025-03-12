import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton, QGroupBox, QFormLayout)

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setFixedSize(450, 550) 

        main_layout = QVBoxLayout()

        # identitas
        identitas_group = QGroupBox("Identitas")
        identitas_layout = QVBoxLayout();
        identitas_layout.addWidget(QLabel("Nama : Nabila Nur Syfani"))
        identitas_layout.addWidget(QLabel("Nim   : F1D022082"))
        identitas_layout.addWidget(QLabel("Kelas : D"))
        identitas_group.setLayout(identitas_layout)

        label_width = 60  

        # navigation
        nav_group = QGroupBox("Navigation")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)

        # user registration
        form_group = QGroupBox("User Registration")
        form_layout = QFormLayout()

        full_name_label = QLabel("Full Name:")
        full_name_label.setFixedWidth(label_width)
        self.full_name = QLineEdit()
        self.full_name.setMinimumWidth(200)

        email_label = QLabel("Email:")
        email_label.setFixedWidth(label_width)
        self.email = QLineEdit()
        self.email.setMinimumWidth(200)

        phone_label = QLabel("Phone:")
        phone_label.setFixedWidth(label_width)
        self.phone = QLineEdit()
        self.phone.setMinimumWidth(200)

        gender_layout = QHBoxLayout()
        self.gender_male = QRadioButton("Male")
        self.gender_female = QRadioButton("Female")
        gender_layout.addWidget(self.gender_male)
        gender_layout.addWidget(self.gender_female)

        country_label = QLabel("Country:")
        country_label.setFixedWidth(label_width)
        self.country = QComboBox()
        self.country.addItems(["Select Country", "Indonesia", "Thailand", "Canada", "Australia", "Korea", "China", "Jepang",])

        form_layout.addRow(full_name_label, self.full_name)
        form_layout.addRow(email_label, self.email)
        form_layout.addRow(phone_label, self.phone)
        form_layout.addRow(QLabel("Gender:"), gender_layout)
        form_layout.addRow(country_label, self.country)
        form_group.setLayout(form_layout)

        # actions
        actions_group = QGroupBox("Actions")
        actions_layout = QHBoxLayout()
        actions_layout.addWidget(QPushButton("Submit"))
        actions_layout.addWidget(QPushButton("Cancel"))
        actions_group.setLayout(actions_layout)

        # tambahkan widget ke main layout
        main_layout.addWidget(identitas_group)
        main_layout.addWidget(nav_group)
        main_layout.addWidget(form_group)
        main_layout.addWidget(actions_group)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = RegistrationForm()
    ex.show()
    sys.exit(app.exec_())

