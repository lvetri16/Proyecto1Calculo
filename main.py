import flet as ft
from flet import ElevatedButton, Row, Page
from convertor import main1
from matrices import main2


def main(page: ft.Page):
    def opcion1(event):
        page.clean()
        page.add(boton_regresar)
        main1(page)
    def opcion2(event):
        page.clean()
        page.add(boton_regresar)
        main2(page)
    def regresar(event):
        page.clean()
        page.add(boton_regresar, fila_boton, Row(alignment=ft.MainAxisAlignment.CENTER, width=70, height=80) , fila_boton2)
        
    click = ElevatedButton(text='Convertor', scale=2, on_click=opcion1)
    fila_boton= Row([click])
    fila_boton.alignment = 'center'
    
    click2 = ElevatedButton(text='Gauss-Jordan',  scale=2, on_click=opcion2)
    fila_boton2 = Row([click2])
    fila_boton2.alignment = 'center'
    
    boton_r = ElevatedButton(text = 'regresar', scale=1, on_click=regresar)
    boton_regresar = Row([boton_r])
    boton_regresar.alignment = 'start'
    page.add(boton_regresar, fila_boton, Row(alignment=ft.MainAxisAlignment.CENTER, width=70, height=80) , fila_boton2)
ft.app(target=main)
    
    