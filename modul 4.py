import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox

class Menu(QWidget):

	switch_window_1 = QtCore.pyqtSignal()
	switch_window_2 = QtCore.pyqtSignal()
	switch_window_3 = QtCore.pyqtSignal()

	def __init__(self):
		super().__init__()
		self.setWindowTitle("Menu")
		self.resize(600, 300)

		layout = QGridLayout()

		button1 = QPushButton("Tabungan ")
		button1.clicked.connect(self.button1_clicked)
		layout.addWidget(button1, 1, 0)

		button2 = QPushButton("Peminjaman")
		button2.clicked.connect(self.button2_clicked)
		layout.addWidget(button2, 3, 0)

		button3 = QPushButton("Anggaran Bulanan")
		button3.clicked.connect(self.button3_clicked)
		layout.addWidget(button3, 5, 0)

		self.setLayout(layout)

	def button1_clicked(self):
		self.switch_window_1.emit()

	def button2_clicked(self):
		self.switch_window_2.emit()

	def button3_clicked(self):
		self.switch_window_3.emit()

class TabunganBerjangka(QWidget):

	switch_window = QtCore.pyqtSignal()

	def __init__(self):
		super().__init__()
		self.setWindowTitle('Tabungan ')
		self.resize(600, 300)

		layout = QGridLayout()

		label_jangka_waktu = QLabel('<font size="4"> Jangka waktu </font>')
		self.lineEdit_jangka_waktu = QLineEdit()
		self.lineEdit_jangka_waktu.setPlaceholderText('Lama Memiinjam')
		layout.addWidget(label_jangka_waktu, 0, 0, 1, 2)
		layout.addWidget(self.lineEdit_jangka_waktu, 0, 2, 1, 3)

		label_penarikan_per_bulan = QLabel('<font size="4"> Penarikan  </font>')
		self.lineEdit_penarikan_per_bulan = QLineEdit()
		self.lineEdit_penarikan_per_bulan.setPlaceholderText('Silahkan masukkan penarikan')
		layout.addWidget(label_penarikan_per_bulan, 2, 0, 1, 2)
		layout.addWidget(self.lineEdit_penarikan_per_bulan, 2, 2, 1, 3)

		label_nomor_rekening = QLabel('<font size="4"> Nomor rekening </font>')
		self.lineEdit_nomor_rekening = QLineEdit()
		self.lineEdit_nomor_rekening.setPlaceholderText('masukkan nomer rekening')
		layout.addWidget(label_nomor_rekening, 4, 0, 1, 2)
		layout.addWidget(self.lineEdit_nomor_rekening, 4, 2, 1, 3)


		OK = QPushButton('OK')
		OK.clicked.connect(self.close)
		layout.addWidget(OK, 6, 3)

		Cancel = QPushButton('Cancel')
		Cancel.clicked.connect(self.cancel)
		layout.addWidget(Cancel, 6, 4)

		self.setLayout(layout)

	def cancel(self):
		self.switch_window.emit()

class Peminjaman(QWidget):

	switch_window = QtCore.pyqtSignal()

	def __init__(self):
		super().__init__()
		self.setWindowTitle('Peminjaman')
		self.resize(600, 300)

		layout = QGridLayout()

		label_jumlah_peminjaman = QLabel('<font size="4"> Jumlah peminjaman </font>')
		self.lineEdit_jumlah_peminjaman = QLineEdit()
		self.lineEdit_jumlah_peminjaman.setPlaceholderText('masukkan jumlah peminjaman')
		layout.addWidget(label_jumlah_peminjaman, 0, 0, 1, 2)
		layout.addWidget(self.lineEdit_jumlah_peminjaman, 0, 2, 1, 3)

		label_lama_peminjaman = QLabel('<font size="4"> Lama peminjaman </font>')
		self.lineEdit_lama_peminjaman = QLineEdit()
		self.lineEdit_lama_peminjaman.setPlaceholderText('masukkan lama peminjaman')
		layout.addWidget(label_lama_peminjaman, 2, 0, 1, 2)
		layout.addWidget(self.lineEdit_lama_peminjaman, 2, 2, 1, 3)

		label_nama_peminjam = QLabel('<font size="4"> Nama peminjam </font>')
		self.lineEdit_nama_peminjam = QLineEdit()
		self.lineEdit_nama_peminjam.setPlaceholderText('masukkan nama peminjam')
		layout.addWidget(label_nama_peminjam, 4, 0, 1, 2)
		layout.addWidget(self.lineEdit_nama_peminjam, 4, 2, 1, 3)


		OK = QPushButton('OK')
		OK.clicked.connect(self.close)
		layout.addWidget(OK, 6, 3)

		Cancel = QPushButton('Cancel')
		Cancel.clicked.connect(self.cancel)
		layout.addWidget(Cancel, 6, 4)

		self.setLayout(layout)

	def cancel(self):
		self.switch_window.emit()

