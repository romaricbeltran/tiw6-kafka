# -*- coding: utf-8 -*-
"""
Example race topology
"""

from streamparse import Grouping, Topology

from bolts.preproc_meteofrance import PreProcBolt, ExitBolt
from spouts.preproc_meteofrance import PreProcMeteoFranceSpout


class TopologyPreProcMeteoFrance(Topology):
    spout = PreProcMeteoFranceSpout.spec()
    preProcBolt = PreProcBolt.spec(inputs=[spout])
    exit_bolt = ExitBolt.spec(inputs=[preProcBolt])

