package tiw.tiw6.storm;

import org.slf4j.LoggerFactory;

import java.io.Closeable;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;

public class NetworkWriter implements Closeable {
    private static final String DEFAULT_HOST = "localhost";
    private static final int DEFAULT_PORT = 12345;
    private String host;
    private int port;
    private Socket socket = null;
    private PrintWriter writer = null;

    public NetworkWriter(String host, int port) {
        this.host = host;
        this.port = port;
    }

    public NetworkWriter() {
        this(DEFAULT_HOST, DEFAULT_PORT);
    }

    private void openSocketIfNeeded() {
        if (socket == null || socket.isClosed()) {
            try {
                socket = new Socket(host, port);
                writer = new PrintWriter(socket.getOutputStream());
            } catch (IOException e) {
                LoggerFactory.getLogger(NetworkWriter.class).error("Error while open connection to monitor", e);
                close();
            }
        }
    }

    public void write(String data) {
        openSocketIfNeeded();
        if (writer != null) {
            writer.println(data);
            writer.flush();
        }
    }

    public void close() {
        if (writer != null) {
            writer.close();
            writer = null;
        }
        if (socket != null) {
            try {
                socket.close();
            } catch (IOException e) {
                // Do nothing as socket will be discarted anyway
            }
            socket = null;
        }
    }
}
