"""Implements a pane in the window to choose hash function."""

__all__ = ['HashChoicePane']

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from hashing import DEFAULT_HASH_ALGORITHM, SUPPORTED_ALGORITHMS, hasher


class HashChoicePane(BoxLayout):
    """The pane that allows one to chose a hash algorithm."""
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(
            text = 'Hash algorithm',
            size_hint_y = None,
            height = 30
        ))

        scroll_view: ScrollView = ScrollView(
            do_scroll_x = False
        )
        scroll_boxlayout: BoxLayout = BoxLayout(
            orientation = 'vertical'
        )

        self.hash_choice_options: dict[str, CheckBox] = {}
        for key in SUPPORTED_ALGORITHMS:
            box_layout: BoxLayout = BoxLayout(orientation = 'horizontal')
            box_layout.add_widget(
                Label(text = SUPPORTED_ALGORITHMS[key])
            )
            new_checkbox: CheckBox = CheckBox(
                group = 'hash_algorithm',
                active = key == DEFAULT_HASH_ALGORITHM,
                size_hint_x = None,
                width = 30
            )
            new_checkbox.bind(active = (
                lambda instance, value, algorithm = key:
                    self.change_hash_algorithm(algorithm)
                ))
            box_layout.add_widget(new_checkbox)
            scroll_boxlayout.add_widget(box_layout)
        scroll_view.add_widget(scroll_boxlayout)
        self.add_widget(scroll_view)

    def change_hash_algorithm(self, algorithm: str) -> None:
        hasher.hash_algorithm = algorithm
