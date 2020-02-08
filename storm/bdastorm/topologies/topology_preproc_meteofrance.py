# -*- coding: utf-8 -*-
"""
Example race topology
"""

from streamparse import Grouping, Topology

from bolts.preprocmeteo import NothingBold, ExitBolt
from spouts.preproc_meteofrance import PreProcMeteoFranceSpout


class TopologyPreProcMeteoFrance(Topology):
    spout = PreProcMeteoFranceSpout.spec()
    nothing_bolt = NothingBold.spec(inputs=[spout])
    exit_bolt = ExitBolt.spec(inputs=[nothing_bolt])

