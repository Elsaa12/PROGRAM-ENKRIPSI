"""
PDA 4 - LARIK (ARRAY)
Nama : Elsa Aiziyah
NIM  : 21305144025
Kelas: Matematika E
"""
print('='*50)
print('PROGRAM ENKRIPSI'.center(50))
print('='*50)
def sandikan(kata, kunci = 1):
    huruf = [chr (i) for i in range (97,123)]
    result= ''
    kata= kata.lower()
    for char in kata:
        if char in huruf:
            result += huruf[(huruf.index(char) + kunci) % 26]
        else:
            result += char 
    return result  
print(sandikan("aku dan kamu"))
print(sandikan("apakah anya suka pergi ke sekolah?",3))
#----------------CONTOH LAIN------------------#
print('-'*50)
print('>>>>> Contoh Lain <<<<<'.center(50))
print('-'*50)
print(sandikan("budi suka makan sate."))
print(sandikan("anya suka kacang, kue, dan sirup."))
print(sandikan("Ani suka makan mie."))
print("="*50)
print(sandikan("halo namaku nobita",4))
print(sandikan("siapa namamu?",6))
print(sandikan("Ani suka minum susu",10))
print("="*50)
