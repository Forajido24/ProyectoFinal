import os
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class DistanceData:
	def __init__(self):
		self.warehouse = []
		self.a = []
		self.b = []
		self.c = []
		self.d = []
		self.e = []
		self.f = []
		self.g = []
		self.h = []
		self.i = []

def get_location(df):
	return df['Location']

def get_notation(df):
	return df['Notation']

def get_dis_warehouse(df):
	return df['Distance from Warehouse (in kms)'].tolist()

def get_dis_a(df):
	return df['Distance from A'].tolist()

def get_dis_b(df):
	return df['Distance from B'].tolist()

def get_dis_c(df):
	return df['Distance from C'].tolist()

def get_dis_d(df):
	return df['Distance from D'].tolist()

def get_dis_e(df):
	return df['Distance from E'].tolist()

def get_dis_f(df):
	return df['Distance from F'].tolist()

def get_dis_g(df):
	return df['Distance from G'].tolist()

def get_dis_h(df):
	return df['Distance from H'].tolist()

def get_dis_i(df):
	return df['Distance from I'].tolist()

def select_file():
	global file
	global dis

	cwd = os.getcwd()
	file_types = [
		("CSV", "*.csv"),
		("All files", "*.*"),
	]

	file = filedialog.askopenfilename(
		title="Select a file", initialdir=cwd, filetypes=file_types
	)

	if file:
		df = pd.read_csv(file, header=0)

		location = get_location(df)
		notation = get_notation(df)

		dis = DistanceData()
		dis.warehouse = get_dis_warehouse(df)
		dis.a = get_dis_a(df)
		dis.b = get_dis_b(df)
		dis.c = get_dis_c(df)
		dis.d = get_dis_d(df)
		dis.e = get_dis_e(df)
		dis.f = get_dis_f(df)
		dis.g = get_dis_g(df)
		dis.h = get_dis_h(df)
		dis.i = get_dis_i(df)

		return location, notation, dis



def gui():
	root = tk.Tk()
	root.title("Problema del Enrutamiento del Vehículo")
	frm = ttk.Frame(root, padding=30)
	frm.grid()
	ttk.Button(frm, text="Select File ", command=select_file).grid(column=0, row=0)
	root.mainloop()

gui()
