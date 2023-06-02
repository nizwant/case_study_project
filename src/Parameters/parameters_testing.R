library(dplyr)
library(tidyverse)
library(ggplot2)
library(wesanderson)

grid5 <-  read.csv2(file = "grid_search_5.csv", sep = ",", dec = ".")
grid6 <-  read.csv2(file = "grid_search_6.csv", sep = ",", dec = ".")
grid4 <-  read.csv2(file = "grid_search_4.csv", sep = ",", dec = ".")
grid3 <-  read.csv2(file = "grid_search_3.csv", sep = ",", dec = ".")
grid2 <-  read.csv2(file = "grid_search_3_prev2.csv", sep = ",", dec = ".")

df <- bind_rows(grid2, grid3, grid4, grid5, grid6)


params <- unique(df$Parametr.changed)
df$Worse.Rate <-  abs(df$Worse.Rate)
bigproblems <- c('rbg323','rbg358','rbg403','rbg443','kro124p', 'ftv170', 'ftv64')
medium_problems <- c('ftv64', 'ftv55', 'ft53', 'ft70', 'ftv70')
small_problems <- c('p43', 'ry48p', 'ftv44', 'ftv33',  'ftv38',  'ftv35', 'br17',  'ftv47')

df['problem_size'] <- if_else(df$Problem %in% bigproblems,'[100, Inf)',
                              if_else(df$Problem %in% small_problems, '(0, 50]','(50, 100)'))


#size impact
ggplot(df, aes(Worse.Rate))+
  geom_density( aes(fill=problem_size, alpha = 0.5 ))+
  scale_fill_manual(values=wes_palette("GrandBudapest1"))+
  theme_minimal()+
  xlim(c(0,40))+
  labs(x = 'Best solution deficit ratio in percent', y='Density', title = "Best solution deficit ratio in percent", fill= "Problem size:")+
  guides(alpha = FALSE, problem_size = TRUE)


parametrs_to_plot <- data.frame()

### Parametrs impact

for (p in params) {
  df %>% 
    group_by(df[p]) %>% 
    summarise(Mean_Worse_Rate = mean(Worse.Rate)) -> df2
    df2 <- pivot_longer(df2, p, names_to = 'Parametr_Changed', values_to = 'Parametr_Value')
    parametrs_to_plot <-  bind_rows(parametrs_to_plot, df2)
     #print(cor(df3[p], df$Worse.Rate))
}


params <- df$'Parametr.changed'

params_to_plot <-  data.frame()
for (i in 1:length(params)) {
  df2 <- df[i,c('Worse.Rate','Parametr.changed',params[i])]
  colnames(df2) <- c("Worse_Rate", 'Parameter_changed', 'Parameter_value')
  params_to_plot <- bind_rows(params_to_plot, df2)
}

pal <- wes_palette(name = "GrandBudapest1", 3, type = 'discrete')

ggplot(params_to_plot, aes( x=Parameter_value, y=Worse_Rate, group = Parameter_value))+

  #geom_segment(size = 1, aes(xend=Parametr_Value, yend=0), color = pal[3])+
  #geom_point(size = 4, color = pal[1])+
  geom_boxplot(width = 0.4)+
  ylim(c(0, 40 ))+
  coord_flip()+
  labs(y= 'Best solution deficit ratio in percent', x='Parameters Values', title = "Results distribution of tested parameters values")+
  theme_bw()+
  facet_wrap(~Parameter_changed, scales = "free_y")



#other stats and plots

df3 <- df[df$Problem %in% bigproblems,]

min_stats<- df %>% 
  group_by(Problem) %>% 
  summarise(mean_worse_rate = mean(Worse.Rate), best_score = min(Worse.Rate))


best_solutions<- inner_join(df, min_stats, by = c('Problem' = 'Problem', 'Worse.Rate' = 'best_score') )
mean(df$Worse.Rate)

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


