def generate_schedule(subjects, days_left, hours_per_day):
    total_hours = sum(subject.hours for subject in subjects)
    schedule = []

    for subject in subjects:
        daily_hours = (subject.hours / total_hours) * (days_left * hours_per_day)
        schedule.append({
            "subject": subject.subject,
            "hours_per_day": round(daily_hours / days_left, 2)
        })

    return schedule
