import sys

from matplotlib import rcParams
from translate import Translator
import matplotlib.pyplot as plt

translator = Translator(to_lang="pt-BR")

rcParams.update({
    # Set the plot left margin so that the labels are visible.
    'figure.subplot.left': 0.3,

    # Hide the bottom toolbar.
    'toolbar': 'None'
})


class Plotter(object):
    """An util class to display the classification results."""

    _PAUSE_TIME = 0.05
    """Time for matplotlib to wait for UI event."""

    def __init__(self) -> None:
        fig, self._axes = plt.subplots()
        fig.canvas.manager.set_window_title('Classificação de Audio')

        # Stop the program when the ESC key is pressed.
        def event_callback(event):
            if event.key == 'escape':
                sys.exit(0)

        fig.canvas.mpl_connect('key_press_event', event_callback)

        plt.show(block=False)

    # TODO(khanhlvg): Add type hint for result once ClassificationResult added
    # to tflite_support.task.processor module
    def plot(self, result) -> None:
        def translateText(text_label):
            return translator.translate(text_label)
        def printScore(label_list_array, score_list_array):
            lengthArray = len(label_list_array)
            for i in range(lengthArray):
                print("A categoria:", label_list_array[i], " Está com Score:", score_list_array[i])

        """Plot the audio classification result.

        Args:
            result: Classification results returned by an audio classification
            model.
        """
        # Clear the axes
        self._axes.cla()
        self._axes.set_title('O Audio é:')
        self._axes.set_xlim((0, 1))

        # Plot the results so that the most probable category comes at the top.
        classification = result.classifications[0]
        label_list = [ translateText(category.category_name) for category in classification.categories ]
        score_list = [ category.score for category in classification.categories ]
        printScore(label_list[::-1], score_list[::-1])
        self._axes.barh(label_list[::-1], score_list[::-1])

        # Wait for the UI event.
        plt.pause(self._PAUSE_TIME)
