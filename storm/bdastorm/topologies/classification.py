# -*- coding: utf-8 -*-
"""
Example race topology
"""

from streamparse import Grouping, Topology

from bolts.classification import classificationBolt, ExitBolt
from spouts.classification import classificationSpout


class TopologyAlertAtmo(Topology):
    spout = classificationSpout.spec()
    bolt = classificationBolt.spec(inputs=[spout])
    exit_bolt = ExitBolt.spec(inputs=[bolt])

