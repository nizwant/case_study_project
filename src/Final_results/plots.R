library(ggplot2)
library(dplyr)
library(scales)

###### SMALL PROBLEM #####
### reading data----------------------------------------------------------------
# directory <- "Small_dfs_for_plots"
# 
# dataframes <- list()
# 
# for (i in 1:15) {
#   file_path <- paste0(directory, "/ftv35_", i, ".csv")
#   
#   df_name <- paste0("df_ftv35_", i)
#   assign(df_name, read.csv(file_path))
#   
#   dataframes[[i]] <- get(df_name)
# }

### joining data----------------------------------------------------------------
# list_of_data_frames <- list(df_ftv35_1, df_ftv35_2, df_ftv35_3, df_ftv35_4, df_ftv35_5, df_ftv35_6, df_ftv35_7, df_ftv35_8, df_ftv35_9, df_ftv35_10, df_ftv35_11, df_ftv35_12, df_ftv35_13, df_ftv35_14, df_ftv35_15)
# 
# 
# full_join_multiple <- function(data_frames) {
#   result <- data_frames[[1]]
#   for (i in 2:length(data_frames)) {
#     result <- full_join(result, data_frames[[i]], by = "time")
#   }
#   return(result)
# }
# 
# df_ftv35 <- full_join_multiple(list_of_data_frames)
# df_ftv35 <- df_ftv35 %>% arrange(time)
# df_ftv35$time <- format(df_ftv35$time, scientific = FALSE)
# write.csv(df_ftv35, file = "ftv35_df.csv", row.names = FALSE)

### final data for small problem------------------------------------------------
df_ftv35_final <- read.csv('ftv35_df.csv')

#formating the data-------------------------------------------------------------
new_names <- c("best_sol_1", "best_sol_2", "best_sol_3","best_sol_4","best_sol_5","best_sol_6","best_sol_7", "best_sol_8", "best_sol_9", "best_sol_10", "best_sol_11", "best_sol_12", "best_sol_13", "best_sol_14", "best_sol_15")  
colnames(df_ftv35_final)[c(1,3,4,5,6,7,8,9,10,11,12,13,14,15,16)] <- new_names  

new_order <- c("time","best_sol_1", "best_sol_2", "best_sol_3","best_sol_4","best_sol_5","best_sol_6","best_sol_7", "best_sol_8", "best_sol_9", "best_sol_10", "best_sol_11", "best_sol_12", "best_sol_13", "best_sol_14", "best_sol_15")  
df_ftv35_final <- df_ftv35_final[new_order]

#mean count---------------------------------------------------------------------
cols_to_mean <- df_ftv35_final[, 2:15]
cols_to_mean[cols_to_mean == 0] <- NA

df_ftv35_final$mean_column <- rowMeans(cols_to_mean, na.rm = TRUE)

#scalling-----------------------------------------------------------------------
df_small <- df_ftv35_final
column <- df_small$mean_column
scaled_column <- (column - min(column)) / (max(column) - min(column))
df_small$column_scaled <- scaled_column

#plot---------------------------------------------------------------------------
ggplot(df_small, aes(x = time, y = column_scaled)) +
  scale_y_log10(labels = comma_format()) +
  scale_y_reverse() + 
  geom_point(size=1) +
  geom_line(aes(x=time, y=column_scaled), size=0.7, colour='red') +
  labs(x = "Time (s)", y = "Best solution length", title = "Small problem") +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    plot.margin = margin(20, 20, 20, 20)
  )


###### MEDIUM PROBLEM #####
### reading data----------------------------------------------------------------
# directory <- "Medium_dfs_for_plots"

# dataframes <- list()

# for (i in 1:15) {
#   file_path <- paste0(directory, "/ft70_", i, ".csv")
#   
#   df_name <- paste0("df_ft70_", i)
#   assign(df_name, read.csv(file_path))
#   
#   dataframes[[i]] <- get(df_name)
# }

### joining data----------------------------------------------------------------
# list_of_data_frames <- list(df_ft70_1, df_ft70_2, df_ft70_3, df_ft70_4, df_ft70_5, df_ft70_6, df_ft70_7, df_ft70_8, df_ft70_9, df_ft70_10, df_ft70_11, df_ft70_12, df_ft70_13, df_ft70_14, df_ft70_15)
# full_join_multiple <- function(data_frames) {
#   result <- data_frames[[1]]
#   for (i in 2:length(data_frames)) {
#     result <- full_join(result, data_frames[[i]], by = "time")
#   }
#   return(result)
# }
# 
# df_ft70 <- full_join_multiple(list_of_data_frames)
# df_ft70 <- df_ft70 %>% arrange(time)
# df_ft70$time <- format(df_ft70$time, scientific = FALSE)

### write.csv(df_ft70, file = "ft70_df.csv", row.names = FALSE)

### final data for medium problem-----------------------------------------------
df_ft70_final <- read.csv('ft70_df.csv')

#formating the data-------------------------------------------------------------
new_names <- c("best_sol_1", "best_sol_2", "best_sol_3","best_sol_4","best_sol_5","best_sol_6","best_sol_7", "best_sol_8", "best_sol_9", "best_sol_10", "best_sol_11", "best_sol_12", "best_sol_13", "best_sol_14", "best_sol_15")  
colnames(df_ft70_final)[c(1,3,4,5,6,7,8,9,10,11,12,13,14,15,16)] <- new_names  

