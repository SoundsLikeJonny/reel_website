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
from src.styles import Fonts
from src.views.view_about import ViewAbout
from src.views.view_error404 import ViewError404
from src.views.view_home import ViewHome


def main(page: ft.Page):
    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()

        view: ft.View = ViewError404(page)
        match page.route:
            case '/':
                view: ft.View = ViewHome(page)
            case '/about':
                view: ft.View = ViewAbout(page)
            case _:
                page.route = 'error'

        view.navigation_bar = NavBar(page)

        page.views.append(
            view
        )

        page.update()

    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)

    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.BLACK,
        font_family=Fonts.POPPINS,
        page_transitions=ft.PageTransitionsTheme(
            windows=ft.PageTransitionTheme.NONE,
            macos=ft.PageTransitionTheme.OPEN_UPWARDS,
            linux=ft.PageTransitionTheme.OPEN_UPWARDS,
            ios=ft.PageTransitionTheme.OPEN_UPWARDS
        )
    )
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
