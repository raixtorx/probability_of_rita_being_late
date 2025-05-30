import matplotlib.pyplot as plt
from ..utils.time_utils import *

def plot_lateness_probabilities(
        values: list[tuple[int, float]], 
        title=""):
    """
    Plot Rita's probability of being late over leave home times.

    Args:
        values: List of tuples (leave_time_in_seconds, probability_of_lateness)
        title: Plot title (optional)
    """
    # Unpack times and probabilities
    leave_times_sec, probabilities = zip(*values)

    x_labels = [seconds_to_str_time(t) for t in leave_times_sec]

    plt.figure(figsize=(10, 5))
    plt.plot(leave_times_sec, probabilities, color="orange", label="Probability of Being Late")

    plt.xlabel("time leaving home")
    plt.ylabel("P(late to meeting)")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.2)

    step = max(len(x_labels) // 10, 1)
    plt.xticks(leave_times_sec[::step], x_labels[::step])

    plt.legend()
    plt.show()

# Example
if __name__ == "__main__":
    start = str_time_to_seconds("08:00")
    end = str_time_to_seconds("09:00")
    values = [(100, 0.532), (200, 0.137), (300, 0.874), (400, 0.456), (500, 0.293)]

    plot_lateness_probabilities(values)
