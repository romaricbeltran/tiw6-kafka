package tiw.tiw6.storm.race;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import tiw.tiw6.storm.data.Tortoise;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

import static tiw.tiw6.storm.data.Utils.MAPPER;

/**
 * Représente une course de tortues
 */
public class Race implements Iterator<Collection<Tortoise>>, Serializable {

    private ArrayList<Runner> runners;
    private long top = 0;

    public Race(int nbRunners) {
        runners = new ArrayList<>(nbRunners);
        for (int i = 0; i < nbRunners; i++) {
            runners.add(new Runner(i));
        }
    }

    public boolean hasNext() {
        return true;
    }

    @Override
    public Collection<Tortoise> next() {
        step();
        Collection<Tortoise> result = new ArrayList<>(runners.size());
        for (Runner r : runners) {
            int before = (int) runners.stream()
                    .filter(r2 -> r2.getAbsPosition() > r.getAbsPosition())
                    .count();
            int after = (int) runners.stream()
                    .filter(r2 -> r2.getAbsPosition() < r.getAbsPosition())
                    .count();
            result.add(new Tortoise(r.getId(), top, r.getPosition(), before, after, runners.size()));
        }
        return result;
    }

    private void step() {
        runners.stream()
                .forEach(Runner::step);
        top = top + 1;
    }

    public JsonNode nextJSON() {
        Collection<Tortoise> tortoises = next();
        ObjectNode node = MAPPER.createObjectNode();
        JsonNode tortoisesJ = MAPPER.valueToTree(tortoises);
        node.set("tortoises", tortoisesJ);
        return node;
    }

    public String nextJSONString() {
        return nextJSON().toString();
    }
}
