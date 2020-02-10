# -*- coding: utf-8 -*-
"""
Example race topology
"""

from streamparse import Grouping, Topology

from bolts.alert_atmo import AlertBolt, ExitBolt
from spouts.alert_atmo import AlertAtmoSpout


class TopologyAlertAtmo(Topology):
    spout = AlertAtmoSpout.spec()
    alertBolt = AlertBolt.spec(inputs=[spout])
    exit_bolt = ExitBolt.spec(inputs=[alertBolt])

