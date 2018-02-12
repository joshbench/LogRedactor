# LogRedactor
Python Script that redacts credit cards and social security numbers from specific gzip log files

To Run:

 - Add filenames of gzipped logs to be redacted as arguments to this script, separated by spaces.
 - Make sure the gzip files have the '.gz' extension
 - This does accept wildcard input

EXAMPLES:

  - python3 LogRedactor.py *.gz
  - python3 LogRedactor.py log1.gz log2.gz log3.gz
  
