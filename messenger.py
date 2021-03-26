from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore
from clientUI import Ui_MainWindow


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        height = 654
        width = 431
        self.setFixedSize(width, height)

        # withClick button set action
        self.pushButton.pressed.connect(self.send_msg)

        # run timer to get messages from server
        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_msgs)
        self.timer.start(2000)

    # printMsgs from server to client
    def print_msgs(self, massage):
        dt = datetime.fromtimestamp(massage['time'])
        dt_str = dt.strftime('%d/%b %H:%M:%S')
        self.textBrowser.append(dt_str + ' ' + massage['name'])
        self.textBrowser.append(massage['text'])
        self.textBrowser.append('')

    # get_msgs from server
    def get_msgs(self):
        try:
            resp = requests.get(
                'http://192.168.194.111:5000/get/msgs',
                params={'after': self.after}
            )


        except:
            return

        # massages = resp.json()['msgs']
        massages = resp.json()['payload']
        for massage in massages:
            self.print_msgs(massage)
            self.after = massage['time']

    # send_msg to server
    def send_msg(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()

        try:
            resp = requests.post(
                'http://192.168.194.111:5000/send/msg',
                json={
                    'name': name,
                    'text': text
                }
            )
        except:
            self.textBrowser.append('server error, try again...')
            self.textBrowser.append('')
            return

        if resp.status_code != 200:
            self.textBrowser.append(resp.text)
            self.textBrowser.append('')
            return

        # clear textEditor after send msg
        self.textEdit.clear()


app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec()
