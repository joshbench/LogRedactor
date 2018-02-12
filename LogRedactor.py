## Import libraries
import gzip, re, sys, logging, shutil

## Configure loging with log file
logging.basicConfig(filename="redactor_audit.log", level=logging.INFO, filemode='w')
 
## Function: Check if lines contain sensitive info
def not_contain_pii(line):
    ## build regular expressions to check for CC or SSN
    ssn = re.compile('.*SSN="\d{3}-\d{2}-\d{4}".*')
    cc = re.compile('.*CC="\d{4}-\d{4}-\d{4}-\d{4}".*')
    ## Check if those expressions match the input string
    if ssn.match(line) or cc.match(line):
        return False
    else:
        return True

## Function: Redact lines from gzip file, saving to new file
def redact(gzin):
    ## Create filename for redacted version
    gzout = gzin + ".redacted.gz"
    ## initialize counters
    redacted_lines = 0
    processed_lines = 0

    ## Open gzip file to write to
    with gzip.GzipFile(gzout, 'w') as fout:
        ## Open provided gzip file to begin reading from
        with gzip.GzipFile(gzin,'r') as fin:
            ## Read lines into memory one by one
            for line in fin:
                ## write non-pii lines to the output gzip
                if not_contain_pii(line.decode('utf-8')):
                    fout.write(line)
                else:
                    redacted_lines += 1
                processed_lines += 1

    ## Copy metadata to new file
    shutil.copystat(gzin, gzout)
    ## Write name, total lines processed, total lines redacted to log
    logging.info("Filename: " + gzin + "; Processed lines: " + str(processed_lines) + "; Redacted lines: " + str(redacted_lines))

## Loop through arguments, run the redact function on each file name ending in .gz
for filename in sys.argv[1:]:
    if filename.endswith('.gz'):
        redact(filename)