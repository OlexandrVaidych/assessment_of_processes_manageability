import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 210)

        self.visualize_button = QPushButton("Visualize input data", self)
        self.visualize_button.setGeometry(50, 25, 150, 30)
        self.visualize_button.clicked.connect(self.visualize_input_data)

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