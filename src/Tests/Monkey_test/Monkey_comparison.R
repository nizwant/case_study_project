# Reading data ------------------------------------------------------------

library(readr)
df <- read.csv("Monkey_comparision.csv")
df$Worse.Rate.Monkey <- 0.01*df$Worse.Rate.Monkey
df$Wore.rate.PT <-  0.01*df$Wore.rate.PT


# Making the plot ---------------------------------------------------------
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
library(ggplot2)
library(tidyr)
library(wesanderson)

palette <- wes_palette("GrandBudapest1", 2)

my_plot <-  df %>% 
  mutate(probleem = factor(probleem, levels = rev(problems_levels))) %>% 
  ggplot() +
  geom_segment(aes(
    x = probleem,
    xend = probleem,
    y = Wore.rate.PT,
    yend = Worse.Rate.Monkey
  ))+
  geom_point(aes(x = probleem, y = Wore.rate.PT, color = "Wore.rate.PT"),
             size = 7) +
  geom_point(aes(x = probleem, y = Worse.Rate.Monkey, color = "Worse.Rate.Monkey"),
             size = 7)+
  scale_color_manual(
    values = rev(palette),
    labels = c("Wore.rate.PT" = "PT_SA", "Worse.Rate.Monkey" = "Monkey"),
    guide = guide_legend(reverse = TRUE),
    name = "Type of algorithm"
  )+
  scale_y_continuous(labels = scales::percent, breaks = seq(0, 0.85, 0.1)) +
  coord_flip() +
  labs(
    title = "Comparison of best solution deficit ratio between PT_SA and Monkey algorithm",
    y = "Best solution deficit ratio",
    x = "Problem name",
    color = "Type of algorithm"
  )+
  theme_minimal() +
  theme(
    legend.position = c(.75, 0.75),
    legend.text = element_text(size = 10),
    plot.title = element_text(size = 14, face = "bold"),
    axis.text = element_text(color = "black"),
    panel.grid.major = element_line(color = "gray", linetype = "dashed")
  )

my_plot

ggsave("monkey_plot.png", my_plot, width = 25, height = 15, units = "cm", bg = "white")
