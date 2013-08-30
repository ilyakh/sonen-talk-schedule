# -*- coding: utf-8 -*- 

from core import *

p = Persons()
person = p.single
persons = p.multiple
events = Events()

events.add(

    unconfirmed( Verksted(
        subject="C++",
        person=persons('Anders Mathiassen', 'Martin Vilhelmsen'),
        quantity=1,
    )),

    unconfirmed( Verksted(
        subject="Android",
        person=person('Kyrre Havik Eriksen'),
        quantity=3,
    )),

    unconfirmed( Verksted(
        subject="Arduino for vitenskapelige anvendelser",
        person=persons('Ilya Kostolomov', 'Peter Havgar', '~Roger Antonsen', '~Andreas Nakkerud'),
        quantity=3,
    )),

    unconfirmed( Foredrag(
        subject="Smarte klær",
        person=person('Kristin Sunde'),
        quantity=1
    )),

    unconfirmed( Foredrag(
        subject="Python, a partner in crime",
        person=person('Ilya Kostolomov'),
        quantity=1
    )),

    unconfirmed( Foredrag(
        subject="Omvisning i sonen",
        person=None,
        quantity=1
    )),

    Verksted(
        subject="Unix basics på Raspberry Pi",
        person=person('Jonathan Ringstad'),
        quantity=2
    ),

    Verksted(
        subject="DOM, CSS og jquery",
        person=person('Ilya Kostolomov'),
        quantity=3
    ),

    Verksted(
        subject="3D-printere og parametrisk design",
        person=persons('Ilya Kostolomov', 'Fredrik Hov'),
        quantity=2
    ),

    Verksted(
        subject="Java med Processing",
        person=persons('Emil Hatleid', 'Persijn Kwekkebom'),
        quantity=3,
    ),

    Foredrag(
        subject="Redd verden",
        person=persons('Kine Gjerstad Eide', 'Peter Havgar'),
        quantity=1,
    ),

    Verksted(
        subject="Vektorgrafikk i Illustrator",
        person=person('Veronika Heimsbakk'),
        quantity=2
    ),

    Verksted(
        subject="Spillutvikling i Lua",
        person=person('Srod Karim'),
        quantity=3
    )

)
