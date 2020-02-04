package tiw.tiw6.storm.operator.example;

import com.fasterxml.jackson.databind.node.ObjectNode;
import org.apache.storm.state.KeyValueState;
import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseStatefulWindowedBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;
import org.apache.storm.windowing.TupleWindow;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.List;
import java.util.Map;

import static tiw.tiw6.storm.data.Utils.MAPPER;


public class ExampleStatefulWindowBolt extends BaseStatefulWindowedBolt<KeyValueState<String, Integer>> {
    private static final long serialVersionUID = 4262379330788107343L;
    private static final Logger LOG = LoggerFactory.getLogger(ExampleStatefulWindowBolt.class);
    private transient KeyValueState<String, Integer> state;

    private transient OutputCollector collector;

    @Override
    public void prepare(Map stormConf, TopologyContext context, OutputCollector collector) {
        this.collector = collector;
    }

    @Override
    public void initState(KeyValueState<String, Integer> state) {
        this.state = state;
        int sum = state.get("sum", 0);
        LOG.info("initState with state [ {} ] current sum [ {} ]", state, sum);
    }

    @Override
    public void execute(TupleWindow inputWindow) {

        final List<Tuple> tuples = inputWindow.get();
        int cpt = tuples.size();
        // Do something with the tuples here
        state.put("sum", cpt);

        ObjectNode object = MAPPER.createObjectNode();
        object.put("test", "statelessWithWindow");
        object.put("nbNewTuples", cpt);
        object.put("totalNumberOfTuples", cpt);
        collector.emit(tuples, new Values(object.toString()));
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
        declarer.declare(new Fields("json"));
    }
}

