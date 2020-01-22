#!/usr/bin/python

from matplotlib import pyplot as plt

sizes = ['50kb', '100kb', '200kb', '500kb', '1mb', '2mb', '4mb', '8mb', '16mb', '32mb']

# TEMPI SEQUENZIALE vs PARALLELO JAVA (BIGRAMMI)
plt.figure(figsize=(8,5))
times_bigrams_java_seq = [0.0054, 0.010199999, 0.031200001, 0.0412, 0.0978, 0.18139999, 0.3116, 0.6382, 1.4016, 3.5723999]
times_bigrams_java_2threads = [0.0104, 0.0095999995, 0.0146, 0.033, 0.083399996, 0.14660001, 0.283, 0.5224, 1.2248, 2.829]
times_bigrams_java_4threads = [0.0094, 0.0064000003, 0.0134, 0.0182, 0.0592, 0.113199994, 0.26920003, 0.5666, 1.0968001, 2.7922]
plt.plot(sizes, times_bigrams_java_seq)
plt.plot(sizes, times_bigrams_java_2threads)
plt.plot(sizes, times_bigrams_java_4threads)
plt.ylabel('Tempi (s)')
plt.gca().legend(('Sequenziale','2 Thread', '4 Thread'), loc='upper left')
plt.grid()
plt.title('Java Bigrammi', fontweight='bold')
plt.savefig('tempi_java_bigrammi.png')

# TEMPI SEQUENZIALE vs PARALLELO JAVA (TRIGRAMMI)
plt.figure(figsize=(8,5))
times_trigrams_java_seq = [0.0014000001, 0.004, 0.0098, 0.0418, 0.0674, 0.12060001, 0.24560001, 0.46820003, 1.1596, 2.556]
times_trigrams_java_2threads = [0.0098, 0.0086, 0.008400001, 0.0264, 0.0592, 0.056599997, 0.2326, 0.4466, 0.9528, 2.0742]
times_trigrams_java_4threads = [0.0056000003, 0.003, 0.0078, 0.016599999, 0.0648, 0.1012, 0.18259999, 0.43319997, 0.93999994, 1.7978001]
plt.plot(sizes, times_trigrams_java_seq)
plt.plot(sizes, times_trigrams_java_2threads)
plt.plot(sizes, times_trigrams_java_4threads)
plt.ylabel('Tempi (s)')
plt.gca().legend(('Sequenziale','2 Thread', '4 Thread'), loc='upper left')
plt.grid()
plt.title('Java Trigrammi', fontweight='bold')
plt.savefig('tempi_java_trigrammi.png')

# TEMPI SEQUENZIALE vs PARALLELO C++ (BIGRAMMI)
plt.figure(figsize=(8,5))
times_bigrams_cpp_2threads = [0.00547881, 0.00800728, 0.0185235, 0.0365383, 0.0812789, 0.167174, 0.296752, 0.615861, 1.33861, 2.69426]
times_bigrams_cpp_4threads = [0.00622182, 0.00862616, 0.016456, 0.0323416, 0.0824938, 0.173515, 0.300432, 0.62582, 1.31204, 2.76904]
plt.plot(sizes, times_bigrams_java_seq)
plt.plot(sizes, times_bigrams_cpp_2threads)
plt.plot(sizes, times_bigrams_cpp_4threads)
plt.ylabel('Tempi (s)')
plt.gca().legend(('Sequenziale','2 Thread', '4 Thread'), loc='upper left')
plt.grid()
plt.title('C++ Bigrammi', fontweight='bold')
plt.savefig('tempi_cpp_bigrammi.png')

# TEMPI SEQUENZIALE vs PARALLELO C++ (TRIGRAMMI)
plt.figure(figsize=(8,5))
times_trigrams_cpp_2threads = [0.00253505, 0.00617335, 0.0136274, 0.0486875, 0.0543259, 0.111901, 0.213461, 0.449823, 0.932955, 1.8912]
times_trigrams_cpp_4threads = [0.00284309, 0.00538997, 0.0134662, 0.0342728, 0.0550195, 0.11203, 0.235621, 0.440845, 0.833858, 1.7818]
plt.plot(sizes, times_trigrams_java_seq)
plt.plot(sizes, times_trigrams_cpp_2threads)
plt.plot(sizes, times_trigrams_cpp_4threads)
plt.ylabel('Tempi (s)')
plt.gca().legend(('Sequenziale','2 Thread', '4 Thread'), loc='upper left')
plt.grid()
plt.title('C++ Trigrammi', fontweight='bold')
plt.savefig('tempi_cpp_trigrammi.png')

# SPEEDUP JAVA BIGRAMMI
plt.figure(figsize=(8,5))
speedup_bigram_java_2thread = [x/y for x, y in zip(times_bigrams_java_seq, times_bigrams_java_2threads)]
speedup_bigram_java_4thread = [x/y for x, y in zip(times_bigrams_java_seq, times_bigrams_java_4threads)]
plt.plot(sizes, speedup_bigram_java_2thread)
plt.plot(sizes, speedup_bigram_java_4thread)
plt.ylabel('Speedup')
plt.gca().legend(('2 Thread', '4 Thread'), loc='upper left')
plt.grid()
plt.title('Speedup Java Bigrammi', fontweight='bold')
plt.savefig('speedup_java_bigrammi.png')

# SPEEDUP JAVA TRIGRAMMI
plt.figure(figsize=(8,5))
speedup_trigram_java_2thread = [x/y for x, y in zip(times_trigrams_java_seq, times_trigrams_java_2threads)]
speedup_trigram_java_4thread = [x/y for x, y in zip(times_trigrams_java_seq, times_trigrams_java_4threads)]
plt.plot(sizes, speedup_trigram_java_2thread)
plt.plot(sizes, speedup_trigram_java_4thread)
plt.ylabel('Speedup')
plt.gca().legend(('2 Thread', '4 Thread'), loc='upper left')
plt.grid()
plt.title('Speedup Java Trigrammi', fontweight='bold')
plt.savefig('speedup_java_trigrammi.png')

# SPEEDUP C++ BIGRAMMI
plt.figure(figsize=(8,5))
speedup_bigram_cpp_2thread = [x/y for x, y in zip(times_bigrams_java_seq, times_bigrams_cpp_2threads)]
speedup_bigram_cpp_4thread = [x/y for x, y in zip(times_bigrams_java_seq, times_bigrams_cpp_4threads)]
plt.plot(sizes, speedup_bigram_cpp_2thread)
plt.plot(sizes, speedup_bigram_cpp_4thread)
plt.ylabel('Speedup')
plt.gca().legend(('2 Thread', '4 Thread'), loc='upper left')
plt.grid()
plt.title('Speedup C++ Bigrammi', fontweight='bold')
plt.savefig('speedup_cpp_bigrammi.png')

# SPEEDUP C++ TRIGRAMMI
plt.figure(figsize=(8,5))
speedup_trigram_cpp_2thread = [x/y for x, y in zip(times_trigrams_java_seq, times_trigrams_cpp_2threads)]
speedup_trigram_cpp_4thread = [x/y for x, y in zip(times_trigrams_java_seq, times_trigrams_cpp_4threads)]
plt.plot(sizes, speedup_trigram_cpp_2thread)
plt.plot(sizes, speedup_trigram_cpp_4thread)
plt.ylabel('Speedup')
plt.gca().legend(('2 Thread', '4 Thread'), loc='upper left')
plt.grid()
plt.title('Speedup C++ Trigrammi', fontweight='bold')
plt.savefig('speedup_cpp_trigrammi.png')