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
