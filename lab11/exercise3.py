class DNA:
  dna_string = ""

  def __init__(self, dna_string):
        self.dna_string = dna_string


  def get_dna_string(self):
        return self.dna_string

 
  def set_dna_string(self, dna_string):
        self.dna_string = dna_string

 

  def count_nucleotides(self):
        dna_dic = {"A":0,"T":0,"C":0,"G":0}
        for char in self.dna_string:
            dna_dic[char]+=1
        return dna_dic

 

  def calculate_complement(self):
        complement_dic = {"A":"T","T":"A","G":"C","C":"G"}
        reversed_dna = self.dna_string[::-1]
        complement_dna = ""
        for char in reversed_dna:
            complement_dna= complement_dna + complement_dic[char]
        return DNA(complement_dna)

 

  def count_point_mutations(self,dna):
        hamming_distance = 0
        for i in range(len(self.dna_string)):
            if self.dna_string[i] != dna.get_dna_string()[i]:
                hamming_distance+=1
        return hamming_distance

 

  def find_motif(self, sub_dna):
        result = []
        sub_dna_len = len(sub_dna.get_dna_string())
        dna_len = len(self.dna_string)
        for i in range(0, dna_len - sub_dna_len + 1):
            if self.dna_string[i:i + sub_dna_len] == sub_dna.get_dna_string():
                result.append(i)
        return result

 

 

dna = DNA("ATGCA")
print(dna.count_nucleotides())

 

complement_dna = dna.calculate_complement()
print(complement_dna.get_dna_string())

 

dna_1 = DNA("GAGCC")
dna_2 = DNA("CATCG")
print(dna_1.count_point_mutations(dna_2))

 

dna_3 = DNA("ATAT")
dna_4 = DNA("GATATATGCATATACTT")
print(dna_4.find_motif(dna_3))
