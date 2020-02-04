package tiw.tiw6.storm.topology;

import org.apache.storm.Config;
import org.apache.storm.StormSubmitter;
import org.apache.storm.generated.AlreadyAliveException;
import org.apache.storm.generated.AuthorizationException;
import org.apache.storm.generated.InvalidTopologyException;
import org.apache.storm.topology.TopologyBuilder;
import tiw.tiw6.storm.operator.ExitBolt;
import tiw.tiw6.storm.operator.GeneratorSpout;
import tiw.tiw6.storm.operator.NothingBolt;
import tiw.tiw6.storm.operator.TortoiseGeneratorSpout;

public class TopologyT1 {

    public static void main(String [] args) throws InvalidTopologyException, AuthorizationException, AlreadyAliveException {
        int monitorPort = 8080;
        String monitorHost = "localhost";
        int nbExecutors = 1;

        /*Création du spout*/
        GeneratorSpout spout = new GeneratorSpout();
        /*Création de la topologie*/
        TopologyBuilder builder = new TopologyBuilder();
        /*Affectation à la topologie du spout*/
        builder.setSpout("masterStream", spout);
        /*Affectation à la topologie du bolt qui ne fait rien, il prendra en input le spout localStream*/
        builder.setBolt("nofilter", new NothingBolt(), nbExecutors).shuffleGrouping("masterStream");
        /*Affectation à la topologie du bolt qui émet le flux de sortie, il prendra en input le bolt nofilter*/
        builder.setBolt("exit", new ExitBolt(monitorHost, monitorPort), nbExecutors).shuffleGrouping("nofilter");

        /*Création d'une configuration*/
        Config config = new Config();
        /*La topologie est soumise à STORM*/
        StormSubmitter.submitTopology("topoT1", config, builder.createTopology());

    }

}
