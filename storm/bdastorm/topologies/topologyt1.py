# -*- coding: utf-8 -*-
"""
Example race topology
"""

from streamparse import Grouping, Topology

from bolts.race import NothingBold, ExitBolt
from spouts.tortoises import TortoiseGeneratorSpout


class TopologyT1(Topology):
    tortoise_spout = TortoiseGeneratorSpout.spec()
    nothing_bolt = NothingBold.spec(inputs=[tortoise_spout])
    exit_bolt = ExitBolt.spec(inputs=[nothing_bolt])

