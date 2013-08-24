# -*- coding: utf-8 -*-

import calendar
import datetime
from itertools import chain

import random

def choice( collection ):
    return random.choice( collection )

def sample( collection, k ):
    # select only the confirmed events
    collection = [e for e in collection if e.confirmed]

    k = k if k <= len( collection ) else len( collection )

    return random.sample( collection, k )

def unconfirmed( event ):
    event.confirmed = False
    return event

class Person:
    def __init__( self, name ):
        self.name = name

class Persons:
    def __init__( self ):
        self.persons = {}

    def __getitem__( self, name ):
        candidate = self.persons.get( name )
        if not candidate:
            self.persons[name] = Person(name)
            candidate = self.persons.get( name )

        return candidate


class Event:
    def __init__( self, *args, **kwargs ):
        self.subject = kwargs.get('subject')
        self.persons = kwargs.get('person')
        self.quantity = kwargs.get('quantity')
        self.confirmed = True
        self.priority = 1

        if kwargs.get('confirmed'):
            self.confirmed = kwargs.get('confirmed')

        if kwargs.get('priority'):
            self.priority = kwargs.get('priority')


class Verksted(Event):
    pass

class Foredrag(Event):
    pass


class Events:
    def __init__(self):
        self.events = set()

    def add(self, *events):
        self.events.update( events )

    def __len__( self ):
        return len( self.events )

    def __iter__( self ):
        return self.events.__iter__()

    def __list__( self ):
        return list( self.events )

    def distribute( self, dates ):
        mapping = {}
        sample_size = min( len( self.events ), len( dates ) )
        events_sample = sample( self.events, sample_size )

        print sample_size

        for d in dates:
            if len( events_sample ):
                mapping[d] = events_sample.pop()
            else:
                break

        return mapping


if __name__ == "__main__":

    persons = Persons()
    events = Events()

    events.add(

        Verksted(
            subject="Vektorgrafikk i Illustrator",
            person=persons['Veronika Heimsbakk'],
            quantity=2
        ),

        Verksted(
            subject="Spillutvikling i Lua",
            person=persons['Srod Karim'],
            quantity=3
        ),

        Foredrag(
            subject="Smarte klær",
            person=persons['Kristin Sunde'],
            quantity=1
        ),

        Foredrag(
            subject="Produksjon av smarte klær",
            person=persons['Kristin Sunde'],
            quantity=1
        ),

        Foredrag(
            subject="Python, a partner in crime",
            person=persons['Ilya Kostolomov'],
            quantity=1
        ),

        Verksted(
            subject="Unix basics på Raspberry Pi",
            person=persons['Jonathan Ringstad'],
            quantity=2
        ),

        Verksted(
            subject="DOM, CSS og jquery",
            person=persons['Ilya Kostolomov'],
            quantity=3
        ),

        Verksted(
            subject="3D-printere og parametrisk design",
            person=persons['Ilya Kostolomov', 'Fredrik Hov'],
            quantity=2
        ),

        unconfirmed( Verksted(
            subject="Java med Processing",
            person=persons['Emil Hatleid', 'Persijn Kwekkebom'],
            quantity=3,
        )),

        unconfirmed( Foredrag(
            subject="Redd verden",
            person=persons['Kine Gjerstad Eide'],
            quantity=1,
        )),

        unconfirmed( Verksted(
            subject="C++",
            person=persons['David'],
            quantity=1,
        )),

        unconfirmed( Verksted(
            subject="Android",
            person=persons['Kyrre Havik Eriksen'],
            quantity=3,
        )),

        unconfirmed( Verksted(
            subject="Arduino for vitenskapelige anvendelser",
            person=persons['Ilya Kostolomov', 'Peter Havgar', 'Roger Antonsen', 'Andreas Nakkerud'],
            quantity=3,
        ))

    )

    # calendar instance
    c = calendar.Calendar()

    # combine the months into a single period
    period = chain(
        c.itermonthdates( 2013, 9 ),
        c.itermonthdates( 2013, 10 ),
        c.itermonthdates( 2013, 11 ),
        c.itermonthdates( 2013, 12 )
    )

    #

    start_date = datetime.date( 2013, 9, 1 )
    end_date = datetime.date( 2013, 12, 19 )

    days = {
        'mandag':   1,
        'tirsdag':  2,
        'onsdag':   3,
        'torsdag':  4,
        'fredag':   5,
        'lørdag':   6,
        'søndag':   7
    }


    #

    thursdays = []

    for i in sorted(set(period)):
        if i.isoweekday() == days['torsdag']:
            # limit by start and end dates
            if start_date <= i < end_date:
                thursdays.append( i )


    # assign dates to different suggestions
    # expand and flatten suggestions

    event_plan = sorted( events.distribute( thursdays ).iteritems(), key=lambda d: d[0] )

    for d,e in event_plan:
        print d,e.subject



