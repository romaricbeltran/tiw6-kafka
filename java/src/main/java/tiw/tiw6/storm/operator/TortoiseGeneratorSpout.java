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

import java.util.Map;

public class TortoiseGeneratorSpout implements IRichSpout {

    private static final long DELAY = 1000L;
    private static final Logger LOG = LoggerFactory.getLogger(TortoiseGeneratorSpout.class);

    private Race race;
    private transient SpoutOutputCollector collector;
    private long messageId = 0L;

    public TortoiseGeneratorSpout(int nbConcurrents) {
        this.race = new Race(nbConcurrents);
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
        declarer.declare(new Fields("json"));
    }

    @Override
    public void nextTuple() {
        try {
            String msg = race.nextJSONString();
            collector.emit(new Values(msg), messageId++);
            Thread.sleep(DELAY);
        } catch (InterruptedException e) {
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
