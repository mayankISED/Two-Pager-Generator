import pandas as pd

def execute_query_and_combine_csv(conn, query, csv_path):
    """
    Execute a SQL query and combine results with a CSV file.
    
    Args:
        conn: Database connection
        query: SQL query string
        csv_path: Path to CSV file to combine
        
    Returns:
        Combined DataFrame from query result and CSV
    """
    df = pd.read_sql(query, conn)
    csv_df = pd.read_csv(csv_path)
    combined_df = pd.concat([df, csv_df], ignore_index=True)
    return combined_df

def get_ip_in_force_query(country, year_start, year_end):
    """
    Generate a SQL query to get the number of IPs in force for a given country and year range.

    Args:
        country: The name of the country.
        year_start: The starting year of the range.
        year_end: The ending year of the range.

    Returns:
        SQL query string
    """
    query = f"""
SELECT year, destination_office, origin, indicator, count as "Total Filings"
FROM fact_yearly_pbi
WHERE origin = 'World'
  AND destination_office = '{country}'
  AND indicator IN ('ID7','TM7','PA3')
  AND year >= {year_start} AND year <= {year_end}
"""
    return query

def get_ip_in_force(conn, country, year_start, year_end):
    """
    Get the number of IPs in force for a given country and year range.

    Args:
        conn: A connection object to the database.
        country: The name of the country.
        year_start: The starting year of the range.
        year_end: The ending year of the range.

    Returns:
       Combined result of SQL query and CSV data containing the year and the number of IPs in force for that year
       """
    
    query = get_ip_in_force_query(country, year_start, year_end)
    return execute_query_and_combine_csv(conn, query, "../Data/Ip_In_force.csv")