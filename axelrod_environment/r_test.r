s <- 'T,T,F|F,T,F'
x <- strsplit(s,split='[|]')
strsplit(x[[1]][2],split='[,]')[[1]]
x
