library(dplyr)
library(tidyverse)
library(ggplot2)

df <-  read.csv2(file = "grid_search_5.csv", sep = ",", dec = ".")
params <- unique(df$Parametr.changed)
df$Worse.Rate <-  -1*df$Worse.Rate
hist(df$Worse.Rate)
bigproblems <- c('rbg323','rbg358','rbg403','rbg443','kro124p', 'ftv170', 'ftv64')
df3 <- df[df$Problem %in% problems,]

for (p in params) {
  df %>% 
    group_by(df[p]) %>% 
    summarise(mean(Worse.Rate)) -> df2
  print(df2)
  #print(cor(df3[p], df$Worse.Rate))
}

min_stats<- df %>% 
  group_by(Problem) %>% 
  summarise(mean_worse_rate = mean(Worse.Rate), best_score = min(Worse.Rate))


best_solutions<- inner_join(df, min_stats, by = c('Problem' = 'Problem', 'Worse.Rate' = 'best_score') )

best_solutions %>% 
  filter(Worse.Rate > 15)


?drop.scope

df %>% 
  group_by(Problem) %>% 
  summary(min(Worse.Rate))


df3 %>% 
  group_by(Parametr.changed) %>% 
  summarise() 


cormatrix<- cor(df[c(5:17, 3)])
cormatrix<- data.frame(cormatrix)
cormatrix[is.na(cormatrix)] <- 0
heatmap(cormatrix)




plot(df3$probability_of_shuffle, df3$Worse.Rate)
plot(df3$probability_of_heuristic, df3$Worse.Rate)
plot(df3$a, df3$Worse.Rate)
plot(df3$b, df3$Worse.Rate)
plot(df3$swap_states_probability, df3$Worse.Rate)
plot(df3$closeness, df3$Worse.Rate)
plot(df3$cooling_rate, df3$Worse.Rate)


