
sonlar=['1','2','3','4','5']
ismlar=['iroda','yulduz','muhayyo','marhabo','manzura']
ismlar[1]='shaxnoza'
print(ismlar[0])
print(ismlar[1])
print(ismlar[2])
print(ismlar[3])
print(ismlar[4])
ismlar.append('sherzod')
ismlar.append('gavhar')
ismlar.append('munisa')
ismlar.append('farida')
ismlar.append('sarvar')
#Listga elemnetni index bilan qo'shish
ismlar.insert(1,'alisher')
print(ismlar)
#Listni slice qilish
numbers=[1,2,3,4,5,6,7,8]
print(numbers[2:7])
#Listdagi oxirgi elementni olish
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(len(numbers))
#Listdan elementlarni o'chirish index bilan
oquvchilar=['iroda','yulduz','muhayyo','marhabo','manzura']
del oquvchilar[0]#iroda o'chadi sababi iroda 0-indexda turibdi
del oquvchilar[3]#manzura o'chadi sababi manzura 4=indexda turibdi
del oquvchilar[1]
print(oquvchilar)
#Listni qiymat bilan o'chirish
#oquvchilar.remove('yulduz')
#matrix
g =[[1,2,3],[4,5,6],[7,8,9]]
print(g[0])
print(g[1])
print(g[2])
print(g[1][0])
      



