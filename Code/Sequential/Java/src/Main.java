import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class Main {
    public static void main(String[] args) throws InterruptedException {

        int nIterations = 10;
        String filename = "../../../Files/artusi_32mb.txt";

        // Compute bigrams
        execute(2, nIterations, filename);

        TimeUnit.SECONDS.sleep(2);

        // Compute trigrams
        execute(3, nIterations, filename);
    }

    public static void execute(int n, int nIterations, String filename) {

        LinesExtractor linesExtractor = new LinesExtractor(filename);
        List<String> lines = new ArrayList<>(linesExtractor.extractLines());

        System.out.println("[*] Number of lines: " + lines.size());

        List<String> words = new ArrayList<>();
        lines.forEach(line -> {
            words.addAll(Arrays.asList(line.split("\\s+")));
        });

        words.removeAll(Collections.singleton(""));

        System.out.println("[*] Number of words: " + words.size());

        System.out.println("[*] Computing " + ((n==2) ? "bigrams" : "trigrams") + " with " + nIterations + " iterations on " + filename);

        float averageTime;
        float sum = 0;
        for (int i=0; i<nIterations; i++) {
            sum += sequentialFindNgrams(n, words);
        }
        averageTime = sum/nIterations;

        System.out.println("[i] Averaged time: " + averageTime + "s\n");
    }

    public static float sequentialFindNgrams(int n, List<String> words) {

        long start = System.currentTimeMillis();

        List<String> ngrams = new ArrayList<>();
        for (String word: words) {
            if (word.length() >= n) {
                for (int i = 0; i < word.length() - (n - 1); i++) {
                    ngrams.add(word.substring(i, i + n));
                }
            }
        }
        long end = System.currentTimeMillis();

        /*if (n==2) {
            System.out.println("[*] Found " + ngrams.size() + " bigrams!");
        } else if (n==3) {
            System.out.println("[*] Found " + ngrams.size() + " trigrams!");
        }*/

        //System.out.println("[i] Time: " + (float)(end-start)/1000 + "s\n");
        return (float)(end-start)/1000;
    }
}
