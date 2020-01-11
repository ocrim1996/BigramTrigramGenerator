import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class NGramThread extends Thread {

    private int id, n, start, stop;
    private List<String> words;
    private AtomicInteger globalCounter;
    private int nGramCounter = 0;

    public NGramThread(int id, AtomicInteger globalCounter, List<String> words, int n, int start, int stop) {
        this.id = id;
        this.n = n;
        this.words = words;
        this.globalCounter = globalCounter;
        this.start = start;
        this.stop = stop;
    }

    public void run() {

        if (stop > words.size()) stop = words.size();

        //System.out.println("Thread " + id + " iterating from word " + start + " to word " + stop);

        List<String> ngrams = new ArrayList<>();
        for (int i=start; i<stop; i++) {
            if (words.get(i).length() >= n) {
                for (int j = 0; j < words.get(i).length() - (n-1); j++) {
                    ngrams.add(words.get(i).substring(j, j+n));
                    //System.out.println(words.get(i).substring(j, j+n));
                    nGramCounter++;
                }
            }
        }
        globalCounter.addAndGet(nGramCounter);
    }
}