import tkinter as tk
from tkinter import messagebox


class LoginView(tk.Frame):
    """
    Vista gráfica de acceso simulado al sistema.
    """

    def __init__(self, parent, controlador, servicio) -> None:
        super().__init__(parent)
        self.controlador = controlador
        self.servicio = servicio

        self.configure(bg="#f0f0f0")

        lbl_titulo = tk.Label(
            self, text="SISTEMA RESTAURANTE", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333333"
        )
        lbl_titulo.pack(pady=30)

        frame_form = tk.Frame(self, bg="#ffffff", padx=20, pady=20, relief="solid", bd=1)
        frame_form.pack(pady=10)

        lbl_user = tk.Label(frame_form, text="Usuario: nombre", font=("Arial", 11), bg="#ffffff")
        lbl_user.pack(anchor="w", pady=5)
        self.entry_user = tk.Entry(frame_form, font=("Arial", 11), width=25)
        self.entry_user.pack(pady=5)

        lbl_pass = tk.Label(frame_form, text="Contraseña: identificación", font=("Arial", 11), bg="#ffffff")
        lbl_pass.pack(anchor="w", pady=5)
        self.entry_pass = tk.Entry(frame_form, font=("Arial", 11), width=25, show="*")
        self.entry_pass.pack(pady=5)

        btn_ingresar = tk.Button(
            frame_form, text="Ingresar", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", width=20, command=self._intentar_login
        )
        btn_ingresar.pack(pady=20)

    def _intentar_login(self) -> None:
        usuario = self.entry_user.get()
        clave = self.entry_pass.get()

        if self.servicio.validar_acceso(usuario, clave):
            self.controlador.mostrar_main_view()
        else:
            messagebox.showerror("Error de Acceso", "Por favor, ingrese un usuario y contraseña válidos.")