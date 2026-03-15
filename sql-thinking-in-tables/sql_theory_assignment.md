# Understanding Relational Databases in AI Systems

## 1. What is a database and why is structured storage necessary?

A database is an organized collection of data stored electronically so it can be easily accessed, managed, and updated.

In AI systems, databases store structured data such as:
- User information
- Transaction records
- Product details
- Sensor data
- Logs and analytics data

Structured storage is necessary because it:
- Keeps data organized
- Allows fast searching and retrieval
- Maintains consistency and accuracy
- Enables efficient data analysis for AI models


## 2. Explain the relational database mental model.

A relational database organizes data into **tables**.

Each table contains:
- **Rows** → represent records
- **Columns** → represent attributes of the data

Example:

| Employee_ID | Name | Department |
|-------------|------|------------|
| 101 | Amit | IT |
| 102 | Neha | HR |

Each table usually represents a **single entity** such as employees, customers, or orders. This keeps the data structured and easy to manage.


## 3. What is a primary key?

A **primary key** is a column or set of columns that uniquely identifies each row in a table.

Properties of a primary key:
- Must be **unique**
- Cannot contain **NULL values**

Example:

| Employee_ID (Primary Key) | Name |
|---------------------------|------|
| 101 | Amit |
| 102 | Neha |

Here, `Employee_ID` uniquely identifies each employee.


## 4. What is a database schema?

A **database schema** defines the structure of the database.

It describes:
- Tables
- Columns
- Data types
- Relationships
- Constraints

Example schema for an employee table:

Schemas help maintain **consistency and organization** in the database.


## 5. Explain relationships between tables using foreign keys.

Tables in relational databases are connected using **foreign keys**.

A **foreign key** is a column that references the **primary key of another table**.

Example:

### Users Table

| user_id | name |
|--------|------|
| 1 | Rahul |
| 2 | Priya |

### Orders Table

| order_id | user_id | product |
|---------|--------|---------|
| 101 | 1 | Laptop |
| 102 | 2 | Phone |

Here:
- `user_id` in **Orders table** is a **foreign key**
- It references `user_id` in **Users table**

This creates a relationship between users and their orders.

