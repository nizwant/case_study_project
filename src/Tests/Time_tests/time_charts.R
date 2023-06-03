

# Reading data ------------------------------------------------------------

library(readr)
df <- read_csv("dataframe_cleared.csv")
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
  mutate(Name = factor(Name, levels = problems_levels)) %>%
  rename(
    "0.25 min" = "0.25_min",
    "0.5 min" = "0.5_min",
    "1 min" = "1_min",
    "1.5 min" = "1.5_min",
    "2 min" = "2_min",
    "2.5 min" = "2.5_min",
    "3 min" = "3_min",
    "50%" = "50_%",
    "30%" = "30_%",
    "20%" = "20_%",
    "15%" = "15_%",
    "10%" = "10_%",
    "5%" = "5_%",
    "3%" = "3_%",
    "2%" = "2_%",
    "1%" = "1_%"
  )


# Making the first table --------------------------------------------------
library(kableExtra)

df %>%
  select("Name",
         "0.25 min",
         "0.5 min",
         "1 min",
         "1.5 min",
         "2 min",
         "2.5 min",
         "3 min") %>%
  arrange(Name) %>%
  kable(format = "latex") %>%
  kable_styling(full_width = FALSE) %>%
  writeLines("table_time.tex")


# Making the second table -------------------------------------------------

df %>%
  select("Name",
         "50%", "30%", "20%", "15%", "10%", "5%", "3%", "2%", "1%") %>%
  arrange(Name) %>%
  kable(format = "latex", digits = 3) %>%
  kable_styling(full_width = FALSE) %>%
  writeLines("table_deficit_ratio.tex")


# Making the first plot ---------------------------------------------------

library(tidyr)
library(ggplot2)
library(scales)
palette <-
  c(
    "#F1BB7B",
    "#f6a86d",
    "#fa9365",
    "#fc7d63",
    "#FD6467",
    "#d25051",
    "#a83e3c",
    "#812b29",
    "#5B1A18")
    
 plot1 <- df %>%
      select("Name",
             "50%", "30%", "20%", "15%", "10%", "5%", "3%", "2%", "1%") %>%
      pivot_longer(
        cols = c("50%", "30%", "20%", "15%", "10%", "5%", "3%", "2%", "1%"),
        names_to = "Deficit_ratio",
        values_to = "Time"
      ) %>%
      mutate(Deficit_ratio = factor(
        Deficit_ratio,
        levels = c( "1%", "2%", "3%", "5%", "10%", "15%", "20%", "30%", "50%")
      )
      ) %>%
      filter(!is.na(Deficit_ratio)) %>% 
      ggplot(aes(
        x = Name, y = Time, color = Deficit_ratio
      )) +
      geom_point(size = 7) +
      scale_y_continuous(trans=scales::pseudo_log_trans(base = 15),
                         breaks = c(0, 1, 2, 4, 8, 15, 30, 60, 120, 180)) +
      #scale_y_log10(labels = function(x) format(x, scientific = FALSE)) +
    labs(
        title = "How long does it take to reach certain best solution deficit ratio?",
        y = "Time in seconds",
        x = "Problem name",
        color = "Best solution deficit ratio"
      ) +
      scale_color_manual(values = palette) +
      theme_minimal() +
      theme(legend.position = c(.15, 0.65),
            legend.text = element_text(size = 10),
            plot.title = element_text(size = 14, face = "bold"),
            axis.text = element_text(color = "black"))
 
 ggsave("time_plot1.png", plot1, width = 25, height = 15, units = "cm", bg = "white")


# Making the second plot --------------------------------------------------

plot2 <- df %>%
  select("Name",
         "best_known_sol",
         "0.25 min",
         "0.5 min",
         "1 min",
         "1.5 min",
         "2 min",
         "2.5 min",
         "3 min") %>%
  pivot_longer(
    cols = c("0.25 min",
             "0.5 min",
             "1 min",
             "1.5 min",
             "2 min",
             "2.5 min",
             "3 min"),
    names_to = "Time",
    values_to = "Deficit_ratio"
  )%>%
  mutate(Deficit_ratio = 100 * (Deficit_ratio - best_known_sol)/best_known_sol,
         Time = factor(Time, levels = c("0.25 min",
                                        "0.5 min",
                                        "1 min",
                                        "1.5 min",
                                        "2 min",
                                        "2.5 min",
                                        "3 min"))) %>%
  select(-best_known_sol) %>% 
  arrange(desc(Time)) %>% 
  ggplot(aes(
    x = Name, y = Deficit_ratio, color = Time
  )) +
  geom_point(size = 7,position = "identity") +
  scale_y_continuous(trans=scales::pseudo_log_trans(base = 10),
                     breaks = c(0, 1, 3, 10, 30)) +
  # scale_y_log10(labels = function(x) format(x, scientific = FALSE)) +
  labs(
    title = "Best solution deficit ratio after certain amount of time",
    y = "Best solution deficit ratio (in percent)",
    x = "Problem name",
    color = "Time"
  ) +
  scale_color_manual(values = palette) +
  theme_minimal() +
  theme(legend.position = c(.15, 0.75),#legend.position = c(.85, 0.3),
        legend.text = element_text(size = 10),
        plot.title = element_text(size = 14, face = "bold"),
        axis.text = element_text(color = "black"))

ggsave("time_plot2.png", plot2, width = 25, height = 15, units = "cm", bg = "white")
