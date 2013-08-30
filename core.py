# -*- coding: utf-8 -*- 

from random import shuffle
import random





days = {
    'mandag':   1,
    'tirsdag':  2,
    'onsdag':   3,
    'torsdag':  4,
    'fredag':   5,
    'lørdag':   6,
    'søndag':   7
}





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

    def single( self, name ):
        candidate = self.persons.get( name )
        if not candidate:
            self.persons[name] = Person(name)
            candidate = self.persons.get( name )

        return candidate.name

    def multiple( self, *args ):
        candidates = []
        for n in args:
            if self.single( n ):
                candidates.append( n )

        return ", ".join( candidates )


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

        for d in dates:
            if len( events_sample ):
                mapping[d] = events_sample.pop()
            else:
                break

        return mapping

    def iterator(self, terminate_after ):
        return self.EventIterator( self, terminate_after )

    class EventIterator:
        def __init__(self, events, terminate_after):
            self.events = [e for e in events if e.confirmed]

            total_quantity = 0
            for e in self.events:
                total_quantity += e.quantity



            print "Number of unique events", len( self.events )
            print "Total quantity", total_quantity

            shuffle( self.events )


            self.iteration_counter = 0
            self.terminate_after = terminate_after

        def next( self ):

            if self.iteration_counter > self.terminate_after:
                return None

            current_index = ( self.iteration_counter % len( self.events ) )

            if current_index == 0:
                self.expand()
                print "wraparound"

            self.iteration_counter += 1

            return self.events[current_index]


        def expand(self):
            candidates = []
            for e in self.events:
                for i in range(e.quantity):
                    current_event = e
                    current_event.quantity = 1
                    candidates.append( current_event )


            self.events = candidates
            shuffle( self.events )
