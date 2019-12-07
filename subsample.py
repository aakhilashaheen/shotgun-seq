from __future__ import division
import random

def sample(n):
    sample_size = 1000

    with open("chr1_GL383518v1_alt.fa") as input:
        lines = sum([1 for line in input])
    total_records = int(lines)
    print("sampling " + str(sample_size) + "from " + str(total_records) + " records")

    records_selection = set(random.sample(range(total_records + 1), sample_size))
    record_number = 0
    output = []
    with open("chr1_GL383518v1_alt.fa") as input:
            for line in input:
                if record_number in records_selection:
                        output.append(line.upper())
                record_number += 1

    with open("sample.txt","w") as outfile:
        outfile.write(''.join(output.strip()))

