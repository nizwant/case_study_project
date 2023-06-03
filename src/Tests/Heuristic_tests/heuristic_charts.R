# Reading data ------------------------------------------------------------

library(readr)
heuristic <- read_csv("../Results/results_heuristic.csv")
df <- read_csv("../Results/results_python.csv")

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

# Making the table --------------------------------------------------

library(kableExtra)
library(dplyr)
df %>%
  rename(final_solution = deficit_ratio) %>% 
  left_join(heuristic, by = "Name") %>%
  select(Name, heuristic_solution, best_known_sol) %>% 
  rename(
    "Best known solution length" = "best_known_sol",
    "Heuristic solution length" = "heuristic_solution"
  ) %>%
  mutate(Name = factor(Name, levels = problems_levels)) %>% 
  arrange(Name) %>%
  kable(format = "latex") %>%
  kable_styling(full_width = FALSE) %>%
  writeLines("heuristic_table.tex")
