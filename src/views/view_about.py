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


class ViewAbout(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.controls = [
            ft.Column(
                [
                    ft.Text(
                        """
I’ve been interested in technology my whole life, from games to computers.
Sound, on the other hand, has grown into my obsession.

In my eight years of working in sound, I’ve pursued the idea of the “Perfect Workflow.” I’ve focused on spending the least time fumbling with file naming, export settings, asset tracking, and other manual work and maximizing my creative time with sound. 
I get excited when I realize a line of Python code will save me 2 minutes each time it runs.

I’ve been able to continue sharing this excitement in the workplace: 
At Piranha Games, I’ve had the opportunity to design and implement sounds for their most significant IP, MechWarrior. I’ve also had a blast creating killer tools to automate workflows for my team and me. 
As a technical sound design contractor, I’ve had the privilege of prototyping audio systems. Recently, I worked on a custom method for implementing diffraction and wrote tools to track used/unused files.

In 2023, I started Game Audio Tools, working on FilePal. FilePal is a filename management and asset tracker program that works with today’s game audio tech (Reaper, Wwise, Unreal).

There’s a lot more work to do. I’ll keep my head down and ears open.  🙂
                        """
                    )
                ]
            )
        ]
