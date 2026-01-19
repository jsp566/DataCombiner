# DataCombiner

For each file type have update frequency
If time is past frequency, do update flow

Update Data flow:
Make new fileid (generic)
Get source file (data specific)
insert file info into db (generic and specific)
Read: insert each row into db (specific)
Interpret: based on each row put data into db with foreign keys (specific)

Run grouping algorithm: disjoint sets (generic)


Search flow:
UI with search parameters and tabs for each table, and a summary table

Backend receives list of parameters

Searches DB with those parameters with intersection, gets ids

(API call to single search APIs, and saves this result)

Shows count for each table, a summary, and all unique identifiers

Click on each tab for full table

