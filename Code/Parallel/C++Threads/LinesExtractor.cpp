//
// Created by ned on 10/01/2020.
//

#include "LinesExtractor.h"
#include <string>
#include <regex>

using namespace std;

vector<string> LinesExtractor::extractLines(const string& filename) {

    vector<string> lines;

    string line;
    ifstream file(filename);

    if (!file) {
        throw runtime_error("Could not open file!");
    }

    // Regex to remove unwanted characters
    regex reg("[^A-Za-z0-9' ]");

    while (getline(file, line)) {
        // Tranform to lowercase
        transform(line.begin(), line.end(), line.begin(), ::tolower);
        // Cleanup
        string cleaned = regex_replace(line, reg, "");
        if (!cleaned.empty()) {
            lines.push_back(cleaned);
        }
    }

    file.close();
    return lines;
}
