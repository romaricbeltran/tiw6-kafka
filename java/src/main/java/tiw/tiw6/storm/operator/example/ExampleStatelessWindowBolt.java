package tiw.tiw6.storm.operator.example;

import com.fasterxml.jackson.databind.node.ObjectNode;
import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseWindowedBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;
import org.apache.storm.windowing.TupleWindow;

import java.util.List;
import java.util.Map;

import static tiw.tiw6.storm.data.Utils.MAPPER;


public class ExampleStatelessWindowBolt extends BaseWindowedBolt {
    private static final long serialVersionUID = 4262387370788107343L;
    private transient OutputCollector collector;

    @Override
    public void prepare(Map stormConf, TopologyContext context, OutputCollector collector) {
        this.collector = collector;
    }

    @Override
    public void execute(TupleWindow inputWindow) {

        final List<Tuple> tuples = inputWindow.get();
        int cpt = tuples.size();
        // Do some computation with tuples here
        ObjectNode r = MAPPER.createObjectNode();
        r.put("test", "statelessWithWindow");
        r.put("nbTuplesInWindow", cpt);

        collector.emit(tuples, new Values(r.toString()));

    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
        declarer.declare(new Fields("json"));
    }
}






