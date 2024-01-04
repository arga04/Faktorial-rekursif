'''
Dalam ilmu materimatika faktorial dari bilangan bulat positif dari n yang dilambangkan dengan n!, adalah hasil perkalian seluruh bilangan positif mulai dari n s.d 1.
Cth:
0! = 1
1! = 1
2! = 2 * 1 = 2
3! = 3 * 2 = 6
4! = 4 * 6 = 24
5! = 5 * 24 = 120
6! = 6 * 120 = 720
.
.
n! = n * (n-1)!

Buat sebuah fungsi rekursif yang menghitung nilai faktorial sebuah bilangan positif n
'''

n = int(input("Masukkan nilai n : "))


def hit_faktorial(n):
  if n > 2:
    return n * hit_faktorial(n - 1)

  return 2


faktorial = hit_faktorial(n)
print(f"{n}! = {faktorial}")
