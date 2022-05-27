# Report Comparator 

Compares reports from vendors with internal reports to point out discrepencies, thereby reducing errors and sreamlining reporting and communication. 

The scripts are currently set up to work with Production reports sent by M2 to DJI. It is very much a work in progress. 

## Quick Start

An overview of how to use the scripts. 

1. Format M2's report as a native google sheets document. The following modifications will need to be made:
    - The top row should be the column headers with nothing above
    - There should be no "buffer" column at the leftmost side of the page
    - Any rows at the bottom of the report that you do not want the script to scan should be removed. This includes any "shipped" or "cancelled" items at the bottom of the report
    - Each item should have the OPO number next to it. M2 does not always do this for orders with multiple pieces, so the report should be scanned through quickly by eye and any missing OPO numbers pasted in. 
2. The new report should be shared with "gsheet@production-report-api.iam.gserviceaccount.com" so the script is allowed access to the report. Without doing so you will get a `no sheet found` error. 
3. Update the name of the sheet in the `m2_book` variable so that the script can find the new sheet. 
4. Run the script! If you want to export a csv to be able to manipulate and more easily review the report enter "True" as a kwarg when calling the `compare_lines` method of the `Comparator` class (otherwise no csv will be exported)

## W.I.P

- The script currently does not differentiate between invididual lines that have the same order number. An approach to improving this needs to be determined. 
- It would be more streamlined to have the script pdate an existing google sheet instead of export to csv. This should be implimented in the future. 
