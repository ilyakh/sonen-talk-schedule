# -*- coding: utf-8 -*-
import calendar
import datetime
import itertools

from core import *
from plan import *


if __name__ == "__main__":

    start_date =  datetime.date( 2013,  9, 15 )
    end_date   =  datetime.date( 2013, 11, 25 )

    valid_days = [ days['torsdag'], days['onsdag'] ]

    # calendar instance
    c = calendar.Calendar()

    # combine the months into a single period
    period = itertools.chain(
        c.itermonthdates( 2013, 9 ),
        c.itermonthdates( 2013, 10 ),
        c.itermonthdates( 2013, 11 ),
        c.itermonthdates( 2013, 12 )
    )

    dates = []



    for i in sorted(set(period)):
        if i.isoweekday() in valid_days:
            # limit by start and end dates
            if start_date <= i < end_date:
                dates.append( i )


    cl = events.iterator( 100 )


    mapping = {}
    for n,d in enumerate(dates):
        current_event = cl.next()
        mapping[d] = current_event


    current_time = datetime.datetime.now().time()
    output_name = "{0}.txt".format( current_time )
    with open( output_name, 'w' ) as output:
        for k,v in mapping.items():
            output.write(
                "{date}\t{subject}\t{persons}\n".format(
                    date=k,
                    subject=v.subject,
                    persons=v.persons
                )
            )



