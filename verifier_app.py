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
        self.title = 'Simple File Verifier'

        self.hash_choice_pane: HashChoicePane = HashChoicePane(
            size_hint_x = None,
            width = LEFT_SIDE_WIDTH
        )
        self.window.add_widget(self.hash_choice_pane)

        self.file_choice_pane: FileChoicePane = FileChoicePane()
        self.window.add_widget(self.file_choice_pane)

        self.calculate_button: Button = Button(
            text = 'COMPUTE HASH',
            size_hint = (None, None),
            size = (LEFT_SIDE_WIDTH, BOTTOM_SIDE_HEIGHT)
        )
        self.calculate_button.bind(on_release = (
            lambda instance:
                self.update_digest_label()
        ))
        self.window.add_widget(self.calculate_button)

        self.hash_sum_output: TextInput = TextInput(
            text = 'The computed hash sum will appear here.',
            size_hint_y = None,
            height = BOTTOM_SIDE_HEIGHT
        )
        self.window.add_widget(self.hash_sum_output)

        return self.window


    def update_digest_label(self) -> None:
        """Updates the hash digest label.

        Args:
            self: The instance of the class.

        Returns:
            None
        """
        try:
            digest: tuple[str, int] = hasher.compute_digest()
            text: str = digest[0] if digest[1] == 0 else {
                1: 'Error: File not found',
                2: 'Error: Permission denied',
                3: 'Please select a file'
            }.get(digest[1])
            self.hash_sum_output.text = text
        except Exception:
            self.hash_sum_output.text = 'An error occurred'
