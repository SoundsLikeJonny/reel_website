#  Copyright (c) 2024 Jon Evans
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.


import flet as ft

from src.styles import ButtonStyles


class NavBar(ft.AppBar):
    def __init__(self, page: ft.Page):
        super().__init__(
            toolbar_height=200,
            leading_width=300,
            leading=ft.Container(
                ft.TextButton(
                    expand=True,
                    on_click=lambda _: page.go('/'),
                    style=ButtonStyles.DEFAULT,
                    content=ft.Image(
                        '/logo.png',
                        fit=ft.ImageFit.FIT_WIDTH,
                    ),
                ),
                padding=00,
                expand=True,
            ),
            automatically_imply_leading=True,
            center_title=True,
            title=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.TextButton(
                            'Home | Reel',
                            on_click=lambda _: page.go('/')
                        ),
                        ft.TextButton(
                            'About',
                            on_click=lambda _: page.go('/about')
                        ),
                    ]
                ),
            ),
            actions=[
                ft.Container(
                    content=ft.IconButton(
                        icon=ft.icons.MAIL_OUTLINE_ROUNDED,
                        on_click=lambda _: page.go('mailto:jon.evans.audio@gmail.com')
                    ),
                    padding=50

                )
            ]
        )
