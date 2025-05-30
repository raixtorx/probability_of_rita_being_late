from probability_of_rita_being_late.probability.probability import generate_lateness_probabilities_seconds
from probability_of_rita_being_late.plotting.plot import plot_lateness_probabilities
from probability_of_rita_being_late.utils.time_utils import str_time_to_seconds

def main():
    start_time = "08:00"
    end_time = "09:00"
    start_sec = str_time_to_seconds(start_time)
    end_sec = str_time_to_seconds(end_time)
    
    # Generate lateness probabilities every 30 seconds.
    values = generate_lateness_probabilities_seconds(start_sec=start_sec, end_sec=end_sec, step_sec=30)
    
    # Plot the probabilities
    plot_lateness_probabilities(values, "Probability of Being Late", "time leaving home", "P(late to meeting)")

if __name__ == "__main__":
    main()