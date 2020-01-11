import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;

public class LinesExtractor {

    private String filename;

    public LinesExtractor(String filename) {
        this.filename = filename;
    }

    public List<String> extractLines() {

        List<String> finalLines = new ArrayList<>();
        List<String> allLines = null;

        try {
            allLines = Files.readAllLines(FileSystems.getDefault().getPath("", filename));
        } catch (IOException e) {
            System.out.println("Failed to read " + filename);
        }

        assert allLines != null;
        allLines.forEach(line -> {
            if (!line.isBlank() && !line.isEmpty()) {
                line = line.toLowerCase().replaceAll("[^A-Za-z0-9' ]","");
                finalLines.add(line);
            }
        });

        return finalLines;
    }
}