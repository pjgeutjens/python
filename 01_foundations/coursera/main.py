import arrow

date = arrow.get('2023-06-25', 'YYYY-MM-DD')
date.shift(weeks=+6).format('YYYY-MM-DD')