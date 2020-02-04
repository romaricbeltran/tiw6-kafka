package tiw.tiw6.storm.operator.example;

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.IRichBolt;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;

import java.util.Map;


/**
 * Sample of stateless operator
 *
 * @author lumineau
 */
public class ExampleStatelessBolt implements IRichBolt {

    private static final long serialVersionUID = 4262369370788107343L;
    private transient OutputCollector collector;


    /* (non-Javadoc)
     * @see backtype.storm.topology.IRichBolt#execute(backtype.storm.tuple.Tuple)
     */
    public void execute(Tuple t) {
        String n = t.getValueByField("json").toString();
        collector.emit(t, new Values(n));
    }


    /* (non-Javadoc)
     * @see backtype.storm.topology.IComponent#declareOutputFields(backtype.storm.topology.OutputFieldsDeclarer)
     */
    public void declareOutputFields(OutputFieldsDeclarer arg0) {
        arg0.declare(new Fields("json"));
    }


    /* (non-Javadoc)
     * @see backtype.storm.topology.IComponent#getComponentConfiguration()
     */
    public Map<String, Object> getComponentConfiguration() {
        return null;
    }

    /* (non-Javadoc)
     * @see backtype.storm.topology.IBasicBolt#cleanup()
     */
    @Override
    public void cleanup() {
        // Nothing to cleanup
    }


    /* (non-Javadoc)
     * @see backtype.storm.topology.IRichBolt#prepare(java.util.Map, backtype.storm.task.TopologyContext, backtype.storm.task.OutputCollector)
     */
    @SuppressWarnings("rawtypes")
    public void prepare(Map arg0, TopologyContext context, OutputCollector collector) {
        this.collector = collector;
    }
}