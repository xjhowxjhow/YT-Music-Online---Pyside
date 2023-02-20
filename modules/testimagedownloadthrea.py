# from PySide2.QtCore import Qt, QThreadPool, QRunnable, pyqtSlot

# class LoadImageRunnable(QRunnable):
#     def __init__(self, url, callback):
#         super().__init__()
#         self.url = url
#         self.callback = callback

#     @pyqtSlot()
#     def run(self):
#         pixmap = load_image(self.url)
#         self.callback(pixmap)

#     def load_image(url):
#         data = urllib.request.urlopen(url).read()
#         image = QPixmap()
#         image.loadFromData(data)
#         return image
    
# def handle_search_results(self, search_results):
#     self.tableWidget.setRowCount(0)
#     threadpool = QThreadPool.globalInstance()
#     for i, result in enumerate(search_results):
#         self.tableWidget.insertRow(i)
#         self.tableWidget.setItem(i, 0, QTableWidgetItem(result['link']))
#         self.thumbnail_button = QPushButton()
#         self.thumbnail_button.setIconSize(QtCore.QSize(200, 200))
#         self.tableWidget.setCellWidget(i, 1, self.thumbnail_button)
#         load_image_runnable = LoadImageRunnable(result['thumbnail'], lambda pixmap: self.thumbnail_button.setIcon(pixmap))
#         threadpool.start(load_image_runnable)
#         self.tableWidget.setItem(i, 2, QTableWidgetItem(result['title']))
#         self.tableWidget.item(i, 2).setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
#         self.tableWidget.setItem(i, 3, QTableWidgetItem(result['duration']))
#         self.tableWidget.setItem(i, 4, QTableWidgetItem(result['view_count']))
#         self.tableWidget.setItem(i, 5, QTableWidgetItem(result['published_time']))
