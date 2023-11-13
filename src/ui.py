import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt

class WordluxeGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("assets/game_icon.ico"))
        self.setWindowTitle("Wordluxe")

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)
        self.showFullScreen()
        self.setup_ui()

        with open('src/style.qss', 'r') as f:
            self.stylesheet = f.read()

        QApplication.instance().setStyleSheet(self.stylesheet)

    def setup_ui(self):
        self.setup_main_menu_page()
        self.setup_second_page()
        self.setup_third_page()
        self.setup_game_page()

    def setup_main_menu_page(self):
        main_menu_frame = QFrame(self.stacked_widget)
        main_menu_frame.setGeometry(0, 0, self.width(), self.height())
        main_menu_frame.setObjectName("mmframe")

        main_layout = QVBoxLayout(main_menu_frame)
        main_layout.setAlignment(Qt.AlignCenter)

        game_logo = QSvgWidget("assets/game_logo.svg", main_menu_frame)
        game_logo.setFixedSize(game_logo.sizeHint())

        play_button = QPushButton("Play", main_menu_frame, objectName="button")
        play_button.setFixedWidth(240)
        play_button.clicked.connect(self.play_button_pressed)
        play_button.setCursor(Qt.PointingHandCursor)

        quit_button = QPushButton("Quit", main_menu_frame, objectName="quitButton")
        quit_button.setFixedWidth(240)
        quit_button.clicked.connect(self.quit_button_pressed)
        quit_button.setCursor(Qt.PointingHandCursor)

        main_buttons_layout = QHBoxLayout()
        main_buttons_layout.addWidget(play_button)
        main_buttons_layout.addSpacing(30)
        main_buttons_layout.addWidget(quit_button)
        main_buttons_layout.setAlignment(Qt.AlignCenter)

        additional_text = QLabel("The new, and \nimproved wordle!", main_menu_frame)
        additional_text.setObjectName("heading")
        additional_text.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(game_logo)
        main_layout.addSpacing(60) 
        main_layout.addWidget(additional_text)
        main_layout.addSpacing(60)
        main_layout.addLayout(main_buttons_layout)

        self.stacked_widget.addWidget(main_menu_frame)

    def setup_second_page(self):
        cat_frame = QFrame(self.stacked_widget)
        cat_frame.setGeometry(0, 0, self.width(), self.height())
        cat_frame.setObjectName("cframe")

        cat_layout = QVBoxLayout()
        cat_layout.setAlignment(Qt.AlignCenter)

        cat_text = QLabel("Choose category", cat_frame)
        cat_text.setObjectName("cat_text")
        cat_text.setAlignment(Qt.AlignCenter)
        cat_layout.addWidget(cat_text)
        cat_layout.addSpacing(30)

        buttons = ["General", "Countries", "Fruits", "Sports", "Animals", "Artists", "Songs"]

        self.create_buttons(cat_layout, buttons, cat_frame, self.cat_buttons_pressed)
        self.stacked_widget.addWidget(cat_frame)

    def setup_third_page(self):
        dif_frame = QFrame(self.stacked_widget)
        dif_frame.setGeometry(0, 0, self.width(), self.height())
        dif_frame.setObjectName("dframe")

        dif_layout = QVBoxLayout()
        dif_layout.setAlignment(Qt.AlignCenter)

        dif_text = QLabel("Choose difficulty", dif_frame)
        dif_text.setObjectName("cat_text")
        dif_text.setAlignment(Qt.AlignCenter)
        dif_layout.addWidget(dif_text)
        dif_layout.addSpacing(30)

        buttons = ["Easy", "Normal", "Hard", "Extreme"]

        self.create_buttons(dif_layout, buttons, dif_frame, self.dif_buttons_pressed)

        self.stacked_widget.addWidget(dif_frame)

    def setup_game_page(self):
        game_frame = QFrame(self.stacked_widget)
        game_frame.setGeometry(0, 0, self.width(), self.height())
        game_frame.setObjectName("gframe")

        self.stacked_widget.addWidget(game_frame)

    def create_buttons(self, layout, buttons, parent, function):

        for button in buttons:
            button = QPushButton(button, parent)
            button.setFixedWidth(260)
            button.setCursor(Qt.PointingHandCursor)
            button.clicked.connect(function)

            if button.text() == "Extreme":
                button.setObjectName("extremeButton")
            else:
                button.setObjectName("button")
            layout.addWidget(button)
            layout.addSpacing(15)

        parent.setLayout(layout)

    def play_button_pressed(self):
        self.stacked_widget.setCurrentIndex(1)

    def quit_button_pressed(self):
        self.close()
    
    def cat_buttons_pressed(self):
        self.stacked_widget.setCurrentIndex(2)

    def dif_buttons_pressed(self):
        self.stacked_widget.setCurrentIndex(3)
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_instance = WordluxeGame()
    game_instance.show()
    sys.exit(app.exec_())
