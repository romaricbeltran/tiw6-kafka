# -*- coding: utf-8 -*-
"""
Example race topology
"""

from streamparse import Grouping, Topology

from bolts.classification import ClassificationBolt, SaveFileClassificationBolt
from spouts.preproc_atmo import PreProcAtmoSpout
from spouts.preproc_meteofrance import PreProcMeteoFranceSpout
from spouts.preproc_traffic import PreProcTrafficSpout
from bolts.preproc_atmo import PreProcAtmoBolt, SaveFileAtmoBolt
from bolts.preproc_meteofrance import PreProcMeteoBolt, SaveFileMeteoBolt
from bolts.preproc_traffic import PreProcTrafficBolt, SaveFileTrafficBolt

class TopologyClassification(Topology):
    #atmo_spout = PreProcAtmoSpout.spec()
    meteo_spout = PreProcMeteoFranceSpout.spec()
    #traffic_spout = PreProcTrafficSpout.spec()
    
    #atmo_bolt = PreProcAtmoBolt.spec(inputs=[atmo_spout])
    meteo_bolt = PreProcMeteoBolt.spec(inputs=[meteo_spout])
    #traffic_bolt = PreProcTrafficBolt.spec(inputs=[traffic_spout])
    
    #save_atmo_bolt = SaveFileAtmoBolt.spec(inputs=[atmo_bolt])
    save_meteo_bolt = SaveFileMeteoBolt.spec(inputs=[meteo_bolt])
    #save_traffic_bolt = SaveFileTrafficBolt.spec(inputs=[traffic_bolt])
    
    #class_bolt = ClassificationBolt.spec(inputs=[atmo_bolt, meteo_bolt, traffic_bolt])
    #save_class_bolt = SaveFileClassificationBolt.spec(inputs=[class_bolt])

