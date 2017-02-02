input <- file('stdin','r')
s <- readLines(input,n=1)
length(s)
x <- strsplit(s,split='[|]')
y <- strsplit(x[[1]][1],split='[,]')[[1]]
cat(y)

