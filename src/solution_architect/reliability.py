def downtime_budget(availability_percent,minutes_in_month=43200):
    if not 0<=availability_percent<=100: raise ValueError('Availability must be 0..100')
    return round(minutes_in_month*(1-availability_percent/100),2)
def combined_serial_availability(*vals):
    result=1.0
    for v in vals:
        if not 0<=v<=1: raise ValueError('Availability values must be fractions')
        result*=v
    return round(result,6)
