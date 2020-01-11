import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class Main {

    public static void main(String[] args) {

        int numThreads = 4;
        int nIterations = 5;

        List<String> sizes = Arrays.asList("50kb", "100kb", "200kb", "500kb", "1mb", "2mb", "4mb", "8mb", "16mb", "32mb");
        sizes.forEach(size -> {

            String filename = "../../../Files/artusi_" + size + ".txt";

            // Compute bigrams
            execute(2, nIterations, numThreads, filename);

            // Compute trigrams
            execute(3, nIterations, numThreads, filename);
        });

    }

    public static void execute(int n, int nIterations, int threads, String filename) {

        LinesExtractor linesExtractor = new LinesExtractor(filename);
        List<String> lines = new ArrayList<>(linesExtractor.extractLines());

        System.out.println("[*] Number of lines: " + lines.size());

        List<String> words = new ArrayList<>();
        lines.forEach(line -> {
            words.addAll(Arrays.asList(line.split("\\s+")));
        });

        words.removeAll(Collections.singleton(""));

        System.out.println("[*] Number of words: " + words.size());

        System.out.println("[*] Computing " + ((n==2) ? "bigrams" : "trigrams") + " with " + nIterations + " iterations using " + threads + " threads on " + filename);

        float averageTime;
        float sum = 0;
        for (int i=0; i<nIterations; i++) {
            sum += parallelFindNgrams(n, threads, words);
        }
        averageTime = sum/nIterations;

        System.out.println("[i] Averaged time: " + averageTime + "s\n");
    }

    public static float parallelFindNgrams(int n, int numThreads, List<String> words) {

        AtomicInteger globalCounter = new AtomicInteger(0);

        List<NGramThread> threads = new ArrayList<>();
        int blockSize = words.size()/numThreads+1;

        int i = 0;

        long start = System.currentTimeMillis();

        while (i < numThreads) {
            threads.add(new NGramThread(i, globalCounter, words, n, i*blockSize, (i+1)*blockSize));
            threads.get(i).start();
            i++;
        }

        for (NGramThread worker: threads) {
            try {
                worker.join();
            } catch (InterruptedException ignored) {}
        }

        long end = System.currentTimeMillis();

        /*if (n==2) {
            System.out.println("[i] #bigrams: " + globalCounter);
        } else if (n==3) {
            System.out.println("[i] #trigrams: " + globalCounter);
        }*/
        //System.out.println("[i] Time: " + (float)(end-start)/1000 + "s\n");
        return (float)(end-start)/1000;
    }
}