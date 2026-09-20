import tkinter as tk
from tkinter import messagebox, ttk


class MainView(tk.Frame):
    """
    Interfaz principal del restaurante organizada con contenedores, componentes y pestañas,
    permitiendo la gestión completa de productos y consulta de usuarios.
    """

    def __init__(self, parent, controlador, servicio) -> None:
        super().__init__(parent)
        self.controlador = controlador
        self.servicio = servicio

        self.configure(bg="#f4f4f4")

        # Barra superior
        frame_top = tk.Frame(self, bg="#333333", height=50)
        frame_top.pack(fill="x", side="top")

        lbl_header = tk.Label(
            frame_top, text="Panel Principal - Restaurante App", font=("Arial", 14, "bold"), bg="#333333", fg="white"
        )
        lbl_header.pack(side="left", padx=15, pady=10)

        btn_salir = tk.Button(
            frame_top, text="Cerrar Sesión", font=("Arial", 10), bg="#d9534f", fg="white", command=self.controlador.mostrar_login_view
        )
        btn_salir.pack(side="right", padx=15, pady=10)

        # Contenedor de Pestañas (Notebook)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=15)

        # Pestaña 1: Gestión de Productos
        self.tab_productos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productos, text="📦 Gestión de Productos")
        self._construir_pestana_productos()

        # Pestaña 2: Consulta de Usuarios
        self.tab_usuarios = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_usuarios, text="👥 Consulta de Usuarios")
        self._construir_pestana_usuarios()

        # Cargar datos iniciales en tablas
        self.actualizar_tabla_productos()
        self.actualizar_tabla_usuarios()

    def _construir_pestana_productos(self) -> None:
        # Contenedor izquierdo: Formulario de Registro / Edición
        frame_form = ttk.LabelFrame(self.tab_productos, text=" Formulario de Producto ")
        frame_form.pack(side="left", fill="y", padx=10, pady=10, ipadx=10, ipady=10)

        ttk.Label(frame_form, text="Código:").grid(row=0, column=0, sticky="w", pady=5)
        self.ent_codigo = ttk.Entry(frame_form, width=22)
        self.ent_codigo.grid(row=0, column=1, pady=5, padx=5)

        btn_buscar = ttk.Button(frame_form, text="Buscar", command=self._buscar_producto_form)
        btn_buscar.grid(row=0, column=2, padx=2)

        ttk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky="w", pady=5)
        self.ent_nombre = ttk.Entry(frame_form, width=28)
        self.ent_nombre.grid(row=1, column=1, columnspan=2, pady=5, padx=5)

        ttk.Label(frame_form, text="Categoría:").grid(row=2, column=0, sticky="w", pady=5)
        self.ent_categoria = ttk.Entry(frame_form, width=28)
        self.ent_categoria.grid(row=2, column=1, columnspan=2, pady=5, padx=5)

        ttk.Label(frame_form, text="Precio ($):").grid(row=3, column=0, sticky="w", pady=5)
        self.ent_precio = ttk.Entry(frame_form, width=28)
        self.ent_precio.grid(row=3, column=1, columnspan=2, pady=5, padx=5)

        ttk.Label(frame_form, text="Stock:").grid(row=4, column=0, sticky="w", pady=5)
        self.ent_stock = ttk.Entry(frame_form, width=28)
        self.ent_stock.grid(row=4, column=1, columnspan=2, pady=5, padx=5)

        # Contenedor de Botones de Acción
        frame_botones = ttk.Frame(frame_form)
        frame_botones.grid(row=5, column=0, columnspan=3, pady=15)

        btn_registrar = tk.Button(frame_botones, text="Registrar", bg="#4CAF50", fg="white", width=10, command=self._registrar_producto)
        btn_registrar.grid(row=0, column=0, padx=3, pady=3)

        btn_actualizar = tk.Button(frame_botones, text="Actualizar", bg="#FF9800", fg="white", width=10, command=self._actualizar_producto)
        btn_actualizar.grid(row=0, column=1, padx=3, pady=3)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar", bg="#F44336", fg="white", width=10, command=self._eliminar_producto)
        btn_eliminar.grid(row=1, column=0, padx=3, pady=3)

        btn_limpiar = tk.Button(frame_botones, text="Limpiar", bg="#9E9E9E", fg="white", width=10, command=self._limpiar_formulario)
        btn_limpiar.grid(row=1, column=1, padx=3, pady=3)

        # Contenedor derecho: Tabla / Listado de Productos
        frame_tabla = ttk.LabelFrame(self.tab_productos, text=" Listado de Productos Registrados ")
        frame_tabla.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Treeview (Tabla)
        columnas = ("codigo", "nombre", "categoria", "precio", "stock")
        self.tree_productos = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=12)
        
        self.tree_productos.heading("codigo", text="Código")
        self.tree_productos.heading("nombre", text="Nombre")
        self.tree_productos.heading("categoria", text="Categoría")
        self.tree_productos.heading("precio", text="Precio")
        self.tree_productos.heading("stock", text="Stock")

        self.tree_productos.column("codigo", width=80, anchor="center")
        self.tree_productos.column("nombre", width=140, anchor="w")
        self.tree_productos.column("categoria", width=110, anchor="w")
        self.tree_productos.column("precio", width=80, anchor="e")
        self.tree_productos.column("stock", width=60, anchor="center")

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree_productos.yview)
        self.tree_productos.configure(yscrollcommand=scrollbar.set)

        self.tree_productos.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        scrollbar.pack(side="right", fill="y", pady=5)

    def _construir_pestana_usuarios(self) -> None:
        frame_tabla_u = ttk.LabelFrame(self.tab_usuarios, text=" Usuarios Registrados en el Sistema ")
        frame_tabla_u.pack(fill="both", expand=True, padx=15, pady=15)

        columnas_u = ("id", "nombre", "correo")
        self.tree_usuarios = ttk.Treeview(frame_tabla_u, columns=columnas_u, show="headings", height=12)
        
        self.tree_usuarios.heading("id", text="Identificación")
        self.tree_usuarios.heading("nombre", text="Nombre Completo")
        self.tree_usuarios.heading("correo", text="Correo Electrónico")

        self.tree_usuarios.column("id", width=120, anchor="center")
        self.tree_usuarios.column("nombre", width=220, anchor="w")
        self.tree_usuarios.column("correo", width=250, anchor="w")

        scrollbar_u = ttk.Scrollbar(frame_tabla_u, orient="vertical", command=self.tree_usuarios.yview)
        self.tree_usuarios.configure(yscrollcommand=scrollbar_u.set)

        self.tree_usuarios.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        scrollbar_u.pack(side="right", fill="y", pady=5)

    def actualizar_tabla_productos(self) -> None:
        for row in self.tree_productos.get_children():
            self.tree_productos.delete(row)
        productos = self.servicio.obtener_productos()
        for p in productos:
            self.tree_productos.insert("", "end", values=(p.codigo, p.nombre, p.categoria, f"${p.precio:.2f}", p.stock))

    def actualizar_tabla_usuarios(self) -> None:
        for row in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(row)
        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            self.tree_usuarios.insert("", "end", values=(u.identificacion, u.nombre, u.correo))

    def _limpiar_formulario(self) -> None:
        self.ent_codigo.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.ent_categoria.delete(0, tk.END)
        self.ent_precio.delete(0, tk.END)
        self.ent_stock.delete(0, tk.END)

    def _buscar_producto_form(self) -> None:
        codigo = self.ent_codigo.get().strip()
        if not codigo:
            messagebox.showwarning("Advertencia", "Ingrese un código para buscar.")
            return
        p = self.servicio.buscar_producto(codigo)
        if p:
            self.ent_nombre.delete(0, tk.END)
            self.ent_nombre.insert(0, p.nombre)
            self.ent_categoria.delete(0, tk.END)
            self.ent_categoria.insert(0, p.categoria)
            self.ent_precio.delete(0, tk.END)
            self.ent_precio.insert(0, str(p.precio))
            self.ent_stock.delete(0, tk.END)
            self.ent_stock.insert(0, str(p.stock))
            messagebox.showinfo("Éxito", f"Producto '{p.nombre}' encontrado y cargado en el formulario.")
        else:
            messagebox.showerror("Error", "No se encontró ningún producto con ese código.")

    def _registrar_producto(self) -> None:
        codigo = self.ent_codigo.get().strip()
        nombre = self.ent_nombre.get().strip()
        categoria = self.ent_categoria.get().strip()
        try:
            precio = float(self.ent_precio.get().strip())
            stock = int(self.ent_stock.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Precio y stock deben ser valores numéricos válidos.")
            return

        if self.servicio.registrar_producto(codigo, nombre, categoria, precio, stock):
            messagebox.showinfo("Éxito", "Producto registrado y guardado correctamente.")
            self.actualizar_tabla_productos()
            self._limpiar_formulario()
        else:
            messagebox.showerror("Error", "No se pudo registrar. Verifique que el código no exista o que los campos estén completos.")

    def _actualizar_producto(self) -> None:
        codigo = self.ent_codigo.get().strip()
        nombre = self.ent_nombre.get().strip()
        categoria = self.ent_categoria.get().strip()
        try:
            precio = float(self.ent_precio.get().strip())
            stock = int(self.ent_stock.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Precio y stock deben ser valores numéricos válidos.")
            return

        if self.servicio.actualizar_producto(codigo, nombre, categoria, precio, stock):
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            self.actualizar_tabla_productos()
            self._limpiar_formulario()
        else:
            messagebox.showerror("Error", "No se pudo actualizar. Verifique que el código exista.")

    def _eliminar_producto(self) -> None:
        codigo = self.ent_codigo.get().strip()
        if not codigo:
            messagebox.showwarning("Advertencia", "Ingrese o busque el código del producto a eliminar.")
            return
        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el producto con código {codigo}?"):
            if self.servicio.eliminar_producto(codigo):
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
                self.actualizar_tabla_productos()
                self._limpiar_formulario()
            else:
                messagebox.showerror("Error", "No se encontró el producto a eliminar.")