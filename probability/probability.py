import scipy.stats as st
from datetime import datetime


def str_time_to_seconds(tstr: str) -> int:
    """Convert 'HH:MM' time string to seconds since midnight."""
    dt = datetime.strptime(tstr, "%H:%M")
    return dt.hour * 3600 + dt.minute * 60


def seconds_to_str_time(seconds: int) -> str:
    """Convert seconds since midnight to a 'HH:MM' string."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{int(hours):02}:{int(minutes):02}"


def lateness_probability_seconds(
    leave_home_sec: int,
    meeting_time_sec: int = 9 * 3600 + 5 * 60,  # 09:05 = 32700 seconds
    walk_to_bus_sec: int = 300,
    bus_ride_sec: int = 780,
    walk_from_bus_sec: int = 240,
    sigma_sec: float = 60.0,
    last_bus_departure_sec: int = 8 * 3600 + 48 * 60  # 08:48 = 31680 seconds
) -> float:
    """
    Calculate probability of being late using seconds.

    Args:
        leave_home_sec: time leaving home in seconds since midnight
        meeting_time_sec: meeting time in seconds
        walk_to_bus_sec: walking time to bus stop
        bus_ride_sec: average bus ride time
        walk_from_bus_sec: walking time from bus stop to office
        sigma_sec: std dev of total trip time in seconds
        last_bus_departure_sec: last acceptable bus departure time in seconds

    Returns:
        Probability of being late (float between 0 and 1)
    """
    arrival_at_bus_stop_sec = leave_home_sec + walk_to_bus_sec
    if arrival_at_bus_stop_sec > last_bus_departure_sec:
        return 1.0

    total_mean_trip_sec = walk_to_bus_sec + bus_ride_sec + walk_from_bus_sec
    available_time_sec = meeting_time_sec - leave_home_sec

    z = (available_time_sec - total_mean_trip_sec) / sigma_sec
    prob_on_time = st.norm.cdf(z)
    return 1 - prob_on_time


def generate_lateness_probabilities_seconds(
    start_sec: int,
    end_sec: int,
    step_sec: int = 60,
    meeting_time_sec: int = 9 * 3600 + 5 * 60,
    walk_to_bus_sec: int = 300,
    bus_ride_sec: int = 780,
    walk_from_bus_sec: int = 240,
    sigma_sec: float = 60.0,
    last_bus_departure_sec: int = 8 * 3600 + 48 * 60
) -> list[tuple[int, float]]:
    """
    Generate lateness probabilities for a range of departure times (in seconds).

    Args:
        start_sec: starting second (since midnight)
        end_sec: ending second
        step_sec: step size in seconds (default: 60)
        [other commute parameters]

    Returns:
        List of (leave_home_sec, prob_late) tuples
    """
    results = []
    for t in range(start_sec, end_sec + 1, step_sec):
        prob = lateness_probability_seconds(
            leave_home_sec=t,
            meeting_time_sec=meeting_time_sec,
            walk_to_bus_sec=walk_to_bus_sec,
            bus_ride_sec=bus_ride_sec,
            walk_from_bus_sec=walk_from_bus_sec,
            sigma_sec=sigma_sec,
            last_bus_departure_sec=last_bus_departure_sec
        )
        results.append((t, prob))
    return results


# Example
if __name__ == "__main__":
    start = str_time_to_seconds("07:30")
    end = str_time_to_seconds("09:00")

    values = generate_lateness_probabilities_seconds(start_sec=start, end_sec=end, step_sec=600)

    for leave_sec, prob in values:
        print(f"Leave at {seconds_to_str_time(leave_sec)} -> Probability late: {prob}")
