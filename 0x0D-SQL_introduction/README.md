## SQL - Introduction

This repository contains my first project where I worked with SQL and relational databases. I gained experience in introductory data definition and manipulation language, subqueries, and function usage.

### Usage 🐬

The following scripts are used to interact with the databases:

- `3-list_tables.sql`: Use this script to query the database as a MySQL command line argument.
  ```bash
  cat 3-list_tables.sql | mysql -h localhost -u root -p mysql
  ```

### Tasks 📃

1. **List databases**

   - `0-list_databases.sql`: Lists all databases in MySQL.

2. **Create a database**

   - `1-create_database.sql`: Creates the database `hbtn_0c_0`.

3. **Delete a database**

   - `2-remove_databases.sql`: Deletes the database `hbtn_0c_0`.

4. **List tables**

   - `3-list_tables.sql`: Lists all tables in the database.

5. **First table**

   - `4-first_table.sql`: Creates the table `first_table` with the following columns:
     - `id: INT`
     - `name: VARCHAR(256)`

6. **Full description**

   - `5-full_table.sql`: Displays the full description of the `first_table`.

7. **List all in table**

   - `6-list_values.sql`: Lists all rows in the `first_table`.

8. **First add**

   - `7-insert_value.sql`: Inserts a new row in the `first_table` with the values:
     - `id = 89`
     - `name = Holberton School`

9. **Count 89**

   - `8-count_89.sql`: Displays the number of records with `id = 89` in the `first_table`.

10. **Full creation**

    - `9-full_creation.sql`: Creates and fills the table `second_table` with the following records:
      - `id: INT`
      - `name: VARCHAR(256)`
      - `score: INT`

    Records:
    ```
    id = 1, name = "John", score = 10
    id = 2, name = "Alex", score = 3
    id = 3, name = "Bob", score = 14
    id = 4, name = "George", score = 8
    ```

11. **List by best**

    - `10-top_score.sql`: Lists the score and name of all records in the `second_table` in descending order of the score.

12. **Select the best**

    - `11-best_score.sql`: Lists the score and name of all records with a score greater than or equal to 10 in the `second_table` in descending order of the score.

13. **Cheating is bad**

    - `12-no_cheating.sql`: Updates the score of "Bob" to 10 in the `second_table`.

14. **Score too low**

    - `13-change_class.sql`: Removes all records with a score less than or equal to 5 in the `second_table`.

15. **Average**

    - `14-average.sql`: Computes the average score of all records in the `second_table`.

16. **Number by score**

    - `15-groups.sql`: Lists the score and the number of records with the same score in the `second_table` in descending order of the count.

17. **Say my name**

    - `16-no_link.sql`: Lists the score and name of all records in the `second_table` in descending order of the score. It does not display rows without a name value.

18. **Go to UTF8**

    - `100-move_to_utf8.sql`: Converts the `hbtn_0c_0` database to UTF8.

19. **Temperatures #0**

    - `101-avg_temperatures.sql`: Displays the average temperature (Fahrenheit) by city in descending order.

20. **Temperatures #1**

    - `102-top_city.sql`: Displays the three cities with the highest average temperature from July to August in descending order.

21. **Temperature #2**

    - `103-max_state.sql`: Displays the maximum temperature of each state in ascending order of the state name.
