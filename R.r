#вывести индексы дублей
a <- c(1,1,2,3,2,2,4,2,2,2)
print(which(duplicated(a, a ==2)))

#всплески
x1 <- c(1,5,3,6,23,6,4)
print(x1)
x1 <- replace(x1, x1 == (x1[x1 > mean(x1)*3]), (mean(x1)))
print(x1)

#матрица
A <- matrix(seq(3,8), nrow = 3, ncol = 3)
print(A)
indx1=(which(A == (min(A))))%%(nrow(A))
indx1 <- replace(indx1, indx1 == 0, ncol(A))
indx2=(((which(A == (min(A))))-indx1)/nrow(A))+1
print(indx1) #строки
print(indx2) #столбцы