import java.nio.file.*;
import java.io.IOException;

public class FileCopy {
    public static void main(String[] args) throws IOException {
        String content = new String(Files.readAllBytes(Paths.get("input.txt")));
        Files.write(Paths.get("output.txt"), content.getBytes());
    }
}