class AnggaranBulanan(QWidget):

	switch_window = QtCore.pyqtSignal()

	def __init__(self):
		super().__init__()
		self.setWindowTitle('Anggaran Bulanan')
		self.resize(600, 300)

		layout = QGridLayout()

		label_anggaran_tempat = QLabel('<font size="4"> Anggaran tempat </font>')
		self.lineEdit_anggaran_tempat = QLineEdit()
		self.lineEdit_anggaran_tempat.setPlaceholderText('masukkan anggaran tempat')
		layout.addWidget(label_anggaran_tempat, 0, 0, 1, 2)
		layout.addWidget(self.lineEdit_anggaran_tempat, 0, 2, 1, 3)

		label_anggaran_peralatan = QLabel('<font size="4"> Anggaran peralatan </font>')
		self.lineEdit_anggaran_peralatan = QLineEdit()
		self.lineEdit_anggaran_peralatan.setPlaceholderText('masukkan anggaran peralatan')
		layout.addWidget(label_anggaran_peralatan, 2, 0, 1, 2)
		layout.addWidget(self.lineEdit_anggaran_peralatan, 2, 2, 1, 3)

		label_anggaran_perlengkapan = QLabel('<font size="4"> Anggaran perlengkapan </font>')
		self.lineEdit_anggaran_perlengkapan = QLineEdit()
		self.lineEdit_anggaran_perlengkapan.setPlaceholderText('masukkan anggaran perlengkapan')
		layout.addWidget(label_anggaran_perlengkapan, 4, 0, 1, 2)
		layout.addWidget(self.lineEdit_anggaran_perlengkapan, 4, 2, 1, 3)


		OK = QPushButton('OK')
		OK.clicked.connect(self.close)
		layout.addWidget(OK, 6, 3)

		Cancel = QPushButton('Cancel')
		Cancel.clicked.connect(self.cancel)
		layout.addWidget(Cancel, 6, 4)

		self.setLayout(layout)

	def cancel(self):
		self.switch_window.emit()

class Login(QWidget):

	switch_window = QtCore.pyqtSignal()

	def __init__(self):
		super().__init__()
		self.setWindowTitle('Login')
		self.resize(600, 300)

		layout = QGridLayout()

		label_name = QLabel('<font size="4"> Username </font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText(' username')
		layout.addWidget(label_name, 1, 0)
		layout.addWidget(self.lineEdit_username, 1, 1, 1, 2)

		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setPlaceholderText(' password')
		layout.addWidget(label_password, 3, 0)
		layout.addWidget(self.lineEdit_password, 3, 1, 1, 2)

		button_login = QPushButton('Login')
		button_login.clicked.connect(self.check_password)
		layout.addWidget(button_login, 5, 1, 1, 2)

		self.setLayout(layout)

	def check_password(self):
		msg = QMessageBox()

		if self.lineEdit_username.text() == 'zaka' and self.lineEdit_password.text() == 'fahmi':
			self.switch_window.emit()
		else:
			msg.setText('Username atau password salah')
			msg.exec_()

class Controller:

	def __init__(self):
		self.login = Login()
		self.menu = Menu()
		self.tabungan_berjangka = TabunganBerjangka()
		self.peminjaman = Peminjaman()
		self.anggaran_bulanan = AnggaranBulanan()

	def show_login(self):
		self.login.switch_window.connect(self.show_menu)
		self.login.show()

	def show_menu(self):
		self.login.close()
		self.tabungan_berjangka.close()
		self.peminjaman.close()
		self.anggaran_bulanan.close()
		self.menu.show()
		self.menu.switch_window_1.connect(self.show_tabungan_berjangka)
		self.menu.switch_window_2.connect(self.show_peminjaman)
		self.menu.switch_window_3.connect(self.show_anggaran_bulanan)

	def show_tabungan_berjangka(self):
		self.menu.close()
		self.tabungan_berjangka.show()
		self.tabungan_berjangka.switch_window.connect(self.show_menu)

	def show_peminjaman(self):
		self.menu.close()
		self.peminjaman.show()
		self.peminjaman.switch_window.connect(self.show_menu)

	def show_anggaran_bulanan(self):
		self.menu.close()
		self.anggaran_bulanan.show()
		self.anggaran_bulanan.switch_window.connect(self.show_menu)


def main():
	app = QApplication(sys.argv)
	controller = Controller()
	controller.show_login()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
