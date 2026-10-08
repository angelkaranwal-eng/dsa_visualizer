from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QBrush, QPen, QFont
from PySide6.QtCore import Qt

class VisualizationCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.mode = "SORTING"
        self.sorting_data = []
        self.active_indices = []
        self.ds_state = {}

    def render_sorting_state(self, data, active_indices):
        self.mode = "SORTING"
        self.sorting_data = data
        self.active_indices = active_indices
        self.update()

    def render_ds_state(self, ds_state):
        self.mode = "DS"
        self.ds_state = ds_state
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Dark Theme Workspace Background
        painter.fillRect(self.rect(), QColor(20, 22, 28))

        if self.mode == "SORTING" and self.sorting_data:
            self.draw_sorting_bars(painter)
        elif self.mode == "DS" and self.ds_state:
            self.draw_data_structure(painter)

    def draw_sorting_bars(self, painter):
        width = self.width() / len(self.sorting_data)
        max_val = max(self.sorting_data) if max(self.sorting_data) > 0 else 1

        for i, val in enumerate(self.sorting_data):
            bar_height = (val / max_val) * (self.height() - 100)
            x = i * width
            y = self.height() - bar_height - 30

            if i in self.active_indices:
                painter.setBrush(QBrush(QColor(235, 87, 87)))  # Red highlight for active swap/compare
            else:
                painter.setBrush(QBrush(QColor(86, 204, 242))) # Blue default bar

            painter.setPen(QPen(QColor(15, 15, 15), 1))
            painter.drawRect(int(x + 2), int(y), int(width - 4), int(bar_height))

            # Render Value Labels
            painter.setPen(QPen(Qt.white))
            painter.drawText(int(x + 4), int(self.height() - 10), str(val))

    def draw_data_structure(self, painter):
        painter.setPen(QPen(Qt.white))
        painter.setFont(QFont("Arial", 12))
        
        op_text = self.ds_state.get("last_op", "")
        painter.drawText(20, 30, f"Last Operation: {op_text}")

        ds_type = self.ds_state.get("type", "")
        data = self.ds_state.get("data", [])

        if ds_type == "STACK":
            # Draw Stack Blocks from bottom up
            start_x = self.width() // 2 - 60
            start_y = self.height() - 80
            
            for i, item in enumerate(data):
                val, addr = item
                y = start_y - (i * 45)
                
                painter.setBrush(QBrush(QColor(111, 207, 151))) # Green Stack Block
                painter.setPen(QPen(Qt.black, 2))
                painter.drawRect(start_x, y, 120, 40)
                
                painter.setPen(QPen(Qt.black))
                painter.drawText(start_x + 15, y + 25, f"{val} ({addr[:6]})")

        elif ds_type == "QUEUE":
            start_x = 50
            start_y = self.height() // 2 - 20
            
            for i, val in enumerate(data):
                x = start_x + (i * 70)
                
                painter.setBrush(QBrush(QColor(242, 201, 76))) # Yellow Queue Block
                painter.setPen(QPen(Qt.black, 2))
                painter.drawRect(x, start_y, 60, 40)
                
                painter.setPen(QPen(Qt.black))
                painter.drawText(x + 20, start_y + 25, str(val))