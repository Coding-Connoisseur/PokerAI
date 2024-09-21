# Hand History Configuration

This directory contains configuration settings related to the handling, processing, and analysis of poker hand history data. Hand histories provide a critical dataset for training the AI, fine-tuning poker strategies, and evaluating game performance. The configuration files in this directory allow for flexible management of hand history files, controlling how they are parsed, stored, and used within the PokerAI system.

## Directory Structure

- **`hand_history_parser_config.yaml`**: Defines settings for parsing raw hand history files, converting them into structured formats suitable for analysis and training.
  - **File Format**: Specifies the format of the input files (e.g., `.txt`, `.json`, `.csv`).
  - **Delimiter Settings**: Configures delimiters and line breaks for structured hand histories.
  - **Field Mapping**: Maps the raw data fields (e.g., player name, actions, outcomes) to the appropriate data structure used by the AI.
  
- **`storage_config.yaml`**: Contains configuration details related to storing parsed hand history data.
  - **Database Type**: Defines where parsed data should be stored, such as SQL, NoSQL, or in-memory databases.
  - **File Path**: Specifies the directory where raw and processed hand history files are saved.
  - **Compression**: Indicates whether parsed data should be compressed to save storage space.
  
- **`data_cleaning_config.yaml`**: Configurations for cleaning and validating the hand history data before it’s used for training or analysis.
  - **Error Handling**: Defines how to manage incomplete or corrupted hand histories (e.g., discard, impute missing values).
  - **Data Normalization**: Specifies rules for normalizing data, such as formatting dates, currency conversions, or correcting inconsistent player names.
  - **Outlier Detection**: Controls how outlier data (e.g., unusually large bets) are detected and handled.

- **`analysis_config.yaml`**: Contains settings related to the analysis of hand histories for performance metrics, trends, and statistical insights.
  - **Performance Metrics**: Defines which game metrics to calculate (e.g., win rate, average pot size, bluff success rate).
  - **Opponent Profiling**: Specifies how historical data is used to build profiles of opponents (e.g., their aggression level, bluff tendencies).
  - **Data Sampling**: Sets parameters for sampling large datasets (e.g., analyzing only 1 out of every 10 hands to reduce processing time).

## Key Configuration Fields

### 1. **Hand History Parsing**
This module converts raw hand history files from poker platforms into structured formats, which are then used to feed the RL agent and strategy engine. The `hand_history_parser_config.yaml` defines the parsing logic for various file formats and platforms, ensuring compatibility with the PokerAI.

### 2. **Data Storage and Management**
The `storage_config.yaml` allows for flexible storage options, supporting local file storage, cloud databases, or in-memory caching. This flexibility ensures that the system can scale, handling large datasets across multiple poker platforms.

### 3. **Data Cleaning and Validation**
Before the hand histories are used for training or analysis, the system cleans and validates the data using rules specified in `data_cleaning_config.yaml`. This process removes any inconsistencies or corrupt entries and ensures data quality, enhancing the AI’s learning process.

### 4. **Historical Data Analysis**
Using `analysis_config.yaml`, the PokerAI can derive key insights from historical data, such as opponent tendencies, hand strength evolution, and performance trends over time. This data also helps fine-tune strategies by identifying successful patterns and areas for improvement.

## Usage

1. **Modify Parsing Settings**: Update `hand_history_parser_config.yaml` to match the specific format and structure of hand histories from your poker platform. Ensure all necessary fields are correctly mapped to the internal data structure.

2. **Configure Data Storage**: Choose the appropriate storage settings in `storage_config.yaml` based on the available infrastructure. If working with large datasets, consider enabling compression or using a cloud-based database.

3. **Set Up Data Cleaning**: Use `data_cleaning_config.yaml` to handle incomplete or erroneous hand histories. This ensures that only high-quality data is fed into the AI for training and analysis.

4. **Analyze Historical Data**: Leverage `analysis_config.yaml` to specify which performance metrics and opponent profiling methods should be applied to the parsed hand history data.

## Future Enhancements

- **Cross-Platform Hand History Support**: Expand the parser to support more poker platforms and hand history formats, increasing flexibility and compatibility.
- **Automated Error Correction**: Introduce automated data correction techniques, such as AI-driven imputation of missing or erroneous values in hand histories.
- **Enhanced Data Insights**: Add advanced statistical analysis tools, such as identifying long-term trends or forecasting opponent behavior based on historical patterns.

---

The hand history configuration module is essential for enabling the PokerAI to effectively learn from past games, providing high-quality data that informs decision-making and improves poker strategies.
```

### Key Takeaways:
- **Parsing Configuration**: Customizable parsing rules for different hand history formats.
- **Storage**: Flexible storage options for managing parsed and raw data.
- **Cleaning and Validation**: Ensures data quality before it's used for training.
- **Analysis**: Configurable analysis for metrics and trends in hand history data.
