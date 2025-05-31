# RMK Data Team Internship – Challenge 2025  
**"Probability of Rita Being Late"**

This repository contains a solution to the **RMK Tallinn office data internship challenge**, where we estimate and visualize the **probability of Rita being late to her daily 9:05 meeting**—depending on what time she leaves home.

---

## Problem Summary

Rita commutes by **Tallinn city bus #8** from **Zoo** to **Toompark**.  
She must arrive **on time (before 9:05)** at the RMK office every weekday.  
Rita's journey to the office includes:

- **300 seconds** walking from home to the Zoo bus stop
- **Bus ride** from Zoo to Toompark (average time = 780 seconds)
- **240 seconds** walking from Toompark to the meeting room

---

## Repository Structure

```bash
probability_of_rita_being_late/
├── main.py                       # Main code
├── probability/
│   └── probability.py            # Probability calculation
├── plotting/
│   └── plot.py                   # Visualization using matplotlib
├── utils/
│   └── time_utils.py             # time -> string and string -> time conversion
└── README.md
```

---

## Future Improvements

- Integrate live or scheduled bus data: Scrape or use an API to use actual bus departure and arrival times.
- Explore alternative probability distributions and implement those on graph.
