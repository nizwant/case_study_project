# Reading data ------------------------------------------------------------

library(readr)
df <- read_csv("../Results/results_cython.csv")

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
    "Our solution length" = "our_solution",
    "Best solution deficit ratio (in percent)" = "deficit_ratio"
  ) %>%
  kable(format = "latex") %>%
  kable_styling(full_width = FALSE) %>%
  writeLines("cython_table.tex")


# Calculating statistics --------------------------------------------------

summary(df$deficit_ratio)


# Making the plot ---------------------------------------------------------

df_python <- read_csv("../Results/Marta_results.csv") %>%
  mutate(python_solution = deficit_ratio/100) %>%
  select(Name, python_solution)

library(ggplot2)
library(tidyr)
library(wesanderson)

palette <- wes_palette("GrandBudapest1", 2)

plot <- 
df %>%
  rename("cython_solution" = "deficit_ratio") %>%
  left_join(df_python, by = "Name") %>%
  mutate(cython_solution = cython_solution / 100) %>%
  select(Name, cython_solution, python_solution) %>%
  mutate(Name = factor(Name, levels = rev(problems_levels))) %>%
  ggplot() +
  geom_segment(aes(
    x = Name,
    xend = Name,
    y = python_solution,
    yend = cython_solution
  )) +
  geom_point(aes(x = Name, y = python_solution, color = "python_solution"),
             size = 7) +
  geom_point(aes(x = Name, y = cython_solution, color = "cython_solution"),
             size = 7) +
  scale_color_manual(
    values = rev(palette),
    labels = c("python_solution" = "Python solution", "cython_solution" = "Cython solution"),
    guide = guide_legend(reverse = TRUE),
    name = "Type of solution"
  ) +
  scale_y_continuous(labels = scales::percent, breaks = seq(0, 0.4, 0.05)) +
  coord_flip() +
  labs(
    title = "Comparison of best solution deficit ratio between Python and Cython solutions",
    y = "Best solution deficit ratio",
    x = "Problem name",
    color = "Type of solution"
  ) +
  theme_minimal() +
  theme(
    legend.position = c(.75, 0.75),
    legend.text = element_text(size = 10),
    plot.title = element_text(size = 14, face = "bold"),
    axis.text = element_text(color = "black"),
    panel.grid.major = element_line(color = "gray", linetype = "dashed")
  )

ggsave("cython_plot.png", plot, width = 25, height = 15, units = "cm", bg = "white")

