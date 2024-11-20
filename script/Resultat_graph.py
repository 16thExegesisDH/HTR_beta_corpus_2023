import pandas as pd
import plotly.express as px

# Path to the CSV file
file_path = "../corpus/updated_files_control.csv"

# Load the CSV file
data = pd.read_csv(file_path)

# Columns to analyze
columns_to_analyze = [
    "Presegmented",
    "SGM Manually Corrected",
    "SGM GitHub Corrected",
    "Transcript",
    "Transcript Manually Corrected"
]

# Initialize a results dictionary
advancement_results = {}

# Calculate advancement for each repository and each column
for repository, group in data.groupby("Repository"):
    repository_results = {}
    for column in columns_to_analyze:
        count_y = group[column].str.upper().value_counts().get("Y", 0)
        count_n = group[column].str.upper().value_counts().get("N", 0)
        total = count_y + count_n
        if total > 0:
            percentage_accomplished = (count_y / total) * 100
        else:
            percentage_accomplished = 0  # Avoid division by zero
        repository_results[column] = percentage_accomplished
    advancement_results[repository] = repository_results

# Convert results to a DataFrame
advancement_df = pd.DataFrame.from_dict(advancement_results, orient="index")

# Convert the DataFrame to long format for Plotly
advancement_df_reset = advancement_df.reset_index()
advancement_df_long = advancement_df_reset.melt(id_vars=["index"], value_vars=columns_to_analyze, 
                                                var_name="Column", value_name="Percentage Accomplished")
advancement_df_long.rename(columns={"index": "Repository"}, inplace=True)

# Create a Plotly bar chart
fig = px.bar(advancement_df_long, 
             x="Column", 
             y="Percentage Accomplished", 
             color="Repository", 
             barmode="group", 
             title="State of Advancement by Repository",
             labels={"Percentage Accomplished": "Percentage Accomplished (%)"},
             color_discrete_sequence=["#00B2A9", "#B0E1D9", "#2196F3"])

# Update layout
fig.update_layout(
    xaxis_title="Columns",
    yaxis_title="Percentage Accomplished (%)",
    xaxis_tickangle=45,
    barmode='group'
)

# Save the plot as an HTML file
fig.write_html("../corpus/advancement_chart.html")
