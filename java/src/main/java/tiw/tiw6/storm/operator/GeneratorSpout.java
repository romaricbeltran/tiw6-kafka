package tiw.tiw6.storm.operator;

import org.apache.storm.spout.SpoutOutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.IRichSpout;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import tiw.tiw6.storm.race.Race;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.Map;

public class GeneratorSpout implements IRichSpout {

    private static final long DELAY = 100000L;
    private static final Logger LOG = LoggerFactory.getLogger(GeneratorSpout.class);

    private transient SpoutOutputCollector collector;
    private long messageId = 0L;

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
        declarer.declare(new Fields("json"));
    }

    @Override
    public void nextTuple() {
        try {
            URL oracle = new URL("http://api.atmo-aura.fr/communes/69003/indices?api_token=ac33ef51d0007489b798fc09244ccb73");
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(oracle.openStream()));

            StringBuilder file = new StringBuilder();
            String inputLine;
            while ((inputLine = in.readLine()) != null)
                file.append(inputLine);
            in.close();

            collector.emit(new Values(file.toString()), messageId++);
            Thread.sleep(DELAY);
        } catch (InterruptedException | IOException e) {
            LOG.error("Error when generating next tortoise top", e);
            Thread.currentThread().interrupt();
        }
    }

    @Override
    public void open(Map map, TopologyContext topologyContext, SpoutOutputCollector spoutOutputCollector) {
        this.collector = spoutOutputCollector;
    }

    @Override
    public void close() {
        // Nothing to close
    }

    @Override
    public void activate() {
        // Nothing changes on activation
    }

    @Override
    public void deactivate() {
        // Nothing to change on deactivation
    }

    @Override
    public void ack(Object o) {
        // Nothing to do on message acknowledgment
    }

    @Override
    public void fail(Object o) {
        // Nothing to do if some message failed
    }

    @Override
    public Map<String, Object> getComponentConfiguration() {
        return null;
    }
}
