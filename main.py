import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QComboBox, QSlider, QLabel, QFrame)
from PySide6.QtCore import Qt, QTimer
from views.canvas import VisualizationCanvas
from algorithms.sorting import AlgorithmEngine
from models.data_structures import DataStructureEngine

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DSA Visualizer Desktop - Engine v0.7")
        self.resize(1100, 700)
        
        # Core Engine Controls
        self.timer = QTimer()
        self.timer.timeout.connect(self.engine_step)
        self.animation_speed = 100
        self.is_playing = False
        
        self.active_generator = None
        self.current_mode = "SORTING"
        
        self.setup_ui()
        self.bind_events()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Left Sidebar Panel
        sidebar = QFrame()
        sidebar.setFixedWidth(280)
        sidebar_layout = QVBoxLayout(sidebar)

        sidebar_layout.addWidget(QLabel("<b>Algorithm / DS Module</b>"))
        self.category_box = QComboBox()
        self.category_box.addItems(["Sorting Algorithms", "Linear Data Structures"])
        sidebar_layout.addWidget(self.category_box)

        self.selector_box = QComboBox()
        sidebar_layout.addWidget(self.selector_box)

        sidebar_layout.addSpacing(15)
        sidebar_layout.addWidget(QLabel("<b>Playback Engine</b>"))
        
        self.btn_play = QPushButton("Play")
        self.btn_step = QPushButton("Next Step")
        self.btn_reset = QPushButton("Reset Engine")
        
        sidebar_layout.addWidget(self.btn_play)
        sidebar_layout.addWidget(self.btn_step)
        sidebar_layout.addWidget(self.btn_reset)

        sidebar_layout.addSpacing(15)
        sidebar_layout.addWidget(QLabel("<b>Execution Speed</b>"))
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(10, 500)
        self.speed_slider.setValue(200)
        sidebar_layout.addWidget(self.speed_slider)

        sidebar_layout.addStretch()

        # Canvas Area
        self.canvas = VisualizationCanvas()

        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.canvas, 1)

        self.update_selector_options()

    def bind_events(self):
        self.category_box.currentIndexChanged.connect(self.update_selector_options)
        self.selector_box.currentIndexChanged.connect(self.reset_engine)
        self.btn_play.clicked.connect(self.toggle_play)
        self.btn_step.clicked.connect(self.engine_step)
        self.btn_reset.clicked.connect(self.reset_engine)
        self.speed_slider.valueChanged.connect(self.update_speed)

    def update_selector_options(self):
        self.selector_box.blockSignals(True)
        self.selector_box.clear()
        if self.category_box.currentText() == "Sorting Algorithms":
            self.current_mode = "SORTING"
            self.selector_box.addItems(["Bubble Sort", "Selection Sort", "Insertion Sort"])
        else:
            self.current_mode = "DS"
            self.selector_box.addItems(["Stack", "Queue"])
        self.selector_box.blockSignals(False)
        self.reset_engine()

    def toggle_play(self):
        if self.is_playing:
            self.timer.stop()
            self.btn_play.setText("Play")
            self.is_playing = False
        else:
            self.timer.start(510 - self.speed_slider.value())
            self.btn_play.setText("Pause")
            self.is_playing = True

    def update_speed(self, val):
        if self.is_playing:
            self.timer.setInterval(510 - val)

    def reset_engine(self):
        self.timer.stop()
        self.is_playing = False
        self.btn_play.setText("Play")
        
        if self.current_mode == "SORTING":
            algo_name = self.selector_box.currentText()
            if algo_name:
                self.active_generator, initial_data = AlgorithmEngine.get_sorting_generator(algo_name)
                self.canvas.render_sorting_state(initial_data, [])
        else:
            ds_name = self.selector_box.currentText()
            if ds_name:
                self.active_generator, _ = DataStructureEngine.get_ds_generator(ds_name)
                self.canvas.render_ds_state({"type": ds_name.upper(), "data": [], "last_op": "Initialized"})

    def engine_step(self):
        if not self.active_generator:
            return
        
        try:
            state = next(self.active_generator)
            if self.current_mode == "SORTING":
                data, active_idx = state
                self.canvas.render_sorting_state(data, active_idx)
            else:
                self.canvas.render_ds_state(state)
        except StopIteration:
            self.timer.stop()
            self.is_playing = False
            self.btn_play.setText("Completed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())