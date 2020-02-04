package tiw.tiw6.storm.race;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import org.junit.Before;
import org.junit.Test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.*;

public class RaceTest {

    private static final ObjectMapper OBJECT_MAPPER = new ObjectMapper();
    private Race race;

    @Before
    public void setup() {
        race = new Race(3);
    }

    @Test
    public void testNextJSONString() throws IOException {
        String jsonString = race.nextJSONString();
        JsonNode root = OBJECT_MAPPER.readTree(jsonString);
        assertNotNull(root);
        assertTrue(root.isObject());
        ArrayNode tortoises = (ArrayNode) ((ObjectNode) root).get("tortoises");
        assertNotNull(tortoises);
        assertEquals(3, tortoises.size());
        String[] expectedFields = {"id", "top", "position", "nbDevant", "nbDerriere", "total"};
        Arrays.sort(expectedFields);
        for (JsonNode tortoise : tortoises) {
            List<String> fields = new ArrayList<>();
            tortoise.fieldNames().forEachRemaining(fields::add);
            String[] fieldsA = fields.toArray(new String[fields.size()]);
            Arrays.sort(fieldsA);
            assertArrayEquals(expectedFields,fieldsA);
        }
    }

}
