import flet as ft

def main(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor ="#829bf5"

    # Variável com a imagem certa
    imagem_correta = "Cascão"
    
    # Texto para feedback
    mensagem = ft.Text(
        f"Qual é o {imagem_correta}?",
        text_align=ft.TextAlign.CENTER,
        size=20,
        height=50
    )

    # Função Jogar
    def jogar(e):
        imagem_selecionada = e.control.content.value
        if imagem_selecionada == imagem_correta:
            e.control.bgcolor = ft.Colors.GREEN_200
            e.control.image.opacity = 0.3
            e.control.content.value = "😁"
            e.control.content.size = 40
            mensagem.value = "Muito bem!! Você conseguiu!!."
        else:
            e.control.bgcolor = ft.Colors.RED_200
            e.control.image.opacity = 0.3
            e.control.content.value = "😣"
            e.control.content.size = 40
            mensagem.value = f"Óh não! Não é o {imagem_correta}. Tente novamente, dessa vez você consegue."
        
        container_cascao.on_click = None
        container_magali.on_click = None

        btn_jogar_novamente.visible = True

        page.update()
    
    # Função Jogar Novamente
    def jogar_novamente(e):
        btn_jogar_novamente.visible = False
        mensagem.value = f"Clique no {imagem_correta}"

        container_magali.image.opacity = 1.0
        container_magali.on_click = jogar
        container_magali.content.size = 0
        container_magali.content.value = "magali"

        container_cascao.image.opacity = 1.0
        container_cascao.on_click = jogar
        container_cascao.content.size = 0
        container_cascao.content.value = "Cascão"
        
        page.update()

    # Container GATO
    container_magali = ft.Container(
        content=ft.Text(
            "Magali",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/magali.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=100,
        height=100,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Container CACHORRO
    container_cascao= ft.Container(
        content=ft.Text(
            "Cascão",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/cascao.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=100,
        height=100,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    container_cebolinha= ft.Container(
        content=ft.Text(
            "Cebolinha",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/cebolinha.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=100,
        height=100,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Botão "Jogar Novamente"
    btn_jogar_novamente = ft.Button(
        "Jogar Novamente",
        visible=False,
        on_click=jogar_novamente
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Selecione a imagem certa",
                    size=24,
                    weight="bold"
                ),
                mensagem,
                ft.Row(
                    [
                        container_magali,
                        container_cascao,
                        container_cebolinha,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                btn_jogar_novamente
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.run(main)