# Developed by Member 4: Anuja (UI Canvas & Visual Renderer)

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QFont, QBrush, QPen
from PySide6.QtCore import Qt

class VisualizerCanvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mode = "SORTING"  # "SORTING" or "DS"
        self.array = [40, 10, 70, 30, 90, 50, 20, 80]
        self.active_indices = []
        self.action = ""
        self.ds_state = []  # List of tuples (val, hex_addr)

    def set_sorting_state(self, array, active, action):
        self.mode = "SORTING"
        self.array = array
        self.active_indices = active
        self.action = action
        self.update()  # Triggers paintEvent

    def set_ds_state(self, ds_state):
        self.mode = "DS"
        self.ds_state = ds_state
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Dark Background
        painter.fillRect(self.rect(), QColor("#0f172a"))

        if self.mode == "SORTING":
            self.draw_sorting(painter)
        else:
            self.draw_ds(painter)

    def draw_sorting(self, painter):
        if not self.array:
            return
        
        w = self.width()
        h = self.height()
        n = len(self.array)
        margin = 40
        bar_width = (w - (2 * margin) - (n * 5)) / n
        max_val = max(self.array) if max(self.array) > 0 else 100

        for i, val in enumerate(self.array):
            bar_height = (val / max_val) * (h - 120)
            x = margin + i * (bar_width + 5)
            y = h - margin - bar_height

            # Color logic based on active state
            if i in self.active_indices:
                if self.action == "SWAP":
                    color = QColor("#ef4444")  # Red for Swap
                else:
                    color = QColor("#f59e0b")  # Yellow for Compare
            else:
                color = QColor("#3b82f6")  # Blue for Normal

            painter.setBrush(QBrush(color))
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(int(x), int(y), int(bar_width), int(bar_height), 4, 4)

            # Draw value on top
            painter.setPen(QPen(QColor("#f8fafc")))
            painter.setFont(QFont("Segoe UI", 10, QFont.Bold))
            painter.drawText(int(x), int(y - 20), int(bar_width), 20, Qt.AlignCenter, str(val))

    def draw_ds(self, painter):
        w = self.width()
        h = self.height()
        
        painter.setFont(QFont("Segoe UI", 10, QFont.Bold))

        if not self.ds_state:
            painter.setPen(QPen(QColor("#94a3b8")))
            painter.drawText(0, 0, w, h, Qt.AlignCenter, "Memory Stack Empty")
            return

        box_width = 160
        box_height = 50
        start_x = (w - box_width) / 2
        start_y = h - 80

        for i, (val, hex_addr) in enumerate(self.ds_state):
            y = start_y - (i * (box_height + 10))

            # Draw memory block
            painter.setBrush(QBrush(QColor("#1e293b")))
            painter.setPen(QPen(QColor("#10b981"), 2))
            painter.drawRoundedRect(int(start_x), int(y), box_width, box_height, 6, 6)

            # Draw Value & Address
            painter.setPen(QPen(QColor("#f8fafc")))
            painter.drawText(int(start_x), int(y + 8), box_width, 20, Qt.AlignCenter, f"Val: {val}")
            
            painter.setPen(QPen(QColor("#64748b")))
            painter.setFont(QFont("Consolas", 9))
            painter.drawText(int(start_x), int(y + 28), box_width, 18, Qt.AlignCenter, f"[{hex_addr}]")