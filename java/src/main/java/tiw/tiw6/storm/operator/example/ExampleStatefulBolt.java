package tiw.tiw6.storm.operator.example;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import org.apache.storm.state.KeyValueState;
import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseStatefulBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;

import java.util.Map;


public class ExampleStatefulBolt extends BaseStatefulBolt<KeyValueState<String, Integer>> {
    private static final long serialVersionUID = 4262379330722107343L;
    transient KeyValueState<String, Integer> kvState;
    int sum;
    private transient OutputCollector collector;


    @Override
    public void execute(Tuple t) {

        sum++;

        kvState.put("sum", sum);

        ObjectMapper mapper = new ObjectMapper();
        ObjectNode object = mapper.createObjectNode();
        object.put("test", "statelessWithWindow");
        object.put("nbNewTuples", 1);
        object.put("totalNumberOfTuples", sum);
        collector.emit(t, new Values(object.toString()));
    }

    @Override
    public void initState(KeyValueState<String, Integer> state) {
        kvState = state;
        sum = kvState.get("sum", 0);

    }

    @Override
    public void prepare(Map stormConf, TopologyContext context, OutputCollector collector) {
        this.collector = collector;
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
        declarer.declare(new Fields("json"));
    }


}