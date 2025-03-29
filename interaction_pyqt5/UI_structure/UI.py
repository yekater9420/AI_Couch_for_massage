#
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 创建程序实例，并通过argv参数传递命令行参数
app = QApplication(sys.argv)

# 创建一个QWidget对象
window = QWidget()

# 设置窗口标题
window.setWindowTitle('智能按摩床')

# 窗口大小设置
window.resize(900, 600) # 后续根据实际情况调整

window.show()
sys.exit(app.exec_()) # 程序一直运行，直到窗口关闭





