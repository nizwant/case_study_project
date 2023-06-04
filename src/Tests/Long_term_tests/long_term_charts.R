# Reading data ------------------------------------------------------------

library(readr)
df <- read_csv("../Results/long_term_results.csv")
View(df)

# Preprocessing -------------------------------------------------------

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
df <- df %>%
  select(-ID) %>%
  mutate(Name = factor(Name, levels = problems_levels))

# Making the table --------------------------------------------------
library(kableExtra)

df %>%
  arrange(Name) %>%
  rename(
    "Best known solution length" = "best_known_sol",
    "30 min solution length" = "our_solution",
    "Best solution deficit ratio (in percent)" = "deficit_ratio"
  ) %>%
  kable(format = "latex") %>%
  kable_styling(full_width = FALSE) %>%
  writeLines("long_term_table.tex")


# Calculating statistics --------------------------------------------------

summary(df$deficit_ratio)


# Making the plot ---------------------------------------------------------

df_python <- read_csv("../Results/Marta_results.csv") %>%
  mutate(short_solution = deficit_ratio/100) %>%
  select(Name, short_solution)

library(ggplot2)
library(tidyr)
library(wesanderson)

palette <- wes_palette("GrandBudapest1", 2)

plot <- 
  df %>%
  mutate(long_solution = deficit_ratio / 100) %>%
  left_join(df_python, by = "Name") %>%
  select(Name, short_solution, long_solution) %>%
  mutate(Name = factor(Name, levels = rev(problems_levels))) %>%
  ggplot() +
  geom_segment(aes(
    x = Name,
    xend = Name,
    y = short_solution,
    yend = long_solution
  )) +
  geom_point(aes(x = Name, y = long_solution, color = "long_solution"),
             size = 7) +
  geom_point(aes(x = Name, y = short_solution, color = "short_solution"),
             size = 7) +
  scale_color_manual(
    values = rev(palette),
    labels = c("short_solution" = "5 min (multiple runs)","long_solution" = "30 min (one run)"),
    guide = guide_legend(reverse = TRUE),
    name = "Execution time of the algorithm"
  ) +
  scale_y_continuous(labels = scales::percent, breaks = seq(0, 0.4, 0.05)) +
  coord_flip() +
  labs(
    title = "Comparison of best solution deficit ratio after 5 and 30 minutes",
    y = "Best solution deficit ratio",
    x = "Problem name",
    color = "Execution time of the algorithm"
  ) +
  theme_minimal() +
  theme(
    legend.position = c(.75, 0.75),
    legend.text = element_text(size = 10),
    plot.title = element_text(size = 14, face = "bold"),
    axis.text = element_text(color = "black"),
    panel.grid.major = element_line(color = "gray", linetype = "dashed")
  )

ggsave("long_term_plot.png", plot, width = 25, height = 15, units = "cm", bg = "white")

