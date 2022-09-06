import fermat

prime1 = 7
trialLen = 2
#print(fermat.fermat(prime1,trialLen))

# print(fermat.mod_exp(2,21,18))
# print(fermat.mod_exp(6,18,7))
# print(fermat.mod_exp(3,12,97))
# print(fermat.mod_exp(4,70,561))
# print(fermat.mod_exp(4,560,561))
# print(fermat.miller_rabin(561,1))
# print(fermat.fprobability(1))
# print(fermat.mprobability(1))
print(fermat.fermat(561,1))
print(fermat.miller_rabin(561,1))
# print(fermat.mod_exp(4,560,561))
# print(fermat.mod_exp(4,70,561))
# print(fermat.fermat(97,1))
