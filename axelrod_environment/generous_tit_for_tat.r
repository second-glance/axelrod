axelrod = function(p, o) {
    if(length(p) == 0) {
        return(TRUE)
    } else {
        ifelse(tail(o, 1), T, sample(c(T, F), 1, p = 1:2)) 
    }
}

