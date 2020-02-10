# -*- coding: utf-8 -*-
"""
Example race topology
"""

from streamparse import Grouping, Topology

from bolts.preproc_atmo import PreProcBolt, ExitBolt
from spouts.preproc_atmo import PreProcAtmoSpout


class TopologyPreProcAtmo(Topology):
    spout = PreProcAtmoSpout.spec()
    preProcBolt = PreProcBolt.spec(inputs=[spout])
    exit_bolt = ExitBolt.spec(inputs=[preProcBolt])

