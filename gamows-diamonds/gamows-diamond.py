# Helper functions
# Generate all possible codons based on the 4 bases
def assemble_codons():
    bases = ['A', 'T', 'G', 'C']
    codons = []
    for b1 in bases:
        for b2 in bases:
            for b3 in bases:
                codons.append(f'{b1}{b2}{b3}')
    return codons


# Create complementary strand based on string input
def create_complementary_strand(strand: str) -> str:
    mapping = [['A', 'T', 'G', 'C'], ['T', 'A', 'C', 'G']]
    complementary = ''
    for aa in strand:
        aa_index = mapping[0].index(aa)
        comp_base = mapping[1][aa_index]
        complementary += comp_base
    return complementary


# Generate a list of complementary stands
def create_complementary_list(codons: list) -> list:
    lys = []
    for codon in codons:
        lys.append(create_complementary_strand(codon))
    return lys


# Create a list of possible diamonds based on gamow's diamonds theory
def create_possible_diamonds(input_codon: list) -> list:
    complement_codon = create_complementary_list(input_codon)

    diamond_paths = [[0, 1, 3, 2], [0, 2, 3, 1], [3, 1, 0, 2], [3, 2, 0, 1]] # possible ways to read the diamond strand
    possible_diamonds = []
    for i in range(len(input_codon)):
        aa_tot = input_codon[i][0:2] + complement_codon[i][1::]
        aa = list(aa_tot)
        for path in diamond_paths:
            diamond = ''
            for start in path:
                diamond += aa[start]
            possible_diamonds.append(diamond)

    possible_diamonds.sort()
    return possible_diamonds


# Convert dictionary values into a list of values, remove duplicates
def extract_unique_sub_list(dic: dict) -> list:
    lys = []
    for key in dic:
        value = dic[key]
        value.sort()
        if value not in lys:
            lys.append(value)
    return lys


# Create list of unique amino acids codons -> based on diamond-theory -> genetic code by gamow
def create_final_list(input_codons):
    dic = {}
    for i in range(len(input_codons)):
        curr_codon = input_codons[i]
        curr_diamonds = create_possible_diamonds([curr_codon])
        for diamond in curr_diamonds:
            if diamond in dic and curr_codon not in dic[diamond]:
                dic[diamond].append(curr_codon)
            elif diamond not in dic:
                dic[diamond] = [curr_codon]

    lys = extract_unique_sub_list(dic)
    lys.sort()
    return lys


# Procedural -> Get output required by problem
codon_list = assemble_codons()
final_list = create_final_list(codon_list)

print(final_list)
print(final_list[5][1])
