# Developed by Member 1: Angel Karanwal (Lead - Core Execution Engine)

import sys
import random
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QSlider, QLabel, QComboBox)
from PySide6.QtCore import QTimer, Qt

# Importing member modules
from models.data_structures import StackModel
from algorithms.sorting import bubble_sort_generator, selection_sort_generator, insertion_sort_generator
from views.canvas import VisualizerCanvas


class AlgoLabMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AlgoLab - DSA Visualizer (Team IDS-III-2026-T019)")
        self.resize(1000, 650)
        self.setStyleSheet("background-color: #0f172a; color: #f8fafc;")

        # Core State
        self.array = [45, 12, 89, 34, 67, 23, 90, 11]
        self.generator = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_step)
        self.stack_model = StackModel()

        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        # Left Control Panel
        control_panel = QVBoxLayout()
        control_panel.setContentsMargins(15, 15, 15, 15)

        title = QLabel("AlgoLab Controls")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #38bdf8;")
        control_panel.addWidget(title)

        # Select Mode / Algo
        control_panel.addWidget(QLabel("Select Feature:"))
        self.algo_box = QComboBox()
        self.algo_box.addItems(["Bubble Sort", "Selection Sort", "Insertion Sort", "Stack Simulation"])
        self.algo_box.setStyleSheet("background-color: #1e293b; padding: 6px; border-radius: 4px;")
        control_panel.addWidget(self.algo_box)

        # Buttons
        self.btn_start = QPushButton("Play")
        self.btn_start.setStyleSheet("background-color: #10b981; padding: 8px; font-weight: bold; border-radius: 4px;")
        self.btn_start.clicked.connect(self.start_visualization)

        self.btn_step = QPushButton("Next Step")
        self.btn_step.setStyleSheet("background-color: #3b82f6; padding: 8px; font-weight: bold; border-radius: 4px;")
        self.btn_step.clicked.connect(self.next_step)

        self.btn_reset = QPushButton("Reset / Randomize")
        self.btn_reset.setStyleSheet("background-color: #ef4444; padding: 8px; font-weight: bold; border-radius: 4px;")
        self.btn_reset.clicked.connect(self.reset_data)

        control_panel.addWidget(self.btn_start)
        control_panel.addWidget(self.btn_step)
        control_panel.addWidget(self.btn_reset)

        # Speed Slider
        control_panel.addWidget(QLabel("Speed Control:"))
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(100, 1000)
        self.speed_slider.setValue(400)
        self.speed_slider.valueChanged.connect(self.update_speed)
        control_panel.addWidget(self.speed_slider)

        control_panel.addStretch()

        # Canvas (Member 4 Visual Renderer)
        self.canvas = VisualizerCanvas()

        main_layout.addLayout(control_panel, 1)
        main_layout.addWidget(self.canvas, 3)

    def start_visualization(self):
        selected = self.algo_box.currentText()
        if "Sort" in selected:
            if selected == "Bubble Sort":
                self.generator = bubble_sort_generator(self.array)
            elif selected == "Selection Sort":
                self.generator = selection_sort_generator(self.array)
            elif selected == "Insertion Sort":
                self.generator = insertion_sort_generator(self.array)

            self.timer.start(1100 - self.speed_slider.value())
        elif selected == "Stack Simulation":
            # Push a random element onto stack
            val = random.randint(10, 99)
            self.stack_model.push(val)
            self.canvas.set_ds_state(self.stack_model.get_state())

    def next_step(self):
        if self.generator:
            try:
                state = next(self.generator)
                self.canvas.set_sorting_state(state['array'], state['active'], state['action'])
                if state['action'] == 'DONE':
                    self.timer.stop()
            except StopIteration:
                self.timer.stop()

    def update_speed(self, val):
        if self.timer.isActive():
            self.timer.setInterval(1100 - val)

    def reset_data(self):
        self.timer.stop()
        self.array = [random.randint(10, 95) for _ in range(8)]
        self.canvas.set_sorting_state(self.array, [], "")
        self.stack_model = StackModel()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AlgoLabMainWindow()
    window.show()
    sys.exit(app.exec())