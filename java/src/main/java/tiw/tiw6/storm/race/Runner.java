package tiw.tiw6.storm.race;

import java.io.Serializable;

/**
 * A runner in a race.
 */
public class Runner implements Serializable {
    private static final int TRACK_SIZE = 255;
    private static final int MAX_FORWARD = 10;

    private int id;
    private long absPosition = 0L;

    public Runner(int id) {
        this.id = id;
    }

    public int getPosition() {
        return (int) (absPosition % TRACK_SIZE);
    }

    public void step() {
        absPosition = absPosition + (long) Math.ceil(Math.random() * MAX_FORWARD);
    }

    public int getId() {
        return id;
    }

    public long getAbsPosition() {
        return absPosition;
    }
}
