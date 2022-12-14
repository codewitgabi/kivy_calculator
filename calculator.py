import re
import kivy
kivy.require("2.0.0")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty


class FloatInput(TextInput):
	pat = re.compile('[^0-9/+*-]')
	def insert_text(self, substring, from_undo=False):
		pat = self.pat
		if '.' in self.text:
			s = re.sub(pat, '', substring)
		else:
			s = '.'.join(re.sub(pat, '', s)for s in substring.split('.', 1))
		return super().insert_text(s, from_undo=from_undo) 
		

class CalculatorWidget(Widget):
	input_text = StringProperty("")
	answer = ObjectProperty(None)
	operators = ["*", "/", "+", "-"]
	double_operators =["*-", "/-"]
		
	def one(self, widget):
		if self.input_text == "0":
			self.input_text = "1"
		else:
			self.input_text += "1"
		
	def two(self, widget):
		if self.input_text == "0":
			self.input_text = "2"
		else:
			self.input_text += "2"
		
	def three(self, widget):
		if self.input_text == "0":
			self.input_text = "3"
		else:
			self.input_text += "3"
		
	def four(self, widget):
		if self.input_text == "0":
			self.input_text = "4"
		else:
			self.input_text += "4"
		
	def five(self, widget):
		if self.input_text == "0":
			self.input_text = "5"
		else:
			self.input_text += "5"
		
	def six(self, widget):
		if self.input_text == "0":
			self.input_text = "6"
		else:
			self.input_text += "6"
		
	def seven(self, widget):
		if self.input_text == "0":
			self.input_text = "7"
		else:
			self.input_text += "7"
		
	def eight(self, widget):
		if self.input_text == "0":
			self.input_text = "8"
		else:
			self.input_text += "8"
		
	def nine(self, widget):
		if self.input_text == "0":
			self.input_text = "9"
		else:
			self.input_text += "9"
		
	def zero(self, widget):
		if len(self.input_text) > 0:
			self.input_text += "0"
		
	def addition(self, widget):
		try:
			if self.input_text[-2:] in self.double_operators:
				print(self.input_text[-2:])
				self.input_text = self.input_text[:-2] + "+"
			else:
				if self.input_text[-1] in self.operators:
					self.input_text = self.input_text[:-1] + "+"
				else:
					self.input_text += "+"
		except:
			pass
		
	def multiplication(self, widget):
		try:
			if self.input_text[-2:] in self.double_operators:
				print(self.input_text[-2:])
				self.input_text = self.input_text[:-2] + "*"
			else:
				if self.input_text[-1] in self.operators:
					self.input_text = self.input_text[:-1] + "*"
				else:
					self.input_text += "*"
		except:
			pass
		
	def division(self, widget):
		try:
			if self.input_text[-2:] in self.double_operators:
				print(self.input_text[-2:])
				self.input_text = self.input_text[:-2] + "/"
			else:
				if self.input_text[-1] in self.operators:
					self.input_text = self.input_text[:-1] + "/"
				else:
					self.input_text += "/"
		except:
			pass
		
	def subtraction(self, widget):
		try:
			if self.input_text[-1] in self.operators[:2]:
				self.input_text += "-"
			else:
				if self.input_text[-1] in self.operators[2:]: 
					self.input_text = self.input_text[:-1] + "-"
				else:
					self.input_text += "-"
		except:
			pass
		
	def fullstop(self, widget):
		if len(self.input_text) == 0:
			self.input_text += "0."
		else:
			if "." not in self.input_text:
				self.input_text += "."
				
	def modulus(self, widget):
		try:
			self.input_text += "%"
		except:
			pass
		
	def delete(self, widget):
		self.input_text = self.input_text[:len(self.input_text)-1]
		
	def square(self, widget):
		try:
			if self.input_text[-1] != "*" and self.input_text[-1] != "**":
				self.input_text += "**"
		except:
			pass
			
	def cancel_button(self, widget):
		self.input_text = ""
		self.answer.text = ""
		
	def equal_to(self, widget):
		try:
			print(eval(self.input_text))
			self.answer.text = f"{round(eval(self.input_text), 8):,}"
		except:
			self.answer.text = "NaN"
			

class CalculatorApp(App):
	def build(self):
		Window.clearcolor = (1,1,1,1)
		return CalculatorWidget()
		
		
if __name__ == "__main__":
	CalculatorApp().run()