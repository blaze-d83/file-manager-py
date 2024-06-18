import os
from textual.app import App
from textual.widgets import ListView, ListItem, Label
from textual.events import Key

from navigation import get_directory_contents, navigate_up, navigate_down

class FileManagerApp(App):
    def __init__(self, path="."):
        super().__init__()
        self.path = path

    def compose(self):
        yield Label(f"Current Directory: {self.path}", id="header")
        yield ListView(id="file-list")

    def on_mount(self):
        self.update_file_list()

    def update_file_list(self):
        file_list = self.query_one("#file-list", ListView)
        file_list.clear()

        contents = get_directory_contents(self.path)
        for filename in contents:
            file_list.append(ListItem(Label(filename)))

    def on_key(self, event: Key):
        if event.key == "enter":
            self.navigate_down()
        elif event.key == "b":
            self.navigate_up()

    def navigate_down(self):
        file_list = self.query_one("#file-list", ListView)
        selected_item = file_list.highlighted_child

        if selected_item:
            selected_label = selected_item.query_one(Label)
            self.path = navigate_down(self.path, str(selected_label.renderable))
            self.update_file_list()
            self.query_one("#header", Label).update(f"Current Directory: {self.path}")

    def navigate_up(self):
        self.path = navigate_up(self.path)
        self.update_file_list()
        self.query_one("#header", Label).update(f"Current Directory: {self.path}")

if __name__ == "__main__":
    FileManagerApp().run()

