csv_files <- list.files(pattern = "\\.csv$")

for (file in csv_files) {
  file_name <- gsub("\\.csv", "", file)
  assign(paste0("df_", file_name), read.csv(file))
}

list_of_data_frames <- list(df_ftv35_1, df_ftv35_2, df_ftv35_3, df_ftv35_4, df_ftv35_5, df_ftv35_6, df_ftv35_7, df_ftv35_8, df_ftv35_9, df_ftv35_10, df_ftv35_11, df_ftv35_12, df_ftv35_13, df_ftv35_14, df_ftv35_15)
library(dplyr)

full_join_multiple <- function(data_frames) {
  
  result <- data_frames[[1]]
  
  for (i in 2:length(data_frames)) {
    result <- full_join(result, data_frames[[i]], by = "time")
  }
  
  return(result)
}

df_ftv35 <- full_join_multiple(list_of_data_frames)
df_ftv35 <- df_ftv35 %>% arrange(time)
df_ftv35$time <- format(df_ftv35$time, scientific = FALSE)

#write.csv(df_ftv35, file = "ftv35_df.csv", row.names = FALSE)
df_ftv35_final <- read.csv('ftv35_df.csv')

new_names <- c("best_sol_1", "best_sol_2", "best_sol_3","best_sol_4","best_sol_5","best_sol_6","best_sol_7", "best_sol_8", "best_sol_9", "best_sol_10", "best_sol_11", "best_sol_12", "best_sol_13", "best_sol_14", "best_sol_15")  
colnames(df_ftv35_final)[c(1,3,4,5,6,7,8,9,10,11,12,13,14,15,16)] <- new_names  

new_order <- c("time","best_sol_1", "best_sol_2", "best_sol_3","best_sol_4","best_sol_5","best_sol_6","best_sol_7", "best_sol_8", "best_sol_9", "best_sol_10", "best_sol_11", "best_sol_12", "best_sol_13", "best_sol_14", "best_sol_15")  
df_ftv35_final <- df_ftv35_final[new_order]

cols_to_mean <- df_ftv35_final[, 2:15]
cols_to_mean[cols_to_mean == 0] <- NA

df_ftv35_final$mean_column <- rowMeans(cols_to_mean, na.rm = TRUE)

df_ftv35_final$mean_log <- log(log(df_ftv35_final$mean_column))
ggplot(df_ftv35_final, aes(x = time, y = mean_log)) +
  geom_line(size = 0.6) +
  scale_y_log10() +
  labs(x = "Time (s)", y = "Best solution length", title = "Small problem") +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    plot.margin = margin(20, 20, 20, 20)
  ) 


slibrary(caret)


# Using the scale() function
df <- df_ftv35_final
column <- df$mean_column
scaled_column <- (column - min(column)) / (max(column) - min(column))
df$column_scaled <- scaled_column



ggplot(df, aes(x = time, y = column_scaled)) +
  geom_line(size = 0.6) +
  labs(x = "Time (s)", y = "Best solution length", title = "Small problem") +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    plot.margin = margin(20, 20, 20, 20)
  ) +
  scale_y_log10()
# Using the preProcess() function

