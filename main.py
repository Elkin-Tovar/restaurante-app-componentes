import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp(tk.Tk):
    """
    Ventana principal de la aplicación que administra el ciclo de vida
    y la alternancia de vistas (Login y Main).
    """

    def __init__(self) -> None:
        super().__init__()
        self.title("Sistema de Restaurante - Componentes y Contenedores (Semana 14)")
        self.geometry("900x550")
        self.minsize(800, 500)

        # Instancia única del servicio de negocio
        self.servicio = RestauranteServicio()

        # Contenedor principal de vistas
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.vista_actual = None
        self.mostrar_login_view()

    def mostrar_login_view(self) -> None:
        if self.vista_actual:
            self.vista_actual.destroy()
        self.vista_actual = LoginView(self.container, self, self.servicio)
        self.vista_actual.grid(row=0, column=0, sticky="nsew")

    def mostrar_main_view(self) -> None:
        if self.vista_actual:
            self.vista_actual.destroy()
        self.vista_actual = MainView(self.container, self, self.servicio)
        self.vista_actual.grid(row=0, column=0, sticky="nsew")


def main() -> None:
    app = RestauranteApp()
    app.mainloop()


if __name__ == "__main__":
    main()