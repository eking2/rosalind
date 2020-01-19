from Bio import SeqIO

def revp():

    record = SeqIO.read('data/rosalind_revp.txt', 'fasta')

    # save position and lengths
    results = []

    # start from beginning of string and loop down
    for start in range(len(record.seq)):

        # chunk sequence into lengths of 4-12 bp
        for i in range(4, 13):
            chunk = record[start : start + i]

            # end of string will have duplicate chunks when sequence runs out
            if len(chunk) < i:
                break

            # check if palindrome
            if chunk.seq == chunk.reverse_complement().seq:
                chunk_pos = start + 1
                chunk_len = i
                results.append([chunk_pos, chunk_len])

    for result in results:
        print(result[0], result[1])


revp()


