from string import ascii_lowercase

alpha = ascii_lowercase + " "

letter_to_number = dict()

for i in range(len(alpha)):
  letter_to_number[alpha[i]] = i

def vigenere(key, message):
  n = len(key)
  key = [letter_to_number[a] for a in key]
  message = [a for a in message]
  for i in range(len(message)):
    message[i] = alpha[(letter_to_number[message[i]] + key[i % n]) % len(alpha)]
  return("".join(message))

alpha_frequences = [.0745, .0114, .0324, .0367, .1443, .0111, .0123, .0111, .0663, .0034, .0029, .0496, .0262, .0639, .0506, .0249, .0065, .0607, .0651, .0592, .0453, .0111, .0017, .0038, .0046, .0015]

alpha_frequences = [4.8 / 5.8 * f for f in alpha_frequences] + [1 / 5.8]

cypher = "fmfgumwjlmfhrdlmamtidiqimafy dibmakqrduiuknmsjhigmtxmtrvu  fexzxoaos dfsffgpblrfzaougiqhvvydyigyztfy iqqzukdyijxlmfhgdcim gkrdtpvqxdbikxu  mhedxu gdbsimnqurmhrrmhiiyyzdxqfifvvdlmstyetizhvedduimhrifxhimhjmsjvvzvziedtshaxevvvqzvzdndkru dwficiulkdplzj zkqrrjdgwtsmebtbihifmgyzhiszqvdfmfgumwjlmfhrdtimixdcyqmfh xvpzwzhiibidhvvzdpscqzhisztewvvzdpijxzhsiflehzhxiemixzhgm wzdvhrdnrrps kdqiqjlmwyrrtimhiimukmumyxmyddvcgrfexiulkgvwzju  vmpvwuknmsjhigmtxedcshwfeytyewmzmcyvwukktrruehafprdtlcnlvrduiucokrrvvzhgdrxvdjmxgrdfelhrimqrnizftdyiwcmtdsvziyzogudaemqyovdgychgdbyspcmfwndcinpuhrdvruuopyiqloqzdpidxu umjedxzhzvamidymvyvwqgzazimifskbkdvpqruwljdiqtfbydnytyhmfwrgkvcakdvpqimafraqciuioremqeohjmjddiocoiziqwcmiprdvruzkjrvvrxmfegdumjtuqnxvdybfwrmpmzukdemvgfmffyezwzhjimzzkzvkvrdgychrimhvglqzdvrjiazkdndkruknmsjhigmtxmtbymhisztbirmfhnridmwtdfvrmnmfhrwqgbqljdiidjixymiddgqrprdtmhyfgrrjdkbgxdiqzcvmxmwzauwtdfveypmfi dwecafhrnrdovkdzijlilkdqiqgbqljdicihafe ebsabkdqedwubtdpskvnhzvnmjiulkdtmezvvffnxjmmagdoibpv udbehyumtdzmbpzhim uqgzvzdpmduoitxrdjviqy"