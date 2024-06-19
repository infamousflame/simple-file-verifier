"""Provides the `VerifierApp` class."""

__all__ = ['VerifierApp']

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from file_choice_pane import FileChoicePane
from hash_choice_pane import HashChoicePane
from hashing import hasher

LEFT_SIDE_WIDTH = 150
BOTTOM_SIDE_HEIGHT = 150


class VerifierApp(App):
    """The actual all class."""

    def build(self) -> GridLayout:
        """Build the app.

        Returns:
            GridLayout: The window's layout.
        """
        self.window: GridLayout = GridLayout(rows = 2, cols = 2)
        self.title = 'File Verifier'

        self.hash_choice_pane: HashChoicePane = HashChoicePane(
            size_hint_x = None,
            width = LEFT_SIDE_WIDTH
        )
        self.window.add_widget(self.hash_choice_pane)

        self.file_choice_pane: FileChoicePane = FileChoicePane()
        self.window.add_widget(self.file_choice_pane)

        self.calculate_button: Button = Button(
            text = 'COMPUTE SUM',
            size_hint = (None, None),
            size = (LEFT_SIDE_WIDTH, BOTTOM_SIDE_HEIGHT)
        )
        self.calculate_button.bind(on_release = (
            lambda instance:
                self.update_digest_label()
        ))
        self.window.add_widget(self.calculate_button)

        self.hash_sum_output: TextInput = TextInput(
            text = 'Computed hash sum',
            size_hint_y = None,
            height = BOTTOM_SIDE_HEIGHT
        )
        self.window.add_widget(self.hash_sum_output)

        return self.window


    def update_digest_label(self) -> None:
        """Updates the hash digest label."""
        digest: tuple[str, int] = hasher.compute_digest()
        match digest[1]:
            case 0:
                self.hash_sum_output.text = hasher.compute_digest()[0]
            case 1:
                self.hash_sum_output.text = 'File not found'
            case 2:
                self.hash_sum_output.text = 'Permission denied'
            case 3:
                self.hash_sum_output.text = 'Please select a file'
