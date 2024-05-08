# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:04:09 2024

@author: User
"""

import tkinter as tk
from tkinter import messagebox

class Robot:
    def __init__(self, name):
        self.name = name
        self.battery_capacity = 10
        self.action_history = []

    def move_forward(self):
        if self.battery_capacity >= 2:
            self.battery_capacity -= 2
            self.action_history.append(f"{self.name} se ha movido hacia adelante. Batería restante: {self.battery_capacity}")
            print(self.action_history[-1])
        else:
            messagebox.showinfo("Batería agotada", f"{self.name} no tiene suficiente batería para moverse hacia adelante.")

    def move_backward(self):
        if self.battery_capacity >= 1:
            self.battery_capacity -= 1
            self.action_history.append(f"{self.name} se ha movido hacia atrás. Batería restante: {self.battery_capacity}")
            print(self.action_history[-1])
        else:
            messagebox.showinfo("Batería agotada", f"{self.name} no tiene suficiente batería para moverse hacia atrás.")

    def turn(self):
        if self.battery_capacity >= 0.5:
            self.battery_capacity -= 0.5
            self.action_history.append(f"{self.name} ha girado. Batería restante: {self.battery_capacity}")
            print(self.action_history[-1])
        else:
            messagebox.showinfo("Batería agotada", f"{self.name} no tiene suficiente batería para girar.")

    def get_action_history(self):
        return "\n".join(self.action_history)

class RobotGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Control de Robots")

        # Crear los robots
        self.robot_a = Robot("Robot A")
        self.robot_b = Robot("Robot B")
        self.robot_c = Robot("Robot C")

        # Variables de control
        self.robot_selection = tk.StringVar()
        self.action_selection = tk.StringVar()

        # Crear elementos de la interfaz
        self.robot_label = tk.Label(self.root, text="Seleccionar Robot:")
        self.robot_label.pack()

        self.robot_option_menu = tk.OptionMenu(self.root, self.robot_selection, "Robot A", "Robot B", "Robot C", command=self.reset_battery)
        self.robot_option_menu.pack()

        self.battery_label = tk.Label(self.root, text="Batería restante: 10")
        self.battery_label.pack()

        self.action_label = tk.Label(self.root, text="Seleccionar Acción:")
        self.action_label.pack()

        self.action_option_menu = tk.OptionMenu(self.root, self.action_selection, "Mover hacia adelante", "Mover hacia atrás", "Girar")
        self.action_option_menu.pack()

        self.execute_button = tk.Button(self.root, text="Ejecutar Acción", command=self.execute_action)
        self.execute_button.pack()

        self.history_button = tk.Button(self.root, text="Ver Historial", command=self.show_history)
        self.history_button.pack()

        self.history_text = tk.Text(self.root, height=10, width=50)
        self.history_text.pack()

    def reset_battery(self, selected_robot):
        if selected_robot == "Robot A":
            self.robot_a.battery_capacity = 10
        elif selected_robot == "Robot B":
            self.robot_b.battery_capacity = 10
        elif selected_robot == "Robot C":
            self.robot_c.battery_capacity = 10

        self.update_battery_label()

    def execute_action(self):
        selected_robot = self.robot_selection.get()
        selected_action = self.action_selection.get()

        if selected_robot == "Robot A":
            robot = self.robot_a
        elif selected_robot == "Robot B":
            robot = self.robot_b
        elif selected_robot == "Robot C":
            robot = self.robot_c
        else:
            return

        if selected_action == "Mover hacia adelante":
            robot.move_forward()
        elif selected_action == "Mover hacia atrás":
            robot.move_backward()
        elif selected_action == "Girar":
            robot.turn()

        self.update_battery_label()

    def show_history(self):
        selected_robot = self.robot_selection.get()

        if selected_robot == "Robot A":
            history = self.robot_a.get_action_history()
        elif selected_robot == "Robot B":
            history = self.robot_b.get_action_history()
        elif selected_robot == "Robot C":
            history = self.robot_c.get_action_history()
        else:
            history = "Seleccione un robot"

        self.history_text.delete('1.0', tk.END)
        self.history_text.insert(tk.END, history)

    def update_battery_label(self):
        selected_robot = self.robot_selection.get()

        if selected_robot == "Robot A":
            battery_capacity = self.robot_a.battery_capacity
        elif selected_robot == "Robot B":
            battery_capacity = self.robot_b.battery_capacity
        elif selected_robot == "Robot C":
            battery_capacity = self.robot_c.battery_capacity
        else:
            return

        self.battery_label.config(text=f"Batería restante: {battery_capacity}")

if __name__ == "__main__":
    gui = RobotGUI()
    gui.root.mainloop()
