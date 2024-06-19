"""Implements a pane that allows the user to choose a file to verify."""

__all__ = ['FileChoicePane']

from os.path import dirname, isfile

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from hashing import hasher


class FileChoicePane(BoxLayout):
    """The pane that allows one to choode a file to hash."""
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(
            text = 'Select file',
            size_hint_y = None,
            height = 30
        ))

        self.file_chooser: FileChooserIconView = FileChooserIconView()
        self.file_chooser.bind(on_submit = (
            lambda instance, selection, touch:
                self.change_file_input(selection[0])
        ))
        self.add_widget(self.file_chooser)

        self.selected_file_input: TextInput = TextInput(
            multiline=False,
            size_hint_y = None,
            height = 40
        )
        self.selected_file_input.bind(on_text_validate=(
            lambda instance:
                self.change_file(self.selected_file_input.text)
        ))
        self.add_widget(self.selected_file_input)

        self.select_button: Button = Button(
            text='Select',
            size_hint_y = None,
            height = 40
        )
        self.select_button.bind(on_release = (
            lambda instance:
                self.change_file(self.selected_file_input.text)
        ))
        self.add_widget(self.select_button)

    def change_file_input(self, selection: str) -> None:
        self.selected_file_input.text = selection
        self.change_file(selection)

    def change_file(self, file: str) -> None:
        hasher.file_path = file
        if isfile(file):
            directory: str = dirname(file)
            self.file_chooser.path = directory
            self.file_chooser.selection = [file]
