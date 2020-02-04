package tiw.tiw6.storm.operator;

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.IRichBolt;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.slf4j.LoggerFactory;
import tiw.tiw6.storm.NetworkWriter;

import java.util.Map;

public class ExitBolt implements IRichBolt {

    private String host = null;
    private int port = -1;
    private NetworkWriter writer = null;
    private OutputCollector collector;

    public ExitBolt(String host, int port) {
        this.host = host;
        this.port = port;
    }

    public ExitBolt() {
    }


    @Override
    public void prepare(Map stormConf, TopologyContext context, OutputCollector collector) {
        this.collector = collector;
        if (port != -1 && host != null) {
            this.writer = new NetworkWriter(host, port);
        } else {
            LoggerFactory.getLogger(ExitBolt.class).warn("Host or port not known, using defaults");
            this.writer = new NetworkWriter();
        }
    }

    @Override
    public void execute(Tuple input) {
        String n = input.getValueByField("json").toString();
        this.writer.write(n);
        collector.ack(input);
        return;
    }

    @Override
    public void cleanup() {
        writer.close();
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
        declarer.declare(new Fields("json"));
    }

    @Override
    public Map<String, Object> getComponentConfiguration() {
        return null;
    }
}
