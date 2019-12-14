#вывести индексы дублей
a <- c(1,1,2,3,2,2,4,2,2,2)
print(which(duplicated(a, a ==2)))