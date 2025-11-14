# 120+ Python Terminal Project Ideas

**Scope:** All projects are *terminal/CLI-only* — no websites, no graphical apps. You may use Python standard library and common packages (e.g., `numpy`, `pandas`, `matplotlib`, `requests`) **only if needed**; each project notes useful modules. Keep implementations runnable from the terminal.

---

## How to use this list

* Pick a difficulty level (Beginner → Advanced).
* Implement core functionality first, then add CLI arguments, config files, tests, and optional packages.
* Write a README with usage examples and sample input/output for each project.

---

## Beginner (1–30)

Small projects focused on core Python: I/O, control flow, data structures.

1. **Basic Calculator** — CLI calculator supporting + - * / and parentheses. (modules: `ast` optional)
2. **Unit Converter** — convert units (length, weight, temperature) with interactive prompts. (modules: none)
3. **To‑Do List** — terminal to‑do manager saved to a local JSON file. (modules: `json`, `argparse`)
4. **Countdown Timer** — countdown and alert message when done. (modules: `time`, `sys`)
5. **Pomodoro Timer** — simple Pomodoro cycles with terminal notifications. (modules: `time`)
6. **Simple Quiz Game** — load questions from a file and score the user. (modules: `csv`, `json`)
7. **Word Counter** — like `wc`, show words, lines, characters for a text file. (modules: `argparse`)
8. **File Renamer** — batch rename files in a folder using rules (prefix, suffix, regex). (modules: `os`, `re`)
9. **Password Generator** — generate secure passwords with options for length and character sets. (modules: `secrets`, `string`)
10. **Password Strength Checker** — analyze a password and rate strength. (modules: `re`)
11. **BMI Calculator** — read height/weight and give BMI category. (modules: none)
12. **Simple Expense Tracker** — track expenses to CSV and show monthly totals. (modules: `csv`, `datetime`)
13. **Random Quote CLI** — print a random inspirational quote from a local file. (modules: `random`)
14. **Mad Libs Generator** — prompt user for words and fill a template story. (modules: none)
15. **Number Guessing Game** — classic higher/lower game with stats across sessions. (modules: `random`, `json`)
16. **FizzBuzz CLI** — extended version with custom rules and output file. (modules: none)
17. **Simple Alarm Clock** — set a time and run a command or print message. (modules: `datetime`, `subprocess` optional)
18. **Text Reverser / Palindrome Tester** — reverse lines or test palindromes. (modules: none)
19. **CSV Sorter** — sort CSV rows by a given column. (modules: `csv`, `argparse`)
20. **Simple Logger** — create a small logging utility that rotates files. (modules: `logging`, `logging.handlers`)
21. **Dice Roller** — roll complex dice expressions like `3d6+2`. (modules: `random`, `re`)
22. **Contact Book** — store contacts in JSON and support search/update/delete. (modules: `json`, `argparse`)
23. **Countdown to Date** — show days/hours/minutes to a target date. (modules: `datetime`)
24. **Simple Clipboard Manager** — save and retrieve small text snippets (terminal only). (modules: `json`, `pyperclip` optional)
25. **Palindrome Finder in Text** — list palindromic words from input text. (modules: `re`)
26. **Simple CSV to Markdown Table** — convert CSV into a markdown table printed in terminal. (modules: `csv`)
27. **Line Diff Tool** — show simple line-based diff between two text files. (modules: `difflib`)
28. **Basic Hangman** — terminal hangman using dictionary file. (modules: `random`)
29. **Image File Inspector** — read image metadata (format, size) in terminal. (modules: `Pillow` optional)
30. **Simple Calendar Printer** — show month/year calendar; allow annotations. (modules: `calendar`, `datetime`)

---

## Intermediate (31–70)

Projects that introduce file I/O, algorithms, testing, and small external packages.

