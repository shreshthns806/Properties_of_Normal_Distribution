#Importing Modules
import statistics
import pandas
import csv
import plotly.figure_factory
import plotly.graph_objects

data_frame = pandas.read_csv("StudentsPerformance.csv")
reading_scores = (data_frame["reading score"].tolist())

reading_score_standard_deviation = statistics.stdev(reading_scores)
reading_score_mean = statistics.mean(reading_scores)

reading_score_standard_deviation1_start = reading_score_mean - reading_score_standard_deviation
reading_score_standard_deviation1_end = reading_score_mean + reading_score_standard_deviation
reading_score_standard_deviation2_start = reading_score_mean - (reading_score_standard_deviation*2)
reading_score_standard_deviation2_end = reading_score_mean + (reading_score_standard_deviation*2)
reading_score_standard_deviation3_start = reading_score_mean - (reading_score_standard_deviation*3)
reading_score_standard_deviation3_end = reading_score_mean + (reading_score_standard_deviation*3)

data_in_standard_deviation1 = [score for score in reading_scores if score > reading_score_standard_deviation1_start if score < reading_score_standard_deviation1_end]
data_in_standard_deviation2 = [score for score in reading_scores if score > reading_score_standard_deviation2_start if score < reading_score_standard_deviation2_end]
data_in_standard_deviation3 = [score for score in reading_scores if score > reading_score_standard_deviation3_start if score < reading_score_standard_deviation3_end]

percent_of_data_in_standard_deviation1 = (((len(data_in_standard_deviation1))*100)/len(reading_scores))
percent_of_data_in_standard_deviation2 = (((len(data_in_standard_deviation2))*100)/len(reading_scores))
percent_of_data_in_standard_deviation3 = (((len(data_in_standard_deviation3))*100)/len(reading_scores))

figure = plotly.figure_factory.create_distplot([reading_scores],["Reading Scores"], show_hist = False)
figure.add_trace(plotly.graph_objects.Scatter(x = [reading_score_mean,reading_score_mean], y = [0,0.04], mode = "lines", name = "Mean"))
figure.add_trace(plotly.graph_objects.Scatter(x = [reading_score_standard_deviation1_start,reading_score_standard_deviation1_start], y = [0,0.04], mode = "lines", name = "Standard Deviation 1 Start"))
figure.add_trace(plotly.graph_objects.Scatter(x = [reading_score_standard_deviation2_start,reading_score_standard_deviation2_start], y = [0,0.04], mode = "lines", name = "Standard Deviation 2 Start"))
figure.add_trace(plotly.graph_objects.Scatter(x = [reading_score_standard_deviation3_start,reading_score_standard_deviation3_start], y = [0,0.04], mode = "lines", name = "Standard Deviation 3 Start"))
figure.add_trace(plotly.graph_objects.Scatter(x = [reading_score_standard_deviation1_end,reading_score_standard_deviation1_end], y = [0,0.04], mode = "lines", name = "Standard Deviation 1 End"))
figure.add_trace(plotly.graph_objects.Scatter(x = [reading_score_standard_deviation2_end,reading_score_standard_deviation2_end], y = [0,0.04], mode = "lines", name = "Standard Deviation 2 End"))
figure.add_trace(plotly.graph_objects.Scatter(x = [reading_score_standard_deviation3_end,reading_score_standard_deviation3_end], y = [0,0.04], mode = "lines", name = "Standard Deviation 3 End"))

figure.show()