new_order <- c("time","best_sol_1", "best_sol_2", "best_sol_3","best_sol_4","best_sol_5","best_sol_6","best_sol_7", "best_sol_8", "best_sol_9", "best_sol_10", "best_sol_11", "best_sol_12", "best_sol_13", "best_sol_14", "best_sol_15")  
df_ft70_final <- df_ft70_final[new_order]

#mean count---------------------------------------------------------------------
cols_to_mean <- df_ft70_final[, 2:15]
cols_to_mean[cols_to_mean == 0] <- NA

df_ft70_final$mean_column <- rowMeans(cols_to_mean, na.rm = TRUE)

#scalling-----------------------------------------------------------------------
df_medium <- df_ft70_final
column <- df_medium$mean_column
scaled_column <- (column - min(column)) / (max(column) - min(column))
df_medium$column_scaled <- scaled_column

#plot---------------------------------------------------------------------------
ggplot(df_medium, aes(x = time, y = column_scaled)) +
  scale_y_log10(labels = comma_format())+
  geom_point(size=1) +
  geom_line(aes(x=time, y=column_scaled), size=0.7, colour='red') +
  labs(x = "Time (s)", y = "Best solution length", title = "Medium problem") +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    plot.margin = margin(20, 20, 20, 20)
  )


###### BIG PROBLEM #####
### reading data----------------------------------------------------------------
# directory <- "Big_dfs_for_plots"
# 
# dataframes <- list()
# 
# for (i in 1:15) {
#   file_path <- paste0(directory, "/rbg358_", i, ".csv")
#   
#   df_name <- paste0("df_rbg358_", i)
#   assign(df_name, read.csv(file_path))
#   
#   dataframes[[i]] <- get(df_name)
# }

### joining data----------------------------------------------------------------
# list_of_data_frames <- list(df_rbg358_1, df_rbg358_2, df_rbg358_3, df_rbg358_4, df_rbg358_5, df_rbg358_6, df_rbg358_7, df_rbg358_8, df_rbg358_9, df_rbg358_10, df_rbg358_11, df_rbg358_12, df_rbg358_13, df_rbg358_14, df_rbg358_15)
# full_join_multiple <- function(data_frames) {
#   result <- data_frames[[1]]
#   for (i in 2:length(data_frames)) {
#     result <- full_join(result, data_frames[[i]], by = "time")
#   }
#   return(result)
# }
# 
# df_rbg358 <- full_join_multiple(list_of_data_frames)
# df_rbg358 <- df_rbg358 %>% arrange(time)
# df_rbg358$time <- format(df_rbg358$time, scientific = FALSE)

#write.csv(df_rbg358, file = "rbg358_df.csv", row.names = FALSE)

### final data for medium problem-----------------------------------------------
df_rbg358_final <- read.csv('rbg358_df.csv')

#formating the data-------------------------------------------------------------
new_names <- c("best_sol_1", "best_sol_2", "best_sol_3","best_sol_4","best_sol_5","best_sol_6","best_sol_7", "best_sol_8", "best_sol_9", "best_sol_10", "best_sol_11", "best_sol_12", "best_sol_13", "best_sol_14", "best_sol_15")  
colnames(df_rbg358_final)[c(1,3,4,5,6,7,8,9,10,11,12,13,14,15,16)] <- new_names  

new_order <- c("time","best_sol_1", "best_sol_2", "best_sol_3","best_sol_4","best_sol_5","best_sol_6","best_sol_7", "best_sol_8", "best_sol_9", "best_sol_10", "best_sol_11", "best_sol_12", "best_sol_13", "best_sol_14", "best_sol_15")  
df_rbg358_final <- df_rbg358_final[new_order]

#mean count---------------------------------------------------------------------
cols_to_mean <- df_rbg358_final[, 2:15]
cols_to_mean[cols_to_mean == 0] <- NA

df_rbg358_final$mean_column <- rowMeans(cols_to_mean, na.rm = TRUE)

#scalling-----------------------------------------------------------------------
df_big <- df_rbg358_final
column <- df_big$mean_column
scaled_column <- (column - min(column)) / (max(column) - min(column))
df_big$column_scaled <- scaled_column

#plot---------------------------------------------------------------------------
ggplot(df_big, aes(x = time, y = column_scaled)) +
  scale_y_log10(labels = comma_format())+
  geom_point(size=1) +
  geom_line(aes(x=time, y=column_scaled), size=0.7, colour='red') +
  labs(x = "Time (s)", y = "Best solution length", title = "Big problem") +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    plot.margin = margin(20, 20, 20, 20)
  )



##### marta's results into tex #####
library(readr)
df <- read_csv("../Tests/Results/Marta_results.csv")
View(df)
df <- df[,-1]

colnames(df) <- c("Name", "Best known solution","Our best known solution", "Deificit ratio")

library(kableExtra)

problems_levels = c(
  "br17",
  "ftv33",
  "ftv35",
  "ftv38",
  "p43",
  "ftv44",
  "ftv47",
  "ry48p",
  "ft53",
  "ftv55",
  "ftv64",
  "ft70",
  "ftv70",
  "kro124p",
  "ftv170",
  "rbg323",
  "rbg358",
  "rbg403",
  "rbg443"
)
library(dplyr)

df %>%
  mutate(Name = factor(Name, levels = problems_levels)) %>% 
  arrange(Name) %>%
  kable(format = "latex") %>%
  kable_styling(full_width = FALSE) %>%
  writeLines("our_results.tex")

