from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Input
from textual.containers import Vertical


class MiApp(App):
    def compose(self) -> ComposeResult:
        # Usamos un contenedor vertical para order
        with Vertical():
            yield Static("Probando entrada de texto")
            yield Input(placeholder="Escribí algo...", id="entrada")
            yield Button("Mostrar texto", id="boton")
            yield Static("", id="salida")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "boton":
            entrada = self.query_one("#entrada", Input)
            salida = self.query_one("#salida", Static)
            salida.update(f"Escribiste: {entrada.value}.")


if __name__ == "__main__":
    app = MiApp()
    app.run()