31. **Todo with Priorities & Tags** — CLI with search, filters, and persistence. (modules: `sqlite3` optional)
32. **CLI Habit Tracker** — track daily habits, streaks, and export stats. (modules: `csv`, `datetime`)
33. **Markdown Previewer** — convert markdown to terminal-friendly text (bold/italic). (modules: `markdown` optional)
34. **Terminal-Based Flashcards** — spaced repetition algorithm (SM-2) for study. (modules: `json`, `datetime`)
35. **Expense Visualizer** — show ASCII charts of spending per category. (modules: `matplotlib` optional)
36. **Text Search Engine** — index text files and provide boolean search in terminal. (modules: `re`, `collections`)
37. **File Backup Script** — incremental backups with timestamps and rotation. (modules: `shutil`, `os`)
38. **Log Analyzer** — parse server logs and produce summary stats. (modules: `re`, `argparse`)
39. **CLI RSS Reader (local)** — fetch RSS feeds to local files and read in terminal. (modules: `feedparser`, `requests` optional)
40. **CLI Chatbot (rule-based)** — pattern matching and response rules stored in files. (modules: `re`, `json`)
41. **Expense Splitter** — split bills among friends and produce settlement list. (modules: none)
42. **Simple Encryption Tool** — symmetric encryption of files using a password. (modules: `cryptography` optional)
43. **CSV Data Cleaner** — detect missing values, type-cast columns, export clean CSV. (modules: `pandas` optional)
44. **Command Aliaser** — create short aliases for long terminal commands stored locally. (modules: `json`, `subprocess` optional)
45. **Text-based Adventure Engine** — build a simple engine and a sample story. (modules: `json`)
46. **Personal Journal with Search** — encrypted or plain entries searchable by tags. (modules: `sqlite3`, `cryptography` optional)
47. **CLI Sudoku Solver** — parse sudoku from text and solve using backtracking. (modules: none)
48. **Maze Generator & Solver (ASCII)** — generate mazes and show solve path. (modules: `random`)
49. **Terminal Music Player (local)** — play audio files via system call with playlist support. (modules: `subprocess`)
50. **Simple Shell** — implement a tiny shell with piping and redirection support. (modules: `subprocess`, `shlex`)
51. **Network Port Scanner** — scan ports on IPs with rate limiting. (modules: `socket`, `argparse`)
52. **CLI Pomodoro Analytics** — record sessions and show productivity metrics. (modules: `csv`, `matplotlib` optional)
53. **Recipe Manager** — save recipes, scale ingredients, and generate shopping lists. (modules: `json`)
54. **Terminal Kanban Board** — columns and cards saved locally with drag-like commands. (modules: `json`)
55. **Binary/Hex Editor (basic)** — view and edit binary files in hex form. (modules: `struct`, `argparse`)
56. **Diff Merge Helper** — semi-automated three-way merge helper for text files. (modules: `difflib`)
57. **CLI Image to ASCII Converter** — convert images to ASCII art output. (modules: `Pillow` optional)
58. **Local Package Version Checker** — scan installed packages and report outdated ones. (modules: `pkg_resources`)
59. **Markdown TODOs Extractor** — scan markdown repository for `- [ ]` items and aggregate them. (modules: `os`, `re`)
60. **Personal Finance Forecast** — simple forecasting using historical CSV (moving averages). (modules: `pandas`, `numpy` optional)
61. **Command-Line Crossword Creator** — create printable crossword puzzles from word lists. (modules: none)
62. **CLI OCR Batch Runner** — run OCR on images in a folder and save text. (modules: `pytesseract`, `Pillow` optional)
63. **HTTP Status Monitor (local)** — check reachability of hosts (no web UI) and log changes. (modules: `requests` optional)
64. **Text Corpus Analyzer** — compute vocabulary, frequency, concordance from a corpus. (modules: `collections`, `nltk` optional)
65. **Terminal Calendar with Reminders** — add reminders that trigger commands. (modules: `sqlite3`, `datetime`)
66. **Habit-Building CLI Game** — gamify streaks, points, and rewards in terminal. (modules: `json`)
67. **Terminal-Based Conway's Game of Life** — step/auto-run modes and patterns loader. (modules: none)
68. **File Integrity Checker** — compute and verify checksums across backups. (modules: `hashlib`)
69. **CLI RSS Aggregator to Mailbox** — fetch feeds and save as mbox or text digest. (modules: `feedparser` optional)
70. **Hex-to-Assembly Toy Disassembler** — for simple instruction sets or bytecodes. (modules: none)

---

## Advanced (71–100)

Complex algorithms, systems tools, networking, concurrency, and data work — terminal-only.

