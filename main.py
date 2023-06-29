import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 210)

        self.visualize_button = QPushButton("Visualize input data", self)
        self.visualize_button.setGeometry(50, 25, 150, 30)
        self.visualize_button.clicked.connect(self.visualize_input_data)

        self.terms_label = QLabel("Terms: T4, T5, T5, T5, T3", self)
        self.terms_label.setGeometry(50, 75, 150, 30)

        self.weight_coeffs_label = QLabel("Weight coefficients: 8, 9, 9, 10, 5", self)
        self.weight_coeffs_label.setGeometry(50, 100, 200, 30)


    def visualize_input_data(self):
        criteria = ['K1', 'K2', 'K3', 'K4', 'K5']

        values = [0.7, 0.5, 0.5, 0.9, 0.6]

        #Create a bar chart
        plt.bar(criteria, values)

        plt.show()


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()