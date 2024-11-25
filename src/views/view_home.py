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

from src.controls.navbar import NavBar


class ViewHome(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route='/'
        )

        page.theme_mode = ft.ThemeMode.LIGHT
        page.scroll = ft.ScrollMode.ADAPTIVE
        page.auto_scroll = True

        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Column(
                    [
                        ft.Text(
                            'Sound Design Reel'
                        ),
                        ft.Container(
                            height=300,
                            width=600,
                            content=ft.Video(
                                playlist=[
                                    ft.VideoMedia('https://www.youtube.com/watch?v=Cr2WM1LCJEk')
                                ]
                            )
                        )
                    ],
                )
            )
        ]