71. **Static Site Link Checker (CLI)** — crawl local HTML files and report broken links (no server). (modules: `html.parser`, `os`)
72. **Dependency Graph Visualizer (ASCII)** — analyze Python imports in a project and show graph as ASCII. (modules: `ast`, `graphlib`)
73. **CLI Task Scheduler** — mini cron alternative that reads tasks from a config and runs commands. (modules: `subprocess`, `schedule` optional)
74. **Concurrent Web Crawler (to disk)** — crawl (if allowed) and archive pages as files; CLI only. (modules: `requests`, `asyncio`, `aiohttp` optional)
75. **Custom Database Engine (toy)** — build a simple append-only DB with indexes. (modules: `struct`, `mmap` optional)
76. **Markdown Static Site Generator (build step only)** — transforms markdown to HTML files on disk (no server). (modules: `markdown` optional)
77. **CLI BitTorrent-like Client (toy)** — demonstrate chunking and reassembly (local only). (modules: `socket`, `threading`)
78. **Network Packet Sniffer (requires privileges)** — capture and analyze packets, print summaries. (modules: `socket`, `struct`)
79. **Build a Mini Compiler** — parse simple language, generate bytecode, and execute a VM. (modules: `ply` optional)
80. **Genetic Algorithm Toolkit** — solve optimization problems via GA CLI with progress bars. (modules: `numpy` optional)
81. **Audio Signal Analyzer** — read WAV files, show frequency analysis in ASCII (FFT). (modules: `wave`, `numpy` optional)
82. **CLI Chat Server & Client (terminal)** — simple TCP chat application runnable in terminal. (modules: `socket`, `threading`)
83. **Distributed Key-Value Store (toy)** — simple leader election and replication for learning. (modules: `socket`, `pickle`)
84. **Static Binary Packer/Unpacker** — pack multiple files into a single custom binary with header. (modules: `struct`)
85. **Advanced Regex Tester** — test regex patterns across multiple files and show matches summary. (modules: `re`, `argparse`)
86. **Automated Grader** — run student scripts, capture outputs/errors, and grade. (modules: `subprocess`, `difflib`)
87. **Image Processing Toolkit (CLI)** — resize, crop, convert formats, and batch operations. (modules: `Pillow` optional)
88. **CLI Financial Backtester** — backtest simple strategies on CSV price data. (modules: `pandas`, `numpy` optional)
89. **Terminal-Based IDE Linter** — run static checks and show annotated source with suggestions. (modules: `ast`, `pylint` optional)
90. **Portable Package Bundler** — gather scripts and dependencies into a tarball with environment metadata. (modules: `tarfile`, `pkgutil`)
91. **Automated Interview Scheduler** — match slots between participants using algorithmic matching. (modules: `datetime`, `itertools`)
92. **CLI Encryption Suite** — support RSA/AES hybrid encryption for files. (modules: `cryptography` optional)
93. **Smart Backup Deduplicator** — detect duplicate files using content hashing and dedupe. (modules: `hashlib`, `os`)
94. **Log Replay Tool** — replay recorded events at real-time or accelerated speeds (for testing distributed systems). (modules: `time`, `json`)
95. **Constraint Solver (SAT toy)** — build a SAT solver and test small instances. (modules: none)
96. **Interactive Debugger (mini)** — step through Python code with breakpoints (toy). (modules: `bdb`, `inspect` optional)
97. **Terminal-based Spreadsheet Engine** — formulas, cell refs, and CSV import/export. (modules: `ast`, `csv`)
98. **CLI Neural Network Playground** — train small feedforward nets on toy datasets (no frameworks). (modules: `numpy` optional)
99. **Time Series Anomaly Detector** — detect anomalies in CSV time-series using stats. (modules: `pandas`, `numpy` optional)
100. **Multi-threaded Build System (like make)** — parse simple build rules and execute tasks with dependency ordering. (modules: `concurrent.futures`, `graphlib`)

---

## Data & ML Terminal Projects (101–120)

Data processing, analysis, and machine learning experiments run entirely from the terminal.

101. **CLI CSV Profiler** — produce a report of column types, missingness, and histograms. (modules: `pandas` optional)
102. **K‑Means from Scratch** — implement and run on CSV numeric data; print clusters and metrics. (modules: `numpy` optional)
103. **Text Classifier (toy)** — bag-of-words classifier using naive Bayes; train/test from terminal. (modules: `scikit-learn` optional)
104. **Word2Vec Tiny Trainer** — train skip-gram on small corpus and query embeddings. (modules: `numpy` optional)
105. **Data Augmentation Toolkit (CLI)** — generate modified versions of datasets (text/image). (modules: `Pillow`, `nlp` optional)
106. **Model Checkpoint Manager** — manage and compare saved model checkpoints and metrics. (modules: `json`, `pickle`)
107. **CLI Hyperparameter Explorer** — run grid/random search across scripts and aggregate results. (modules: `concurrent.futures`)
108. **Confusion Matrix Visualizer (ASCII)** — train classifier and show confusion matrix in terminal. (modules: `numpy`, `pandas` optional)
109. **Dimensionality Reduction Demo** — run PCA/t-SNE on numeric CSV and print embeddings. (modules: `numpy`, `sklearn` optional)
110. **CLI Data Imputer** — implement mean/median/KNN imputation for missing values in CSV. (modules: `pandas`, `numpy` optional)
111. **Feature Store Simulator** — local feature extraction and versioned storage for ML experiments. (modules: `sqlite3`, `pandas` optional)
112. **Streaming Data Processor** — read a stream (file tail) and compute rolling statistics. (modules: none)
113. **Batch Image Labeling Tool (terminal-driven)** — show filename and accept keyboard label input saved to CSV. (modules: none)
114. **Text Summarizer (extractive)** — implement simple extractive summarization algorithms and run on files. (modules: `nltk` optional)
115. **CLI Reinforcement Learning Gridworld** — implement Q‑learning and display policy in terminal. (modules: `numpy` optional)
116. **Data Versioning CLI** — snapshot datasets and compare differences between versions. (modules: `hashlib`, `json`)
117. **Streaming Anomaly Alert** — tail logs and print alerts based on thresholds or pattern frequency. (modules: `re`, `collections`)
118. **CLI EDA Report Generator** — generate a text report with distributions, correlations, and recommendations. (modules: `pandas` optional)
119. **Bayesian Inference Playground** — implement simple Bayesian updating examples and visualize text output. (modules: `numpy` optional)
120. **CLI Recommendation System Demo** — simple collaborative filtering from CSV interaction data. (modules: `numpy`, `pandas` optional)

---

## Ideas for extension & grading

* Add unit tests (`unittest` or `pytest`).
* Create CLI flags (`argparse`) and subcommands.
* Add example datasets and a `Makefile` to run demos.
* Benchmark performance and document complexity.

---

If you want, I can: add short starter templates for any 10 of these projects, or generate a GitHub-ready README + CLI skeleton for one project you pick.
