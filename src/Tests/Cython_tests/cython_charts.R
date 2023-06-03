# Reading data ------------------------------------------------------------

library(readr)
df <- read_csv("results_cython.csv")
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
  rename("Best known solution length" = "best_known_sol",
         "Our solution length" = "our_solution",
         "Best solution deficit ratio (in percent)" = "deficit_ratio") %>% 
  kable(format = "latex") %>%
  kable_styling(full_width = FALSE) %>%
  writeLines("cython_table.tex")


# Calculating statistics --------------------------------------------------

summary(df$deficit_ratio)

