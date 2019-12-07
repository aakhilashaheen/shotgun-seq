from __future__ import division
import random

def sample(n):
    number_to_sample = 1000

    with open("chr1_GL383518v1_alt.fa") as input:
        num_lines = sum([1 for line in input])
    total_records = int(num_lines)
    print("sampling " + str(number_to_sample) + " out of " + str(total_records) + " records")

    records_to_keep = set(random.sample(range(total_records + 1), number_to_sample))
    record_number = 0
    output = []
    with open("chr1_GL383518v1_alt.fa") as input:
            for line in input:
                if record_number in records_to_keep:
                        output.append(line.upper())
                record_number += 1

    with open("sample.txt","w") as outfile:
        outfile.write(''.join(output))

