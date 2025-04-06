import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from qt_Framework import Ui_Form  # 假设转换后的类名是Ui_Form


class ChatWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        self.setWindowTitle("按摩床")
        # 初始化消息区域
        self.user_text_browser.clear()
        self.ai_text_browser.clear()

    def connect_signals(self):
        # 信息交流部分信号
        self.send_btn.clicked.connect(self.send_message)
        self.input_edit.returnPressed.connect(self.send_message)
        # 按钮部分信号
        self.power_btn.clicked.connect(self.power_button_click)
        # 其他按钮按此方式连接
        self.act_btn.clicked.connect(self.act_btn_click)
        self.set_up_btn.clicked.connect(self.set_up_btn_click)
        self.pushButton_1.clicked.connect(self.pushButton_1_click)
        self.pushButton_2.clicked.connect(self.pushButton_2_click)
        self.pushButton_3.clicked.connect(self.pushButton_3_click)
        self.pushButton_4.clicked.connect(self.pushButton_4_click)
        self.pushButton_5.clicked.connect(self.pushButton_5_click)
        self.pushButton_6.clicked.connect(self.pushButton_6_click)
        self.pushButton_7.clicked.connect(self.pushButton_7_click)
        self.pushButton_8.clicked.connect(self.pushButton_8_click)
        self.pushButton_9.clicked.connect(self.pushButton_9_click)
        self.pushButton_10.clicked.connect(self.pushButton_10_click)
        # 其他按钮按此方式连接

    def send_message(self):
        user_text = self.input_edit.text().strip()
        if not user_text:
            return
        self.user_text_browser.append(f"用户：{user_text}")
        # 模拟AI回复
        ai_response = "这是AI的回复"
        self.ai_text_browser.append(f"AI：{ai_response}")
        self.input_edit.clear()

    def power_button_click(self):
        QMessageBox.information(self, "提示", "电源按钮被点击")
        # 其他按钮的槽函数按需求编写
    def act_btn_click(self):
        QMessageBox.information(self, "提示", "启动按钮被点击")
        # 其他按钮的槽函数按需求编写
    def set_up_btn_click(self):
        QMessageBox.information(self, "提示", "设置按钮被点击")
        # 其他按钮的槽函数按需求编写
    def pushButton_1_click(self):
        QMessageBox.information(self, "提示", "按钮被点击")
        # 其他按钮的槽函数按需求编写
    def pushButton_2_click(self):
        QMessageBox.information(self, "提示", "按钮被点击")
        # 其他按钮的槽函数按需求编写
    def pushButton_3_click(self):
        QMessageBox.information(self, "提示", "按钮被点击")
        # 其他按钮的槽函数按需求编写
    def pushButton_4_click(self):
        QMessageBox.information(self, "提示", "按钮被点击")
        # 其他按钮的槽函数按需求编写
    def pushButton_5_click(self):
        QMessageBox.information(self, "提示", "按钮被点击")
        # 其他按钮的槽函数按需求编写
    def pushButton_6_click(self):
        QMessageBox.information(self, "提示", "按钮被点击")
        # 其他按钮的槽函数按需求编写
    def pushButton_7_click(self):
        QMessageBox.information(self, "提示", "按钮被点击")
        # 其他按钮的槽函数按需求编写
    def pushButton_8_click(self):
        QMessageBox.information(self, "提示", "按钮被点击")
        # 其他按钮的槽函数按需求编写
    def pushButton_9_click(self):
        QMessageBox.information(self, "提示", "按钮被点击")
        # 其他按钮的槽函数按需求编写
    def pushButton_10_click(self):
        QMessageBox.information(self, "提示", "按钮被点击")
        # 其他按钮的槽函数按需求编写


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
