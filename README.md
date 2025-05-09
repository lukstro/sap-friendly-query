# sap-friendly-query

## :file_folder: About this project

While working with __SAP S/4HANA__ data in __Databricks__, I encountered a common challenge among colleagues: the difficulty of dealing with SAP's technical field names. Writing queries often meant diving into wonderfully obscure documentation just to find out what a field like AWREF actually meant. It's not exactly the most efficient way to work, and certainly not welcoming for new users. :baby:

To address this, I developed a lightweight solution that allows users to query __SAP S/4HANA__ tables stored in __Databricks Delta Lake__ using friendly, human-readable field names. This means users can write intuitive queries in either __SQL__ or __PySpark__ without needing to memorize technical __SAP__ terminology.

The tool automatically translates these friendly field names into their corresponding __SAP__ technical names before executing the query, improving accessibility, reducing friction, and making __SAP__ data analysis faster and more user-friendly.

## :open_file_folder: Project Structure

    sap-friendly-query/
    ├── src/
    │   └── translator.py
    ├── config/
    |   └── field_mappings/
    |       └── acdoca.json
    ├── notebooks/
    |   └── demo_translator.py
    ├── requirements.txt
    ├── README.md
