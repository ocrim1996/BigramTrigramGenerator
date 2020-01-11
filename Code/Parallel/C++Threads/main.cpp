#include <iostream>
#include <algorithm>
#include <vector>
#include <chrono>
#include <thread>
#include <future>
#include <sstream>
#include "LinesExtractor.h"

using namespace std;

void run(atomic_int& counter, int id, int n, vector<string> words, int start, int stop) {

    int nGramCounter = 0;

    if (stop > words.size()) stop = words.size();

    //cout << "Thread " << id << " iterating from word " << start << " to word " << stop << endl;

    vector<string> ngrams;
    for (int i=start; i<stop; i++) {
        if (words[i].length() >= n) {
            for (int j=0; j<words[i].length()-(n-1); j++) {
                ngrams.push_back(words[i].substr(j, n));
                nGramCounter++;
            }
        }
    }

    //cout << "Thread " << id << " found " << nGramCounter << " ngrams" << endl;

    counter.fetch_add(nGramCounter, memory_order_relaxed);

}

double parallelFindNgrams(int n, int numThreads, vector<string> words) {


    int blockSize = words.size() / numThreads + 1;
    atomic_int globalCounter(0);

    auto start = chrono::steady_clock::now();

    std::vector<thread> threads(numThreads);
    for (int i = 0; i < numThreads; i++) {
        threads[i] = thread(run, ref(globalCounter), i, n, words, i * blockSize, (i + 1) * blockSize);
    }
    for (auto &th: threads) {
        th.join();
    }

    auto end = chrono::steady_clock::now();
    std::chrono::duration<double> elapsedSeconds = end - start;

    /*if (n == 2) {
        cout << "[i] Found " << globalCounter << " bigrams!" << endl;
    } else {
        cout << "[i] Found " << globalCounter << " trigrams!" << endl;
    }*/
//    cout << "[i] Time: " << elapsedSeconds.count() << " seconds" << endl;

    return elapsedSeconds.count();
}

void execute(int n, int nIterations, int threads, const string& filename) {

    // Extract lines
    vector<string> lines = LinesExtractor::extractLines(filename);
    cout << "[*] Number of lines: " << lines.size() << endl;

    // Extract all words from lines
    vector<string> words;
    for (auto &line: lines) {
        stringstream ss(line);
        istream_iterator<string> begin(ss), end;
        vector<string> lineWords(begin, end);
        for (auto &word: lineWords) {
            words.push_back(word);
        }
    }
    cout << "[*] Number of words: " << words.size() << endl;

    cout << "[*] Computing " << ((n==2) ? "bigrams" : "trigrams") << " with " << nIterations << " iterations using " << threads << " threads on " << filename << endl;

    double averageTime;
    double sum = 0;
    for (int i=0; i<nIterations; i++) {
        sum += parallelFindNgrams(n, threads, words);
    }
    averageTime = sum/nIterations;

    cout << "[i] Averaged time: " << averageTime << "\n" << endl;
}

int main(int argc, char const *argv[]) {

    int numThreads = 4;
    int nIterations = 5;

    vector<string> sizes = {"50kb", "100kb", "200kb", "500kb", "1mb", "2mb", "4mb", "8mb", "16mb", "32mb"};
    for (auto &size: sizes) {
        string filename = "../../../../Files/artusi_" + size + ".txt";

        // Compute bigrams
        execute(2, nIterations, numThreads, filename);

        // Compute trigrams
        execute(3, nIterations, numThreads, filename);
    }

}
