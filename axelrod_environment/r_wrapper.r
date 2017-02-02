#!/usr/bin/Rscript

# This script manage call to R functions in the Axelrod Reloaded competition
# Structure to call this wrapper:
# Rscript r_wrapper.r <function name> [true | false]* [true | false]*
# The answer from the function is returned as stdout


# Get function to call
# Assumes that it is located in the file provided as the first argument and that it contains a function named axelrod
fun_to_call <- commandArgs(trailingOnly = T)[1]
source(fun_to_call)

# Function to split input from stdin
splitstdin <- function(stdinstr)
{
  if(stdinstr != '|')
  {
  split1 <- strsplit(stdinstr,split = '[|]')
  dec1 <-sapply(strsplit(split1[[1]][1],split = '[,]')[[1]],function(x){if(x=='true'){T}else{F}},USE.NAMES = F)
  dec2 <-sapply(strsplit(split1[[1]][2],split = '[,]')[[1]],function(x){if(x=='true'){T}else{F}},USE.NAMES = F)  
  }else{
  dec1 <- dec2 <- logical(0)
  }
  return(list(dec1,dec2))
}






while(T) {
  input <-file('stdin','r')
  line <- readLines(input,n=1)
  previous <- splitstdin(line)
  selfdec <- previous[[1]]
  otherdec <- previous[[2]]
  if(axelrod(selfdec,otherdec))
  {
    write('T',stdout())
  }else
  {
    write('F',stdout())
  }
}




