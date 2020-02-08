# -*- coding: utf-8 -*-
import logging
import json
import time
from random import randint
from streamparse.spout import Spout


class Tortoise:
    """Une tortue est représentée en JSON comme suit:
       {"id":0,"top":523,"position":4,"nbDevant":8,"nbDerriere":1,"total":10}
    """

    def __init__(self, id, top, position, nbDevant, nbDerriere, total):
        self.id = id
        self.top = top
        self.position = position
        self.nbDevant = nbDevant
        self.nbDerriere = nbDerriere
        self.total = total

    def as_dict(self):
        return dict(
            id=self.id,
            top=self.top,
            position=self.position,
            nbDevant=self.nbDevant,
            nbDerriere=self.nbDerriere,
            total=self.total,
        )


TRACK_SIZE = 255
MAX_FORWARD = 10


class Runner:
    """Représente les informations sur un concurrent dans une course."""

    def __init__(self, id):
        self.id = id
        self.absPosition = 0

    def getPosition(self):
        return self.absPosition % TRACK_SIZE

    def step(self):
        self.absPosition = self.absPosition + randint(1, MAX_FORWARD)


class Race:
    """Represente une course.

    Permet en particulier de simuler le déroulement de la course.
    """

    def __init__(self, nbRunners):
        self.runners = [Runner(i) for i in range(0, nbRunners)]
        self.top = 0

    def _step(self):
        for r in self.runners:
            r.step()
        self.top = self.top + 1

    def _tortoise(self, r):
        before = len(list(filter(lambda r2: r2.absPosition > r.absPosition, self.runners)))
        after = len(list(filter(lambda r2: r2.absPosition < r.absPosition, self.runners)))
        return Tortoise(
            r.id, self.top, r.getPosition(), before, after, len(self.runners)
        )

    def next(self):
        self._step()
        return dict(tortoises=[self._tortoise(r).as_dict() for r in self.runners])

    def __iter__(self):
        return self


DELAY = 1000
NB_CONCURRENTS = 10


class TortoiseGeneratorSpout(Spout):
    outputs = ["json"]

    def initialize(self, stormconf, context):
        self.race = Race(NB_CONCURRENTS)

    def next_tuple(self):
        data = self.race.next()
        out = json.dumps(data)
        self.emit([out])
        time.sleep(1)  # 1 s

    def ack(self, tup_id):
        pass  # if a tuple is processed properly, do nothing

    def fail(self, tup_id):
        pass  # if a tuple fails to process, do nothing
