//
// Created by ned on 10/01/2020.
//

#ifndef PARALLELCPPBIGRAMTRIGRAMGENERATOR_LINESEXTRACTOR_H
#define PARALLELCPPBIGRAMTRIGRAMGENERATOR_LINESEXTRACTOR_H

#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

class LinesExtractor {
public:
    static vector<string> extractLines(const string& filename);
};


#endif //PARALLELCPPBIGRAMTRIGRAMGENERATOR_LINESEXTRACTOR_H
